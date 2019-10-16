from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    return render(request, 'articles/index.html', context)

def create(request):
    """
    Form Class
    1. 모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 데이터 정제 후
    DB에 실제 저장하는 로직 필요

    Model Form
    이미 Model에 대한 정보(스키마)를 알고 있기 때문에 어떤 모델에 넣어야 하는지 알고 있음.
    form.save()만 해도 DB에 저장됨
    """
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {'form': form, }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_forms = CommentForm()
    context = {'article': article, 'comment_forms': comment_forms, }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index') # redirect -> GET 요청
    return redirect('articles:detail', article.pk)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # instance -> 수정의 대상이 되는 특정한 글 객체
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # embed()
            return redirect('articles:detail', article.pk)
    else:
        # form = ArticleForm(initial={
        #     'title': article.title,
        #     'content': article.content,
        # })
        form = ArticleForm(instance=article)
        # embed()
    context = {'form': form, 'article': article, }
    return render(request, 'articles/form.html', context)


"""
Create 로직
1. GET
- 사용자가 데이터를 입력 할 수 있는 빈 Form을 제공
2. POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1. GET
- 기존 사용자의 글이 입력된 Form 제공
2. POST
- 수정된 글을 DB에 저장
"""

def comments_create(request, article_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
    return redirect('articles:detail', article_pk)

def comments_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
    return redirect('articles:detail', article_pk)