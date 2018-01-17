from flask import Flask, render_template, request
import random
import smtplib
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def sorteio():
    if request.method == "POST":
        post_data = {}
        friends_with_emails = {}

        for i in request.form:
            post_data[i] = request.form[i]

        for i in range(len(post_data) / 2):
            friends_with_emails[post_data["name-" + str(i)]] = post_data["email-" + str(i)]

        # print friends_with_emails
        sorteio = sort_friends(friends_with_emails.keys())
        # print sorteio
        for friend in sorteio:
            # send_email(friends_with_emails[friend], sorteio[friend])
            print 'Email enviado para {0}'.format(friends_with_emails[friend])
            # print(friends_with_emails[friend], sorteio[friend])

        return render_template('ok.html')
    else:
        return render_template('sorteio.html')


def send_email(giver_email, receiver_name):
    fromaddr = ''
    toaddrs = [giver_email]
    msg = "\r\n".join([
        "From: user_me@gmail.com",
        "To: {0}".format(giver_email),
        "Subject: Amigo Oculto",
        "",
        "Voce saiu com: {0}".format(receiver_name)])











    username = 'sauloml'
    password = 'pqpsoftass'
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


if __name__ == '__main__':
    app.debug = True
    app.run()
