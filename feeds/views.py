from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    display_list = Article.objects.articles_after(days=20)
    context = {'rows':display_list}
    template = "feeds/feeds_list.html"
    return render(request, template, context )
