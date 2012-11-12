/*
 * Helper JS to change classnames and HTML on the fly
 * because it would be too hard to do it customizing
 * each template
 *
 */

(function($){
$(document).ready(function(){

    /* Automatically generated portal status messages */

    $('dl.portalMessage #kssPortalMessage').each(function(){
        var message = $(this);
        message.removeClass('portalMessage');
        var replacement = $(
            '<div data-alert="alert" class="alert ' + message[0].className + '">' +
                    '<strong>' + message.find('dt').html() + '</strong> ' +
                    message.find('dd').html() +
            '</div>');
        message.replaceWith(replacement);
    });

    /* Convert input[type=buttons] to button tags */
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

    /* Add btn class to the rest form buttons */
    $('input[type="submit"], input[type="button"]').addClass('btn');

    /* Edit form tabs */

    $('form ul.formTabs').each(function(){
        var ul = $(this);
        ul.addClass('nav');
        ul.addClass('nav-tabs')
        ul.removeClass('formTabs');
        ul.find('li').removeClass('formTab firstFormTab lastFormTab');

        ul.find('li:first').addClass('active');
        ul.find('li').click(function(){
            $(this).parent().find('li').removeClass('active');
            $(this).addClass('active');
        });
        ul.find('li a span').each(function(){
            var span = $(this);
            var a = span.parent().html(span.html);
        });
    });

    /* Help text in Archetypes forms */
    $('.formHelp').addClass('help-block').removeClass('formHelp');

    /* Plone's default class for tables */
    $('table.listing').addClass('zebra-striped');


    /*
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
    */
});
})(jQuery);