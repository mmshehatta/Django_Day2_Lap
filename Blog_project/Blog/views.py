from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm #import it to use here 
from django.http import HttpResponseRedirect


# Create your views here.
# ******************* Index function *******
def index(request):
    allArticles =  Article.objects.order_by('-posted_at').all()
    return  render(request , 'index.html' , context={
        'articles' :allArticles
    })


# ******************* Create Article function *******
def create_article(request):
    if request.method == "POST":
         form = ArticleForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('index')
         return render (request  , 'form.html' , context={
            "form" : form
            })
    form = ArticleForm()
    return render (request  , 'form.html' , context={
        "form" : form
    })


# ******************* Delete Article function *******
def article_delete(request , id):
    # To delete it from an instance:
    instance = Article.objects.get(id=id)
    instance.delete()
    return redirect('index')

   
# ******************* Update Article function *******
def article_update(request , id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
         form = ArticleForm(request.POST , instance=article)
         if form.is_valid():
             form.save()
             return redirect('index')
         return render (request  , 'edit.html' , context={
            "ArticleForm" : form,
            "ArticleModel":Article.objects.get(id=id)
            })
    else:
        form = ArticleForm()
        return render (request  , 'edit.html' , context={
           "ArticleForm" : form,
            "ArticleModel":Article.objects.get(id=id)
        })