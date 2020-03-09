from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^create/$', views.article_create, name="create"),
    url(r'^$', views.article_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]