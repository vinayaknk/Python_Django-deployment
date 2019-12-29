from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView, DeleteView,DetailView,UpdateView
from . models import Post,Comments
from . forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # return Post.objects.all()
        return Post.objects.filter(published_date__lte=timezone.now())

class AboutView(TemplateView):
    template_name = 'about.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    form_class = PostForm

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    redirect_field_name = 'blog/post_list.html'
    login_url = '/login/'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    login_url = '/login/'

class DraftListView(LoginRequiredMixin,ListView):
    template_name = 'blog/post_draft_list.html'
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm()

    return render(request,'blog/comments_form.html',{'form' : form})

@login_required
def comment_approve(req,pk):
    comment = get_object_or_404(Comments, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)

@login_required
def comment_remove(req,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', pk=post_pk)

# class CommentCreateView(CreateView):
#     model = Comments
#     form_class = CommentForm
#     redirect_field_name = 'blog/post_detail.html'
#
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     post = Post.objects.get(self.pk)
    #     form.instance.post = post
    #     return super().form_valid(form)
    #
    # def form_valid(self, form):
    #     comment=form.save(commit=False)
    #     comment.post=self.kwargs.get(self.pk)
    #     comment.save()
    #     super().form_valid(form)




