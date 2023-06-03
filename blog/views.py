from django.shortcuts import render
from django.utils import timezone
from .models import Post

POST_MAX = 500

def post_list(request):
    # get data first
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # prepare data
    for p in posts: 
        max = POST_MAX
        l = p.text.__len__()
        if l > max: l = max
        p.text_short = p.text[0:l]

    return render(request, 'blog/post_list.html', {'posts': posts})