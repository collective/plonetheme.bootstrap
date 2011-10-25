(function($){
$(document).ready(function(){
    $('dl.portalMessage:not(#kssPortalMessage)').each(function(){
        var message = $(this);
        message.removeClass('portalMessage');
        var replacement = $(
            '<div data-alert="alert" class="alert-message fade in ' + message[0].className + '">' +
                '<a class="close" href="#">×</a>' +
                '<p>' + 
                    '<span class="label">' + message.find('dt').html() + '</span> ' +
                    message.find('dd').html() +
                '</p>' + 
            '</div>');
        message.replaceWith(replacement);
    });

    var foundPrimary = false;
    $('div.formControls input[type="submit"]').each(function(){
        var input = $(this);
        var button = $('<button type="submit" class="btn" name="' + input.attr('name') + '">' + 
            input.attr('value') + '</button>');

        if(input.hasClass('context') && !foundPrimary){
            button.addClass('primary');
            foundPrimary = true;
        }
        input.replaceWith(button);
    });

    $('form ul.formTabs').each(function(){
        var ul = $(this);
        ul.addClass('tabs');
        ul.find('li:first').addClass('active');
        ul.find('li').click(function(){
            $(this).parent().find('li').removeClass('active');
            $(this).addClass('active');  
        });
    });

    $('table.listing').addClass('zebra-striped');
    $('input[type="submit"],input[type="button"]').addClass('btn');

    $('ul#navigation li[data-dropdown="dropdown"]').hover(function(){
        $(this).addClass('open'); 
    }, function(){
        $(this).removeClass('open'); 
    });
    $('ul#navigation li[data-dropdown="dropdown"] ul').hover(function(){}, function(){
        $(this).parent().removeClass('open');
    });
    $('ul#navigation li[data-dropdown="dropdown"] a').click(function(){
        window.location = $(this).attr('href');
    });
});
})(jQuery);