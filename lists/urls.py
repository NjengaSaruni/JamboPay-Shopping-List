from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^items/$', views.ShoppingItemListCreateView.as_view(), name='create_list_items'),
    url(r'^items/(?P<pk>[^/]+)/$', views.ShoppingItemDetailView.as_view(), name='detail_list_items'),
    url(r'^$', views.ShoppingListListCreateView.as_view(), name='create_shopping_list'),
    url(r'^(?P<pk>[^/]+)/$', views.ShoppingListDetailView.as_view(), name='detail_shopping_list'),
]