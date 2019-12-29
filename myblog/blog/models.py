from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=128)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse("blog:post_list")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comments(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=128)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("blog:post_list", kwargs={'pk': self.pk})

    def approve(self):
        self.approved_comment = True
        self.save()

