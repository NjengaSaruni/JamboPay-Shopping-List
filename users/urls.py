from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^', views.UserList.as_view(), name='list_users'),
    url(r'^(?P<pk>[^/]+)/$', views.UserDetail.as_view(), name='detail_user'),
]