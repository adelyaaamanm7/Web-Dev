
(() => {
  const formElement = document.querySelector('#todo-form');
  const inputElement = document.querySelector('#task-input');
  const listElement = document.querySelector('#todo-list');

  const createTodoItem = (taskText) => {
 
    const listItemElement = document.createElement('li');
    listItemElement.classList.add('todo-item');

   
    const checkboxElement = document.createElement('input');
    checkboxElement.type = 'checkbox';
    checkboxElement.classList.add('checkbox');

  
    const textElement = document.createElement('span');
    textElement.classList.add('task-text');
    textElement.textContent = taskText;

   
    const deleteButtonElement = document.createElement('button');
    deleteButtonElement.type = 'button';
    deleteButtonElement.classList.add('delete-button');
    deleteButtonElement.textContent = 'Delete';
    deleteButtonElement.setAttribute('aria-label', `Delete task: ${taskText}`);

   
    checkboxElement.addEventListener('change', (event) => {
      const isChecked = event.target.checked;
      listItemElement.classList.toggle('is-done', isChecked);
    });

    deleteButtonElement.addEventListener('click', () => {
      listElement.removeChild(listItemElement);
    });


    listItemElement.appendChild(checkboxElement);
    listItemElement.appendChild(textElement);
    listItemElement.appendChild(deleteButtonElement);

    return listItemElement;
  };

  const addTask = () => {
    const rawValue = inputElement.value;
    const trimmedValue = rawValue.trim();

    if (!trimmedValue) {
      alert('Please type a task first.');
      return;
    }

    const todoItemElement = createTodoItem(trimmedValue);
    listElement.appendChild(todoItemElement);

    inputElement.value = '';
    inputElement.focus();
  };

  formElement.addEventListener('submit', (event) => {
    event.preventDefault();
    addTask();
  });
})();


  