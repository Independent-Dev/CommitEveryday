const toDoForm = document.querySelector('.js-toDoForm'),
    toDoInput = toDoForm.querySelector('input'),
    toDoList = document.querySelector('.js-toDoList');

const TODOS_LS = "toDos";

function loadToDos(){
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if (loadedToDos !== null){
        const restoredToDo = JSON.parse(loadedToDos);
        restoredToDo.forEach(function(todo){
            paintToDo(todo.text);
        });
    }
}

let toDos = [];

function deleteToDo(event){
    const btn = event.target;
    const li = btn.parentNode;
    toDoList.removeChild(li);
    const cleanToDo = toDos.filter(function(todo){
        return todo.id !== parseInt(li.id);
    });
    toDos = cleanToDo;
    saveToDo();
}

function saveToDo(){
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}

function paintToDo(text){
    const li = document.createElement('li');
    const delBtn = document.createElement('button');
    const span = document.createElement('span');
    const newId = toDos.length+1;
    li.id = newId;
    delBtn.innerText = "❌";
    delBtn.addEventListener("click", deleteToDo);
    span.innerText = text;
    li.appendChild(delBtn);
    li.appendChild(span);
    toDoList.appendChild(li);
    const toDosObj = {
        text : text,
        id : newId 
    }
    toDos.push(toDosObj);
    saveToDo();
}

function handleSubmit(event){
    event.preventDefault();
    const currentValue = toDoInput.value
    paintToDo(currentValue);
    toDoInput.value = "";
}

function init(){
    loadToDos();
    toDoForm.addEventListener("submit", handleSubmit);
}

init()