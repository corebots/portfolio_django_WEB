from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from photologue_custom.models import GalleryExtended
from photologue.models import *
from .models import Contact
from django.views.generic import TemplateView

# Create your views here.


# def index(request):
#     return render(request, 'index.html')

# passing photologue model to index too
def index(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'index.html', context)


def design(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'design.html', context)


def amanita_brand(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'amanita_brand.html', context)


def amanita_app(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'amanita_app.html', context)


def printerest_web(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'printerest_web.html', context)


def tls_3d_video(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'tls_3d_video.html', context)


def tls_flyers_posts(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'tls_flyers_posts.html', context)


def t_shirts(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 't_shirts.html', context)


def posters(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'posters.html', context)


def tls_ci(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'tls_ci.html', context)


def about(request):
    photos = Photo.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'photos': photos,
        'galleries': galleries,
        }
    return render(request, 'about.html', context)


def photologue(request):
    return render(request, 'photologue/gallery_list.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email') # DO SOMETHING
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'thanks.html')
    else:
        return render(request, 'contact.html')









# class TagIndexView(ListView):
#     template_name = 'photologue/gallery_list.html'
#     model = GalleryExtended
#     paginate_by = '3'
#     context_object_name = 'tags'
#
#     def get_queryset(self):
#         return GalleryExtended.objects.filter(tags__slug=self.kwargs.get('slug'))



# def show_object(request):
#     """ View all objects """
#     return render(request,
#         template_name="photologue/gallery_list.html",
#         context={
#             'objects':GalleryExtended.tags.all(),
#         })


class TagListView(ListView):
    """The listing for tagged books."""
    template_name = "photologue/list.html"

    def get_queryset(self):
        return GalleryExtended.objects.filter(tags__slug=self.kwargs.get("slug")).all()

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("slug")
        return context


def gal_tagged(request, id):
    """The detail view for one book."""
    gal = get_object_or_404(GalleryExtended, id=id)

    # List of similar books
    tags = gal.tags.all()
    similar_gals = gal.objects.filter(
        tags__in=tags
    ).exclude(
        id=gal.id
    ).distinct()

    return render(request,
                  "photologue/gallery_tagged.html",
                  {"gal": gal,
                   "similar_books": similar_gals})