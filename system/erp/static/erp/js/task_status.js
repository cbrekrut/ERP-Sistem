function takeTask(taskId) {
    // Отправить AJAX-запрос на сервер для изменения статуса задачи на 'runs'
    $.ajax({
        type: 'POST',
        url: '/change_task_status/',
        data: { task_id: taskId, new_status: 'runs' },
        success: function(data) {
            // Обновить страницу или выполнить другие действия по желанию
            location.reload();
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function completeTask(taskId) {
    // Отправить AJAX-запрос на сервер для изменения статуса задачи на 'done'
    $.ajax({
        type: 'POST',
        url: '/change_task_status/',
        data: { task_id: taskId, new_status: 'done' },
        success: function(data) {
            // Обновить страницу или выполнить другие действия по желанию
            location.reload();
        },
        error: function(error) {
            console.log(error);
        }
    });
}