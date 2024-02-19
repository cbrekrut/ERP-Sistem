function toggleTaskForm(counter) {
    var overlayId = "taskFormOverlay_" + counter;
    var overlay = document.getElementById(overlayId);
    overlay.style.display = (overlay.style.display === "none") ? "flex" : "none";
}

function saveTask(subordinateName, counter) {
    var formId = "taskFormInner_" + counter;
    var form = document.getElementById(formId);

    var formData = new FormData(form);
    
    // Получаем user_id из атрибута данных
    var userId = document.querySelector("[data-user-id]").getAttribute("data-user-id");
    
    formData.append('user_id', userId);  // Добавляем идентификатор пользователя

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/save_task/' + userId + '/', true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Закрываем форму после успешного сохранения задачи
                toggleTaskForm(counter);
                alert("Задача успешно сохранена для: " + subordinateName);
            } else {
                alert("Произошла ошибка при сохранении задачи");
            }
        }
    };

    xhr.send(formData);
}