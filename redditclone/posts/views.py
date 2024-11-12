from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.db.models import Count
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Post, Category, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()

# Top post
    
    #top_posts = Post.objects.annotate(
    #    vote_score=models.Count('upvotes') - models.Count('downvotes')
    #).order_by('-vote_score')[:3]

    #top_posts = sorted (
    #   Post.objects.all (),
    #  key=lambda post: post.vote_score,
    # reverse=True
    #)[:3]

    #all_posts = Post.objects.all()
    #print("Number of total Posts:", all_posts.count())

    #top_posts = []
    #for post in all_posts:
        #upvotes = post.upvotes.count()
        #downvotes = post.downvotes.count()
        #score = upvotes - downvotes
        #print(f"Post  '{post.title}' has score: {score} (upvotes: {upvotes}, downvotes: {downvotes})")
        #top_posts.append(post)

    #top_posts = sorted(top_posts, key =lambda x:x.vote_score, reverse=True)[3]
    #print("Top posts after sorting:", [(post.title, post.vote_score) for post in top_posts])

    top_posts = Post.objects.annotate(
        total_score=Count('upvotes') - Count('downvotes')
    ).order_by('-total_score')[:5]

    return render(request, 'posts/post_list.html', {
        'posts': posts,
        'categories': categories,
        'top_posts': top_posts
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(parent=None)  # Get only top-level comments
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': post.comments.filter(parent=None)
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        print("FILES in request:", request.FILES)
        title = request.POST['title']
        content = request.POST['content']
        category_id = request.POST['category']
        image = request.FILES.get('image') #added images to post

          # Check if image is being received
        print(f"Image received: {image}")

        if not all([title, content, category_id]):
            messages.error(request, "Please fill in all fields.")
            return redirect("posts:post_create")

        try: 
            category = Category.objects.get(id=category_id)
            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user,
                category_id=category_id,
                image=image
            )

            # Debug message
            print(f"Post created with image: {post.image}")
            print(f"Post image path:{post.image.path if post.image else 'no image'}")

            messages.success(request,"Post created successfully!")
            return redirect('posts:post_detail', post_id=post.id)
        except Exception as e:  # Catch any errors
            print(f"Error creating post: {str(e)}")  # Debug print
            messages.error(request, f"Error creating post: {str(e)}")
            return redirect('posts:post_create')

    categories = Category.objects.all()
    return render(request, 'posts/post_form.html', {'categories': categories})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    #check that user is the author
    if request.user != post.author:
        messages.error(request, "You can't edit this post.")
        return redirect ("posts:post_detail", post_id=post.id)

    if request.method == 'POST':
        title = request.POST.get['title']
        content = request.POST.get['content']
        category_id = request.POST.get['category']
        image = request.FIELS.get['image']

        if not all ([title, content, category_id]):
            messages.error(request, "Please fill all fields.")
        else:
            try:
                category = Category.objects.get(id=category_id)
                post.title = title
                post.content = content
                post.category = category
                if image:
                    post.image = image
                post.save()
                messages.success(request, "Post update successfully!")
                return redirect("post:post_detail", post_id=post.id)
            except Category.DoesNotExist:
                messages.error(request,"Invalid category selected")

    categories = Category.objects.all()
    return render(request, 'posts/post_form.html', {
        'post': post,
        'categories': categories
    })

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        messages.error(request, "You cannot delete this post.")
        return redirect("posts:post_detais", post_id=post.id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request,"Post deleted successfully!")
        return redirect('posts:post_list')
    
    return render(request, "posts/post_confirm_delete.html", {"post": post})

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

