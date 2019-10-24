from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user.article_set.all(): 유저가 쓴 게시글을 전부 (1:N)
    # user.like_articles.all(): 유저가 좋아요를 누른 게시글들 전부 (M:N)
    # article.like_users.all() 게시글에 좋아요를 누른 유저 전부 (M:N)
    # article.user 게시글을 작성한 유저( 1:N)

    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return self.content