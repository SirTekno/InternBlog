from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request, page = 0):
    results_per_page = 12
    next_page = False
    prev_page = False

    #posts = Post.objects.order_by('-date')[page * results_per_page: (page+1 * results_per_page) + 1]
    posts = Post.objects.order_by('-date')

    if results_per_page == 13:
        next_page = True
    if page > 0:
        prev_page = True

    return render(request, "posts/_overview.html", {"prev": prev_page, "next": next_page, "posts": posts, "authenticated": request.user.is_authenticated()})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if not request.user.is_authenticated() and not post.published:
        return redirect("/")

    return render(request, "posts/_individual_post.html", {"post": post})

# Todo
def rss(request):
    pass
