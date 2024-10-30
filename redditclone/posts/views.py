from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'posts/post_list.html', {
        'posts': posts,
        'categories': categories
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(parent=None)  # Get only top-level comments
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category_id = request.POST['category']
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            category_id=category_id
        )
        return redirect('posts:post_detail', post_id=post.id)

    categories = Category.objects.all()
    return render(request, 'posts/post_form.html', {'categories': categories})

@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category_id = request.POST['category']
        post.save()
        return redirect('posts:post_detail', post_id=post.id)

    categories = Category.objects.all()
    return render(request, 'posts/post_form.html', {
        'post': post,
        'categories': categories
    })

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:post_list')

@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            author=request.user,
            content=content
        )
        return redirect('posts:post_detail', post_id=post.id)

@login_required
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
    return redirect('posts:post_detail', post_id=post_id)

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'posts/category_posts.html', {
        'category': category,
        'posts': posts
    })

@login_required
def category_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Category.objects.create(name=name, description=description)
        return redirect('posts:post_list')
    return render(request, 'posts/category_form.html')

@login_required
def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.description = request.POST['description']
        category.save()
        return redirect('posts:category_posts', category_id=category.id)
    return render(request, 'posts/category_form.html', {'category': category})

@login_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('posts:post_list')

@login_required
def post_upvote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.upvotes.add(request.user)
    post.downvotes.remove(request.user)
    return redirect('posts:post_detail', post_id=post.id)

@login_required
def post_downvote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.downvotes.add(request.user)
    post.upvotes.remove(request.user)
    return redirect('posts:post_detail', post_id=post.id)