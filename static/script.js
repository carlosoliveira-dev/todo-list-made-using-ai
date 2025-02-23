async function fetchTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.task;
        const button = document.createElement('button');
        button.textContent = 'Remover';
        button.onclick = () => deleteTask(task.id);
        li.appendChild(button);
        taskList.appendChild(li);
    });
}

async function addTask() {
    const taskInput = document.getElementById('taskInput');
    if (!taskInput.value.trim()) return;

    await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task: taskInput.value })
    });

    taskInput.value = '';
    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`/tasks/${id}`, { method: 'DELETE' });
    fetchTasks();
}

document.addEventListener('DOMContentLoaded', fetchTasks);
