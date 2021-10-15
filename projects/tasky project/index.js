const taskContainer = document.querySelector(".task_container");

let globalStore = [];

const generateNewCard = (taskData) =>
 `
      <div class="col-md-6 col-lg-4" id=${taskData.id}>
        <div class="card">
          <div class="card-header d-flex justify-content-end gap-2">
            <button type="button" id=${taskData.id} class="btn btn-outline-success" onclick="editCard.apply(this, arguments)">
              <i class="fas fa-pencil-alt" id=${taskData.id} onclick="editCard.apply(this, arguments)"></i>
            </button>
            <button type="button" class="btn btn-outline-danger" id=${taskData.id} onclick="deleteCard.apply(this, arguments)">
              <i class="fas fa-trash-alt" id=${taskData.id} onclick="deleteCard.apply(this, arguments)"></i>
              </button>
          </div>
          <img src= ${taskData.imageUrl}>
          <div class="card-body">
            <h5 class="card-title">${taskData.taskTitle}</h5>
            <p class="card-text">${taskData.taskDescription}</p>
            <a href="#" class="btn btn-primary">${taskData.taskType}</a>
        </div>
          <div class="card-footer">
            <button type="button" id=${taskData.id} class="btn btn-outline-primary float-end">
              Open Task
            </button>
          </div>
        </div>
      </div>
 `;


 // store the data into globalStore and not to delete the data when we refresh...
const loadInitialCardData = () => {
  // getting data from the tasky card data of localstorage....
  const getCardData = localStorage.getItem("tasky");

  // converting the string into the normal object.....
  const {cards} = JSON.parse(getCardData);

  // loop over those array of task object to create a HTML card.......
  cards.map((cardObject) => {
    
    // inject it into DOM...
    taskContainer.insertAdjacentHTML("beforeend",generateNewCard(cardObject));

    // update our global store....
    globalStore.push(cardObject);
  })
};

updateLocalStorage = () => {
  localStorage.setItem("tasky",JSON.stringify({cards:globalStore}));
};

const saveChanges = () => {
    const taskData = {
        id: `${Date.now()}`, //unique number for id
        imageUrl: document.getElementById("imageurl").value,
        taskTitle: document.getElementById("tasktitle").value,
        taskType: document.getElementById("tasktype").value,
        taskDescription: document.getElementById("taskdescription").value,
    };
    // HTML code
  const createNewCard = generateNewCard(taskData);

  taskContainer.insertAdjacentHTML("beforeend", createNewCard);
  globalStore.push(taskData);

  // add to localstorage
  updateLocalStorage();
};


const deleteCard = (event) => {
  event = window.event;
  // id
  const targetID = event.target.id;
  const tagname = event.target.tagName; //BUTTON

  // match the id of the element with the id inside the elemnet
  // if match found then remove it
  globalStore = globalStore.filter((cardObject) => cardObject.id !== targetID);

  updateLocalStorage();
  // contact parent
  if(tagname === "BUTTON"){
    return taskContainer.removeChild(event.target.parentNode.parentNode.parentNode);
   }else{
    return taskContainer.removeChild(event.target.parentNode.parentNode.parentNode.parentNode);
   }
};

const editCard = (event) => {
  event = window.event;
  // id
  const targetID = event.target.id;
  const tagname = event.target.tagName; //BUTTON

  let parentElement;

  if(tagname === "BUTTON"){
    parentElement = event.target.parentNode.parentNode;
   }else{
    parentElement = event.target.parentNode.parentNode.parentNode;
   }
   // console.log(parentElement.childNodes); --> it helps to get below childNodes array values
   //                                            and we have to look into the class name in html
   let taskTitle = parentElement.childNodes[5].childNodes[1];
   let taskDescription = parentElement.childNodes[5].childNodes[3];
   let taskType = parentElement.childNodes[5].childNodes[5];
   let submitButton = parentElement.childNodes[7].childNodes[1];

   taskTitle.setAttribute("contenteditable", "true");
   taskDescription.setAttribute("contenteditable", "true");
   taskType.setAttribute("contenteditable", "true");
   submitButton.setAttribute("onclick","saveEditChanges.apply(this, arguments)");
   submitButton.innerHTML = "save changes"
}

const saveEditChanges = (event) => {
  event = window.event;
  // id
  const targetID = event.target.id;
  const tagname = event.target.tagName; //BUTTON

  let parentElement;

  if(tagname === "BUTTON"){
    parentElement = event.target.parentNode.parentNode;
   }else{
    parentElement = event.target.parentNode.parentNode.parentNode;
   }
   // console.log(parentElement.childNodes); --> it helps to get below childNodes array values
   //                                            and we have to look into the class name in html
   let taskTitle = parentElement.childNodes[5].childNodes[1];
   let taskDescription = parentElement.childNodes[5].childNodes[3];
   let taskType = parentElement.childNodes[5].childNodes[5];
   let submitButton = parentElement.childNodes[7].childNodes[1];

   const updateData = {
     taskTitle: taskTitle.innerHTML,
     taskType: taskType.innerHTML,
     taskDescription: taskDescription.innerHTML,
   };

   globalStore = globalStore.map((task) => {
     if (task.id === targetID) {
       return {
        id: task.id, //unique number for id
        imageUrl: task.imageUrl,
        taskTitle: updateData.taskTitle,
        taskType: updateData.taskType,
        taskDescription: updateData.taskDescription,
       };
     }
     return task;
   });
   updateLocalStorage();

   // to return back to "open task" after clicking on "save changes" and become content not editable.........
   taskTitle.setAttribute("contenteditable", "false");
   taskDescription.setAttribute("contenteditable", "false");
   taskType.setAttribute("contenteditable", "false");
   submitButton.setAttribute("onclick","saveEditChanges.apply(this, arguments)");
   submitButton.innerHTML = "Open Task"
}