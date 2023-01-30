import logging

from django.contrib import messages
# from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
# from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from posts.forms import (
    PostForm,
    ImageForm,
    VideoForm
)
from posts.models import (
    Post,
    ContactInformation,
    Image,
    Video,
    UserfulLinks,
    AboutUs,
)


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'posts/index.html')


def post_list(request):
    posts = Post.objects.order_by('-pub_date')

    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    context = {
        'post': post,
        'post_images': post.get_post_images(),
        'post_video': post.get_post_video(),
    }
    return render(request, 'posts/post_detail.html', context)


def useful_links(request):
    links = UserfulLinks.objects.all()

    context = {
        'links': links,
    }
    return render(request, 'posts/useful_links.html', context)


def get_contact_info_inst(request):
    info = ContactInformation.objects.all()

    context = {
        'info': info,
    }
    return render(request, 'posts/contact_info.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('posts:index'))
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        files = request.FILES.getlist("image")

        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            if files:
                for file in files:
                    Image.objects.create(image=file, post=post)
            if request.POST['video']:
                Video.objects.create(video=request.POST['video'], post=post)

            messages.success(request, 'Пост создан')
        return HttpResponseRedirect(reverse('posts:post_list'))

    else:
        form = PostForm()
        image_form = ImageForm()
        video_form = VideoForm()

    return render(request, "posts/create_post.html", {
        'form': form,
        'image_form': image_form,
        'video_form': video_form,
        }
    )


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('posts:index'))
def post_update_view(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    image_instance_set = post.get_post_images()
    video_instance = post.get_post_video()

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        files = request.FILES.getlist("image")

        if post_form.is_valid:
            post_form.save()

            if files:
                if image_instance_set.exists():
                    image_instance_set.delete()

                for file in files:
                    Image.objects.create(image=file, post=post)

            if request.POST['video']:
                Video.objects.create(video=request.POST['video'], post=post)

                if video_instance:
                    video_instance.delete()

            if not request.POST['video'] and video_instance:
                video_instance.delete()

            messages.success(request, 'Пост изменен')
        return HttpResponseRedirect(reverse('posts:post_detail', args=[post.id]))

    else:
        post_form = PostForm(instance=post)

        # image_formset = modelformset_factory(Image, fields=('image', ))
        # image_forms = image_formset(request.POST, image_instance_set)
        # image_forms = []
        # for i, image in enumerate(post.get_post_images()):
        #     image_forms.append(ImageForm(prefix=str(i), instance=image))
        image_forms = ImageForm()
        video_form = VideoForm(instance=video_instance)

    return render(request, "posts/post_update_form.html", {
        'form': post_form,
        'image_forms': image_forms,
        'video_form': video_form,
        }
    )


def about_us_view(request):
    about_us_obj = get_object_or_404(AboutUs)
    return render(request, 'about/about_us.html', {'about_us': about_us_obj})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')
    success_message = 'Пост удалён.'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('posts:index')))
    def post(self, request, *args, **kwargs):
        super().post(self, request, *args, **kwargs)

