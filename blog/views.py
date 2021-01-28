from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import CommentForm
class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    success_url = reverse_lazy("blog")