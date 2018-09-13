from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^', views.ShoppingListListCreateView.as_view(), name='create_shopping_list'),
]