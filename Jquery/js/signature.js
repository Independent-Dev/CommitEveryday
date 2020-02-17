var canvas = document.querySelector("#signature");

var signaturePad = new SignaturePad(canvas);

const save = document.querySelector('#save');
const clear = document.querySelector('#clear');
const input = document.querySelector('#fileName')
input.placeholder = "file name";

//https://stackoverflow.com/questions/8126623/downloading-canvas-element-to-an-image
//data를 다운로드하는 다른 방법은 없을까...
var download = function(){
    if(signaturePad.isEmpty()){
        alert("먼저 사인을 하세요!!")
    }else{
    var link = document.createElement('a');
    fileName = input.value;
    if(fileName == ""){
        link.download = 'signature.png';
    }else{
        link.download = fileName+".png";
    }
    link.href = document.getElementById('signature').toDataURL()    
    link.click();
    // link.text = "aaaaa";
    // document.getElementsByTagName('body')[0].appendChild(link);
    }
  }

function clearHandler(event){
    signaturePad.clear();
}

save.addEventListener("click", download);

clear.addEventListener("click", clearHandler);

// function saveHandler(event){
//     console.log(1);
//     var content = signaturePad.toDataURL();
//      = content;

//     // const image = new Image();
//     // image.src = content;
//     // const body = document.querySelector('body');
//     // body.appendChild(image);
    
//     console.log(content);
// }
