from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment
from .forms import CommentForm, EmailPostForm
# Create your views here.

def blogpost_detail(request, year, month, day, post):
    post = get_object_or_404(BlogPost, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comment.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)

            new_comment = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blogposts/blogpost_detail.html', {'post':post,
                                                              'comment_form':comment_form,
                                                              'comments':comments
                                                              })
