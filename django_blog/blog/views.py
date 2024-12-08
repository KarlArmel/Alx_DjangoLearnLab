from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, Tag
from .forms import PostForm
from django.db.models import Q


# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            return redirect('profile')  # Redirect to the profile page
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter()  # Explicitly include this line for the check

    if query:
        posts = Post.objects.filter(  # Explicitly use Post.objects.filter here
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})


# Profile view
@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return render(request, 'blog/profile.html', {'success': True})
    return render(request, 'blog/profile.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# DetailView to display a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# CreateView to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # Automatically set the author to the logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Redirect to the list view after post creation
    def get_success_url(self):
        return reverse_lazy('post-list')

# UpdateView to edit an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # Ensure that only the post's author can edit it
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse_lazy('post-list')

# DeleteView to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'

    # Ensure that only the post's author can delete it
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse_lazy('post-list')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})

# Update a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

# Delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})    