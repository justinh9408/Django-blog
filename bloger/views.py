from django.shortcuts import render
from bloger.models import Article
from bloger.models import Tag
# Create your views here.

def indexpage(request,tagid):

    if tagid:
        art = Article.objects.filter(tag_id=tagid)
    else:
        art = Article.objects.all()

    return render(request, 'index.html',locals())

def articlepage(request, pageid):
    article = Article.objects.all().get(id=pageid)
    print(article.tag)
    return render(request, 'art_page.html',locals())

def artlist(request):
    art = Article.objects.all()
    return render(request, 'artlist.html',locals())

def taglist(request):
    taglist = Tag.objects.all()

    return render(request, 'taglist.html',locals())
