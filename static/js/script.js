$(document).ready(function(){

function displayDate(){
	document.getElementById("showtime").innerHTML=Date();
};

$.ajax('/createdata',{
	type: 'get',
	staueCode:{
	400: function(response){
		alert('400 failed');
}, 
	400: function(response){
		alert('500 failed');
}, 
	success: function(response){
		alert('success');
},
}
});

});
