from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article, Comment, Image


def index(request):
    articles = Article.objects.all()

    # articles_result = dict(articles)

    context = {
        'articles': articles,
        'text': 'BlaBLa',
        'items': [1, 2, 3, 4]
    }

    return render(request=request, template_name='articles/list.html', context=context)


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    print(article)
    context = {
        'article': article,
    }

    return render(request=request, template_name='articles/detail.html', context=context)


def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404('Comment not found')

    author_name = request.POST.get('author_name', '-')
    comment_text = request.POST.get('comment_text', '-')

    article.comments.create(
        author_name=author_name,
        comment_text=comment_text
    )

    return HttpResponseRedirect(reverse('detail_page', args=(article.id,)))


def image(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404('Image not found')

    image_article = request.POST.get('-')

    article.image.create(
         image_article=image_article
    )

    return HttpResponseRedirect(reverse('detail_page', args=(article.id,)))




