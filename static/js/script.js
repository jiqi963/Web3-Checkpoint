$(document).ready(function(){

function displayDate(){
	document.getElementById("showtime").innerHTML=Date();
}

$.get("/countries",function(){
	alert('Load sccess');
}).fail(function(){
	alert('Load fail');
});

});
