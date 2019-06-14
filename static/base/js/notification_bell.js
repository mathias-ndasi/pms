$(document).ready(function () {

    // count the number of messages
    let messages = document.querySelectorAll(".messages ul li");

    // ANIMATEDLY DISPLAY THE NOTIFICATION COUNTER.
    $('#noti_Counter')
        .css({
            opacity: 0
        })
        .text(messages.length) // ADD DYNAMIC VALUE (YOU CAN EXTRACT DATA FROM DATABASE OR XML).
        .css({
            top: '-10px'
        })
        .animate({
            top: '-2px',
            opacity: 1
        }, 500);

    $('#noti_Button').click(function () {
        // TOGGLE (SHOW OR HIDE) NOTIFICATION WINDOW.
        $('#notifications').fadeToggle('fast', 'linear');

        $('#noti_Counter').fadeToggle('slow', 'linear'); // TOGGLE THE COUNTER.

        return false;
    });

    // HIDE NOTIFICATIONS WHEN CLICKED ANYWHERE ON THE PAGE.
    $(document).click(function () {
        $('#notifications').hide();
        $('#noti_Counter').fadeToggle('slow', 'linear'); // TOGGLE THE COUNTER.
    });

    $('#notifications').click(function () {
        return false; // DO NOTHING WHEN CONTAINER IS CLICKED.
    });


});