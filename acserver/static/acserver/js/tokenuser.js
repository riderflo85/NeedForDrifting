$(document).ready(function() {
    let tokenLink = $('#displayToken');
    let tokenForDisplay = $('#userToken');

    tokenLink.on('click', function() {
        if (tokenForDisplay.hasClass('d-none')) {
            tokenForDisplay.removeClass('d-none');
        } else {
            tokenForDisplay.addClass('d-none');
        }
    });
});