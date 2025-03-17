from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Thread, Post
from .forms import ThreadForm, CategoryForm, PostForm


# Create your views here.
def forum(request):
    categories = Category.objects.all()
    threads = Thread.objects.all()

    template = 'forum/forum.html'
    context = {
        'categories': categories,
        'threads': threads,
    }

    return render(request, template, context)


@login_required
def create_thread(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.category = category
            thread.created_by = request.user
            thread.save()
            return redirect('forum')
        else:
            form = ThreadForm()
        return render(request, 'forum/create_thread.html', {
            'form': form,
            'category': category
        })


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
    else:
        form = CategoryForm()

    template = 'forum/add_category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def post_list(request, category_id, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    posts = Post.objects.filter(thread=thread)

    template = 'forum/post_list.html'
    context = {
        'thread': thread,
        'posts': posts
    }
    return render(request, template, context)


@login_required
def create_post(request, category_id, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            return redirect('post_list', category_id=category_id, thread_id=thread_id)
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form, 'thread': thread})
