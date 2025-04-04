from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Thread, Post
from .forms import ThreadForm, CategoryForm, PostForm


# Create your views here.
def forum(request):
    categories = Category.objects.all()
    threads = Thread.objects.filter(is_deleted=False)

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
            return redirect(
                'post_list', category_id=category_id, thread_id=thread_id)
    else:
        form = PostForm()
    return render(
        request, 'forum/create_post.html', {'form': form, 'thread': thread})


@login_required
def edit_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)

    if request.user != thread.created_by:
        messages.error(request, 'You are not authorized to edit this thread.')
        return redirect('forum')

    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thread updated successfully!')
            next_url = request.POST.get('next', '')
            if next_url:
                return redirect(next_url)
            return redirect(
                'post_list',
                category_id=thread.category.id, thread_id=thread.id)
    else:
        form = ThreadForm(instance=thread)

    template = 'forum/edit_thread.html'
    context = {
        'form': form,
        'thread': thread,
        'next': request.GET.get('next', '')
    }
    return render(request, template, context)


@login_required
def delete_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)

    if request.user != thread.created_by:
        messages.error(
            request,
            'You are not authorized to delete this thread.')
        return redirect('forum')

    thread.is_deleted = True
    thread.save()
    messages.success(request, 'Thread deleted successfully!')
    return redirect('forum')


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.created_by:
        messages.error(request, 'You are not authorized to edit this post.')
        return redirect('forum')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            next_url = request.POST.get('next', 'profile')
            return redirect(next_url)
    else:
        form = PostForm(instance=post)

    template = 'forum/edit_post.html'
    context = {
        'form': form,
        'post': post,
        'next': request.GET.get('next', 'profile')
    }
    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.created_by:
        messages.error(request, 'You are not authorized to delete this post.')
        return redirect('profile')

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        next_url = request.POST.get('next', 'profile')
        return redirect(next_url)
    else:
        return redirect('profile')
