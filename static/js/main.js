$(document).ready(function () {

    // Re-Boot trading years appear in the footer
     
    $('#trading-year').text('2019 - ' + new Date().getFullYear());
    
    // Shopping cart popover
    
    $('#cart-popover').popover({
        html : true,
        container: 'body',
        content: function() {
            return $('#popover_content_wrapper').html();
        }
    });
});

// Scroll to top of webpage...

    $("a[href='#move-up']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 800);
        return false;
    });

    // If position of vertical scroll is above 575px, for 
    // return to top button to disappear.
    
    $(window).scroll(function () {
        if ($(this).scrollTop() > 575) {
            $('.move-top').fadeIn();
        } else {
            $('.move-top').fadeOut();
        }
    });