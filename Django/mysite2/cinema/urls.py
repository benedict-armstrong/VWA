from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /cinema
    url(r'^$', views.index, name='index'),
    # ex: /cinema/5/
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /cinema/screening/5/
    url(r'^screening/(?P<screening_id>[0-9]+)/$',
        views.screening,
        name='screening'),
]