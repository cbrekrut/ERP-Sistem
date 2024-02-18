function toggleTaskForm(counter, subordinateName) {
    var overlayId = "taskFormOverlay_" + counter;
    var overlay = document.getElementById(overlayId);
    overlay.style.display = (overlay.style.display === "none") ? "flex" : "none";
}

function saveTask(subordinateName) {
    var formId = "taskFormInner_" + subordinateName.replace(/\s+/g, '_');
    var form = document.getElementById(formId);

    var formData = new FormData(form);
    formData.append('user_id', '{{ user.id }}');  // Добавляем идентификатор пользователя

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/save_task/{{ user.id }}/', true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Закрываем форму после успешного сохранения задачи
            toggleTaskForm(subordinateName.replace(/\s+/g, '_'));
            alert("Задача успешно сохранена для: " + subordinateName);
        } else if (xhr.readyState === 4) {
            alert("Произошла ошибка при сохранении задачи");
        }
    };

    xhr.send(formData);
}