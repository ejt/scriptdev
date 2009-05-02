$(document).ready(function() {
    $('#tab a').click(function() {
        $('#panelcontent').slideToggle();
        return false;
    });

    $('#developers li').hover(function() {
        $(this).stop().animate({minHeight: '200px'}, 'slow');
    }, function() {
        $(this).stop().animate({minHeight: '42px'}, 'slow');
    });
});
