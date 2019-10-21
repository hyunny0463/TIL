from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    article_form = ArticleForm()
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        article = article_form.save()
        return redirect('articles:detail', article.pk)
    context = {'article_form': article_form, }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    pass

def update(request, article_pk):
    pass

def delete(request, article_pk):
    pass

def comment_create(request, article_pk):
    pass

def comment_delete(request, article_pk, comment_pk):
    pass