from django.conf.urls import *

from photologue.views import GalleryListView

urlpatterns = [
    url(r'^gallerylist/gallerylist/$',
        GalleryListView.as_view(paginate_by=40),
        name='photologue_custom-gallery-list'),
]