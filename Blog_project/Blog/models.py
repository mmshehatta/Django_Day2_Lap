from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100 , null=False , blank=False , unique=True)

    body = models.TextField(max_length=1000 , null=False , blank=False)

    posted_at = models.DateTimeField(auto_now_add=True)

    cover_photo = models.ImageField(upload_to='blog/articles/covers' , default='blog/articles/covers/default-cover.jpg')

    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ' {} Article '.format(self.title)

class KeyWord(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='keywords') 

