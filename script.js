var count = 0;
function dosomething(el) {
    el.innerText = "You Clicked The Button!";
    count = count + 1;
    if (count === 30) {
        var element = document.createElement('p');
        element.innerText = "YOU FOUND THE SECRET!!!!!!!";
        document.body.appendChild(element);
        create('button', 'Click For Your Prize', document.body, 'id', 'prz')
    }
}

function create(el, text, parent, attr, attrval) {
    var element = document.createElement(el);
    element.innerText = text;
    element.setAttribute(attr, attrval);
    parent.appendChild(element);
}

var prz = document.getElementById('prz')
prz.addEventListener('click', click)

function click(){
    window.open('https://therickroll.com', '_blank');

}