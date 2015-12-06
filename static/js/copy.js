$(document).ready(function() {
    var change_icons = function(){
        $('.fa-clipboard').toggleClass('hidden');
        $('.fa-check-circle').toggleClass('hidden');
    };

    var clipboard = new Clipboard('#copy-to-clipboard');

    clipboard.on('success', function(e){
        change_icons();
        setTimeout(change_icons, 1000)
    });
});