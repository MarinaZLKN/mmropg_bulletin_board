from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-datecreation'
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    '''def image_upload_view(request):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                return render(request, 'posts.html', {'form': form, 'img_obj': img_obj})
        else:
            form = PostForm()
        return render(request, 'posts.html', {'form': form})'''