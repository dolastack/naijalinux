from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.views.decorators.cache import cache_page
from django.conf import settings
from openprojects.models import OpenSourceProject


# Create your views here.
def index(request):
    display_list = Article.objects.articles_after(days=20)
    project_list = OpenSourceProject.objects.all()

    #context = {'rows':display_list}
    template = "feeds/feeds_list.html"

    paginator = Paginator(display_list, 10)
    page = request.GET.get('page')
    try:
         rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)
    except EmptyPage:
        rows = paginator.page(paginator.num_pages)

    context = {'rows' : rows, 'project_list':project_list}
    return render(request, template, context )
