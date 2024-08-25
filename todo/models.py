from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title
