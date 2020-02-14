var count = 0;
$(document).ready(function(){
    $('.guess_box').click(function(){
        $('li').remove();
        var discount = Math.floor((Math.random()*5)+5);
        $(this).append(`<li>you clicked me!!</li>`);
        // $('.guess_box').unbind('click');
        $('.guess_box').each(function(){//각각의 .guess_box 요소에 대하여 unbind.
            $(this).unbind('click');
        });
    });
});