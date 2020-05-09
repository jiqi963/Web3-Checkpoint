$(document).ready(function(){

$('button#toggle-1').click(_ => {
		$('p1').toggle()
	})

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
