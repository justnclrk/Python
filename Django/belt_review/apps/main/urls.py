from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^$', views.index),
    url(r'^books$', views.books),
    url(r'^books/add$', views.bookadd),
    url(r'^books/create_book$', views.create_book),
    url(r'^books/(?P<book_id>\d+)$', views.review_create),
    url(r'^users/(?P<user_id>\d+)$', views.users),
    url(r'^logout$', views.log_out),
]