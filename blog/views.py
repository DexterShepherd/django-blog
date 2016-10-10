from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.utils import timezone
from blog.models import Blog, Category
from .forms import PostForm, CategoryForm

# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

#post crud TODO rename Blog model to Post
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('view_blog_post', slug=post.slug)
    form = PostForm()
    return render(request, 'post_form.html', { 'form': form })

def edit_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.published_date = timezone.now()
            post.save()
            return redirect('view_blog_post', slug=post.slug)
    form = PostForm(instance=post)
    return render(request, 'post_form.html', { 'form': form })


def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render_to_response('view_post.html', {
        'post': post,
        'category': post.category
    })

def destroy_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    if post.delete()[0]:
        return redirect('blog_index')

#category crud
def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('view_blog_category', slug=category.slug)
    form = CategoryForm()
    return render(request, 'category_form.html', { 'form': form })
    

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def edit_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category.save()
            return redirect('view_blog_category', slug=category.slug)
    form = CategoryForm(instance=category)
    return render(request, 'category_form.html', { 'form': form })

def destroy_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if category.delete()[0]:
        return redirect('blog_index')

