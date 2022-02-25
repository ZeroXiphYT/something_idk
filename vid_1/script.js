function start(){
    swal({
        title:"You Clicked The Button",
        text: "You Clicked The Button, That's Pretty Cool",
        icon:"success",
        buttons:["I Don't Care", "Ok, Thanks"]
    })

}

var btn = document.getElementById('btn')
btn.addEventListener('click', start)