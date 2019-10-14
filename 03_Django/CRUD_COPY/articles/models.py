from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'제목: {self.title}, 내용: {self.content}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') # on_delete=models.CASCADE << 게시글이 삭제되면 댓글도 같이 사라지게 함 없으면 댓글만 떠다님
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        # return f'댓글: {self.content}'
        return f'<Article({self.article_id}): Comment({self.pk} - {self.content})>'