const body = document.querySelector("body")

const IMG_NUMBER = 3;

function paintImg(imgNumber){
    const img = new Image();
    img.src = `./img/${imgNumber+1}.jpg`;
    img.id = 'image'
    body.appendChild(img);
    img.width = 200;
    img.height = 200;
}

function getRandom(){
    const number = Math.floor(Math.random()*IMG_NUMBER);
    return number
}

function init(){
    const ranNumber = getRandom();
    paintImg(ranNumber);
}

init();