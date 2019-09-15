from django.shortcuts import render
from .models import Article, Profile


def show_articles(request):
    articles = Article.objects.defer('image', 'text').order_by('-id')
    context = {'articles': articles}
    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    article = Article.objects.get(pk=id)
    authorisation_data_user = request.user.is_authenticated
    if authorisation_data_user == True:
        subscription_data_user = Profile.objects.get(user_id=request.user).paid_subscription
    else:
        subscription_data_user = False

    context = {
        'article': article,
        'subscription_data_user': subscription_data_user
    }

    return render(
        request,
        'article.html',
        context
    )
