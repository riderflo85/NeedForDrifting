$(document).ready(function() {
	
	setTimeout(function(){
        $('body').addClass('loaded');
        $('.navbar').fadeIn('slow', function(el) {
        });
        $('#loader').remove();
        $('#container-msg').fadeOut("slow", function(el) {
            this.remove();
        });
    }, 2000);
});