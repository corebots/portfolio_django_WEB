from django.urls import path, re_path
from portfolio.views import TagListView
from . import views # from top folder import views + settings for media trying

urlpatterns = [
    path('', views.index, name='home'),
    path("photologue/", views.photologue, name='photologue'),
    path('design/', views.design, name='design'),
    path('design/amanita_brand/', views.amanita_brand, name='amanita_brand'),
    path('design/amanita_app/', views.amanita_app, name='amanita_app'),
    path('design/printerest_web/', views.printerest_web, name='printerest_web'),
    path('design/tls_3d_video/', views.tls_3d_video, name='tls_3d_video'),
    path('design/tls_flyers_posts/', views.tls_flyers_posts, name='tls_flyers_posts'),
    path('design/tls_ci/', views.tls_ci, name='tls_ci'),
    path('design/t_shirts/', views.t_shirts, name='t_shirts'),
    path('design/posters/', views.posters, name='posters'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path("tags/", views.show_object, name='tags'),
    re_path(r'^tagged/(?P<slug>[-\w]+)/$', TagListView.as_view(), name="tagged_galleries"),
    # re_path(r'^tag/(?P<slug>[-\w]+)/$', views.TagIndexView.as_view(), name='tagged'),
]