from django.db import models
from authentication.models.CustomUser import CustomUser

class Task(models.Model):
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('waits', 'Ожидает'),
        ('runs', 'В работе'),
        ('done', 'Выполено'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waits')

    def __str__(self):
        return f'Task for {self.assigned_to.get_full_name()}'