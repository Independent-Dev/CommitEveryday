
$(document).ready(function(){
    $('.guess_box').click(checkForCode);
    $('.guess_box').hover(function(){
        $(this).addClass('my_hover');
    },
    function(){
        $(this).removeClass('my_hover');
    })
});

var hideCode = function(){
    var numRand = getRandom(4);
    $(".guess_box").each(function(index, value){
        if(numRand==index){
            $(this).append("<span id = 'has_discount'></span>");
            return false;//.each()메서드 루프를 빠져나오는 방법!!
        }
    });
};

hideCode()

function checkForCode(){
    var discount;
    //hideCode()로 하면 왜 내가 생각하는대로 작동하지 않는지는 random의 작동방식을 잘 모르기 때문이기도 함. 
    if($.contains(this, document.getElementById('has_discount'))){
        var my_num = getRandom(5);
        discount = `<p>Your Discount is ${my_num}%</p>`;    
    }else {
        discount = `<p>Sorry, no discount this time!</p>`;
        $('.guess_box').each(function(){
            if($.contains(this, document.getElementById('has_discount'))){
                $(this).addClass("discount");
            }else{
                $(this).addClass("no_discount");
            }
            $(this).unbind('click');
        });
    }
    $(this).append(discount);

    
}

function getRandom(number){
    return Math.floor(Math.random()*number);
}