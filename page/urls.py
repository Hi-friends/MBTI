from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^list', views.list, name='list'),
  url(r'^entire', views.entire_list, name='entire'),
  url(r'^same/', views.same_list, name='same'),
  url(r'^detail1', views.same_detail, name='same_detail'),
  url(r'^match', views.match_list, name='match'),
  url(r'^detail2', views.match_detail, name='match_detail'),
]
