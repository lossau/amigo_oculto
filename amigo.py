# -*- coding: utf-8 -*-
import smtplib
import random


def send_email(giver_email, receiver_name, subject):
    fromaddr = ''
    toaddrs = [giver_email]
    # msg = 'Why,Oh why!'
    msg = "\r\n".join([
        "From: sorteador@amigo.oculto",
        "To: {0}".format(giver_email),
        "Subject: {0}".format(subject),
        "",
        "Voce saiu com: {0}".format(receiver_name)])
    username = ''
    password = ''
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


def sort_friends(people):
    receivers = people[:]
    givers = people[:]

    listsEqual = True

    while listsEqual:
        random.shuffle(receivers)
        duplicate = [i for i, j in zip(givers, receivers) if i == j]
        if not duplicate:
            listsEqual = False

    return dict(zip(givers, receivers))


people_with_email = {
    "Nome1": "nome@email.com",
    "Nome2": "nome@email.com",
    "Nome3": "nome@email.com"
}

subject = "SORTEIO - AMIGO Oculto"

sorteio = sort_friends(people_with_email.keys())
# print sorteio
# print "--------------------------"

for person in sorteio:
    # send_email(people_with_email[person], sorteio[person], subject)
    print(people_with_email[person], sorteio[person])
    print 'Email enviado para {0}'.format(people_with_email[person])
