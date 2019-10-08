from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article, Comment
from IPython import embed

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = { 'articles': articles }
    return render(request, 'articles/index.html', context)

def create(request):
    # POST 요청일 때
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    # GET 요청일 때
    else:
        return render(request, 'articles/create.html')

    '''
    title = request.POST.get('title')
    content = request.POST.get('content')

    #1. 첫 번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2. 두 번째 방법
    article = Article(title=title, content=content)
    article.save()

    #3. 세 번째 방법
    # Article.objects.create(title=title, content=content)

    return redirect(f'/articles/{ article.pk }')
    '''


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article, }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    if request.method == 'POST':
        Article.objects.get(pk=article_pk).delete()
    return redirect('articles:index')

    # article = Article.objects.get(pk=pk)
    # article.delete()

    # return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
        }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article': article,
            }
        return render(request, 'articles/update.html', context)

def comments_create(request, article_pk): # pk는 pk번 째 글을 의미함
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # article.comments.article = article
        # article.comments.content = request.POST.get('content')
        content = request.POST.get('content')
        comment = Comment(article=article, content=content)
        comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)