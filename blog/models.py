from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    #%Y 2022, %y 22
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # μΆν author μμ±

    def __str__(self):
        return f'[{self.pk}]{self.title}    {self.create_at}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

