from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.views.decorators.cache import cache_page
from django.conf import settings
from openprojects.models import OpenSourceProject
from blogposts.models import BlogPost
from clips.models import YoutubeVideo

# Create your views here.
def about(request):
    return render(request, 'about.html', {} )
    
def index(request):
    display_list = Article.objects.articles_after(days=20)
    project_list = OpenSourceProject.objects.all()
    blogposts = BlogPost.objects.all()
    videos = YoutubeVideo.objects.videos_after( days=60)


    template = "feeds/feeds_list.html"

    paginator = Paginator(display_list, 10)
    page = request.GET.get('page')
    try:
         rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)
    except EmptyPage:
        rows = paginator.page(paginator.num_pages)

    context = {'rows' : rows, 'project_list':project_list ,
               'blogposts':blogposts, 'videos' : videos}
    return render(request, template, context )
