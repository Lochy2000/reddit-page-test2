from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category, Comment

# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            category=self.category
        )

    def test_post_list_view(self):
        client = Client()
        response = client.get(reverse('posts:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test Category')

    def test_post_detail_view(self):
        client = Client()
        response = client.get(reverse('posts:post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')

    def test_post_create_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.post(reverse('posts:post_create'), {
            'title': 'New Post',
            'content': 'This is a new post.',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_comment_create_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.post(reverse('posts:comment_create', args=[self.post.id]), {
            'content': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertTrue(Comment.objects.filter(content='This is a test comment.').exists())