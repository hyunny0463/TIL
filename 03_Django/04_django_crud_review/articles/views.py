from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = { 'articles': articles }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.full_clean()
    except ValidationError:
        raise ValidationError('Your Error Message')
    else:
        article.save()
        # return redirect(f'articles/{ article.pk }/')
        return redirect('articles:detail', article.pk)

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

    return redirect(f'/articles/{article.pk}')
    '''


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    # article = Article.objects.get(pk=pk)
    # article.delete()

    # return redirect('/articles/')
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
        }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    
    # return redirect(f'/articles/{article.pk}/')
    return redirect('articles:detail', article.pk)