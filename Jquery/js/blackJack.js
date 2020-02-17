function Card(suit, value){
    this.suit = suit;
    this.value = value;
    this.good_card = true;
}
var deck = [];
var usedCard = [];
var current_total = 0;

const newGame = document.querySelector("#newGame");
newGame.addEventListener('click', clearBoard);
const moreCard = document.querySelector("#moreCard");

for(var i = 0; i<52; i++){
    var temp = "";
    if(parseInt(i/13)==0){
        temp+="heart";
    }else if(parseInt(i/13)==1){
        temp+="dia";
    }else if(parseInt(i/13)==2){
        temp+="clubs";
    }else temp+="spade";
    deck[deck.length] = new Card(temp, (i%13)+1);
}

function getRandom(number){
    var my_num = Math.floor(Math.random()*number);
    return my_num;
}

function hit(){
    var index = getRandom(52);
    var c = deck[index];
    while(!c.good_card){
        index = getRandom(52);
        c = deck[index]; 
    }
    deck[index].good_card = false;
    usedCard[usedCard.length] = index;
    $('#my_hand').append("<div class='card'>"+c.suit+", "+c.value+"</div>");
    current_total+=c.value;
}

function checkCurrentTotal(total){
    if(total>21){
        $('#btnDeal').append("<div class='bust'>Bust!!</div>");
        $('#btnDeal div').css('font-size', '50px');
        moreCard.removeEventListener('click', moreCardHandler);
    }
}

function clearBoard(){
    $('#btnDeal div').remove();
    $('#my_hand').children().remove();
    for(var i = 0; i<usedCard.length; i++){
        var temp = usedCard[i];
        deck[temp].good_card = true;
        current_total = 0;
    }
    init();
}

function moreCardHandler(){
    hit();
    checkCurrentTotal(current_total);
}

function init(){
    moreCard.addEventListener('click', moreCardHandler);
}

init();