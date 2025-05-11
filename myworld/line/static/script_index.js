var sho = (a) => {
document.getElementById("logi").style.display ="none";
document.getElementById("chan").style.display ="none";
document.getElementById(a).style.display ="inline";
}

var hid = (a) => {
document.getElementById(a).style.display ="none";
}

$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});