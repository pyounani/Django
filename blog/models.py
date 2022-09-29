from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 추후 author 작성

    def __str__(self):
        return f'[{self.pk}]{self.title}    {self.create_at}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'