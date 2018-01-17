var friendId;

function count() {
    friendId = document.getElementById("friends").getElementsByTagName("p").length;
    document.getElementById("qty").innerHTML = friendId;
}
function addFriend() {
    friendId++;
    var html = '<span>Nome: <input type="text" name="name-'+friendId+'"> Email: <input type="text" name="email-'+friendId+'"></span>' +
               '<span class="glyphicon glyphicon-remove-circle" onclick=\'removeElement("friend-' + friendId + '"); return false;\'></span>';
    addElement('friends', 'p', 'friend-' + friendId, html);
}

function addElement(parentId, elementTag, elementId, html) {
    var p = document.getElementById(parentId);
    var newElement = document.createElement(elementTag);
    newElement.setAttribute('id', elementId);
    newElement.innerHTML = html;
    p.appendChild(newElement);
    document.getElementById("qty").innerHTML=friendId;
}

function removeElement(elementId) {
    var element = document.getElementById(elementId);
    element.remove();
    friendId--;
    document.getElementById("qty").innerHTML=friendId;
}
window.onload = count;
