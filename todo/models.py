from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='todos')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title
