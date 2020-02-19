var canvas = document.querySelector("#signature");

var signaturePad = new SignaturePad(canvas);

const download = document.querySelector('#download');
const save = document.querySelector('#save');
const clear = document.querySelector('#clear');
const input = document.querySelector('#fileName');
const dataURL = document.querySelector('#dataURL');
const fileName = document.querySelector('#fileName');
const form = document.querySelector('#form');

input.placeholder = "file name";

//https://stackoverflow.com/questions/8126623/downloading-canvas-element-to-an-image
//data를 다운로드하는 다른 방법은 없을까...
var downloadPNG = function(){
    if(signaturePad.isEmpty()){
        alert("먼저 사인을 하세요!!")
    }else{
    var link = document.createElement('a');
    var filename = input.value;
    if(filename == ""){
        link.download = 'signature.png';
    }else{
        link.download = filename+".png";
    }
    link.href = document.getElementById('signature').toDataURL()    
    // input.value = link.href;
    // $('#saveForm').val(link.href);
    // console.log($('#saveForm').val());
    link.click();
    // link.text = "aaaaa";
    // document.getElementsByTagName('body')[0].appendChild(link);
    }
  }

function clearHandler(event){
    signaturePad.clear();
}

function saveHandler(event){
    dataURL.value = document.getElementById('signature').toDataURL();
    var filename = "";
    if(input.value == ""){
        filename = 'signature.png';
    }else{
        filename = input.value+".png";
    } 
    $.ajax({ url: "/rest/1/pages/245", // 클라이언트가 HTTP 요청을 보낼 서버의 URL 주소 
    data: { 
        filename: filename,
        dataurl :document.getElementById('signature').toDataURL()
     }, // HTTP 요청과 함께 서버로 보낼 데이터 
    method: "GET", // HTTP 요청 메소드(GET, POST 등) 
    dataType: "json" // 서버에서 보내줄 데이터의 타입 
    })
    console.log(document.getElementById('signature').toDataURL());

    // fileName.value = filename;
    // console.log(fileName.value)
    // form.submit();

}

download.addEventListener("click", downloadPNG);

clear.addEventListener("click", clearHandler);

save.addEventListener('click', saveHandler);



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
