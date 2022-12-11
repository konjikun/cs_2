from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
import random
from blog.models import Article

#cs概論の方
def index(request):
 if request.method == 'POST':
  article = Article(title=request.POST['title'], body=request.POST['text'])
  article.save()
  return redirect(detail, article.id)
 context = {
        "articles": Article.objects.all()
    }
 return render(request, 'blog/index.html', context)

def update(request, article_id):
 try:
  article = Article.objects.get(pk=article_id)
 except Article.DoesNotExist:
  raise Http404("Article does not exist")

 if request.method == 'POST':
  article.title = request.POST['title']
  article.body = request.POST['text']
  article.save()
  return redirect(detail, article_id)
 context = {
  "article": article
 }
 return render(request, "blog/edit.html", context)

def hello(request):
 fortune = random.randint(1,3)
 isGreatFortune = False
 fortuneMassage = ""

 if fortune == 1:
  fortuneMassage = "Great Fortune"
  isGreatFortune = True
 elif fortune == 2:
  fortuneMassage = "Small Fortune"
 else:
  fortuneMassage = "Bad fortune"

 data = {
  'name': 'Alice',
  'weather_detail': ['Temperature: 23°C', 'Humidity: 40%', 'Wind: 5m/s'],
  'isGreatFortune': isGreatFortune,
  'fortune': fortuneMassage
 }
 return render(request, 'blog/hello.html', data)

def redirect_test(request):
 return redirect(hello)

def detail(request, article_id):
 try:
  article = Article.objects.get(pk=article_id)
 except Article.DoesNotExist:
  raise Http404("Article does not exist")
 context = {
  "article": article
 }
 return render(request, "blog/detail.html", context)



def delete(request, article_id):
 try:
  article = Article.objects.get(pk=article_id)
 except Article.DoesNotExist:
  raise Http404("Article does not exist")
 article.delete()
 
 return redirect(index)