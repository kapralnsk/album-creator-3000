$(document).ready(function() {
    $('#next').on('click', function (event) {
        $('#loaded-text').toggleClass('hidden');
        $('#loader').toggleClass('hidden');
        $.get('get_album', function (data) {
            $('#loaded-text').toggleClass('hidden');
            $('#loader').toggleClass('hidden');
            $('#album').html(data);
        })
    });
});