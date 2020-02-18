$(".menu_entrees>li>ul").addClass("menu_list");

$(document).ready(function(){
    var vegiMode = false;
    $fish = [];
    $meat = [];
    $('#vegOn').click(function(){
        vegiMode = true;
        $("#mode").text('For Vegitarian!!');
        $fish = $('.fish').parent().parent().detach();
        $('.hamburger').replaceWith("<li class='portobello'>portobello</li>");
        $('.meat').after("<li class='tofu'><em>tofu</em></li>");
        $meat = $('.meat').detach();
        /*parent(), children(), 
        prev()(DOM 트리를 그렸을 때 왼쪽에 있는 형제 요소)
        next()(DOM 트리를 그렸을 때 오른쪽에 있는 형제 요소)
        closest("css선택자")(부모 방향으로 거슬러 올라갔을 때 인수에 부합하는 요소 가운데 가장 가까운 것)
        siblings()모든 next()와 prev()요소*/
        
        /*DOM요소 조작 메소드
        -remove(), empty(), 
        */

    })

    $('#restoreMe').click(function(){
        vegiMode = false;
        $('#mode').text('For Everybody!!');
        $(".menu_entrees").children().first().before($fish);
        $('.portobello').replaceWith("<li class='hamburger'>hamburger</li>");
        $('.tofu').each(function(i){
            $(this).after($meat[i]);
        });
        $(".tofu").remove();
    })
})