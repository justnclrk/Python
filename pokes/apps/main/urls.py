from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^main$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^pokes$', views.pokes),
    url(r'^create_poke/(?P<user_id>\d+)$$', views.create),
    url(r'^logout$', views.logout),
]