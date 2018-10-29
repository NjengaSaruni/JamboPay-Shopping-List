from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ItemListCreateView.as_view(), name='create_item'),
    url(r'^(?P<pk>[^/]+)/$', views.ItemDetailView.as_view(), name='detail_item'),
]