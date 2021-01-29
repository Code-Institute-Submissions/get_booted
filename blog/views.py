from django.contrib.auth.models import User
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

class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'
    
    success_url = reverse_lazy("blog")

    def form_valid(self, form):
        post = Post.objects.filter(slug=self.kwargs['slug'])
        if self.request.user.pk:
            # Make sure authenticated user is owner
            form.instance.comment_owner = self.request.user
        else:
            # assuming user.username = admin is the superuser, they will be the owner of anonymous comments
            user = User.objects.get(username='admin')
            form.instance.comment_owner = user
        form.instance.post_id = post[0].id
        return super().form_valid(form)

    success_url = reverse_lazy("blog")