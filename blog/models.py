from django.db import models

# Create your models here.
class Blog(models.Model):
    title= models.TextField()
    tag_word=models.TextField(default="random")
    intro= models.TextField()
    body=models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-date_time"]


class Comment(models.Model):
    post=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['date_add']