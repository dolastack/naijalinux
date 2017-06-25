from django.shortcuts import render, get_object_or_404

# Create your views here.

def blogpost_detail(request, year, month, day, post):
    post = get_object_or_404(post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blogposts/blogpost_detail.html', {'post':post})
