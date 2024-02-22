function toggleTaskForm(counter) {
    var overlayId = "taskFormOverlay_" + counter;
    var overlay = document.getElementById(overlayId);
    overlay.style.display = (overlay.style.display === "none") ? "flex" : "none";
}

function saveTask(subordinateName, counter, email) {
    var formId = "taskFormInner_" + counter;
    var form = document.getElementById(formId);
    var formData = new FormData(form);

    var userId = document.querySelector("[data-user-id]").getAttribute("data-user-id");
    console.log(userId);
    formData.append('user_id', subordinateName);
    formData.append('email', email);

    $.ajax({
        type: 'POST',
        url: '/save_task/' + userId + '/',
        data: formData,
        processData: false,  // Не обрабатывать данные (уже FormData)
        contentType: false,  // Не устанавливать Content-Type
        success: function(data) {
            // Закрываем форму после успешного сохранения задачи
            toggleTaskForm(counter);
            alert("Задача успешно сохранена для: " + subordinateName);
        },
        error: function(xhr, status, error) {
            alert("Произошла ошибка при сохранении задачи");
            console.error(xhr.responseText);
        }
    });
}