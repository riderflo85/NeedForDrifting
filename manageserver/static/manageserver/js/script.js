$(document).ready(function() {
	
	setTimeout(function(){
        $('body').addClass('loaded');
        $('.navbar').fadeIn('slow', function(el) {
        });
        $('#loader').remove();
    }, 2000);
});