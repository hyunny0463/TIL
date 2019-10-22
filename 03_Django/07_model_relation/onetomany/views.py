from django.shortcuts import render

# 2. 1번 사람의 게시글별로 모든 댓글 출력
# for article in user1.article_set.all():
#     for comment in article.comment_set.all():
#         print(comment.content)

# 3. 2번 댓글을 쓴 사람은?
# c2.user.name

# 4. 2번 댓글을 쓴 사람의 모든 게시글?
# c2.user.article_set.all()

# 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
# article1.comment_set.first().user.name
# article1.comment_set.all()[0].user.name

# 6. 1번 글의 두번째부터 네번째까지 댓글을 가져오면?
# article1.comment_set.all()[1:4]

# 7. 1번 글의 첫번째 ~ 두번째 댓글을 가져오면?
# article1.comment_set.all()[:2]

# 8. 1번 글의 두번째 댓글을 쓴 사람의 첫번째 게시물의 작성자 이름
# article1.comment_set.all()[1].user.article_set.all()[0].user.name

# 9. 1번 댓글의 user 정보만 가져오면?(.values)
# Comment.objects.values('user').get(pk=1)

#10. 2번 사람이 작성한 댓글을 content를 기준으로 내림차순으로 가져오면?
# user2.comment_set.all().order_by('-content')
# user2.comment_set.order_by('-content')

#11. 제목이 '1글' 인 게시글은?
# Article.objects.all().filter(title='1글')
# Article.objects.filter(title='1글')