from django.conf.urls import url
from .views import game_detail,game_collection


urlpatterns = [
    url(r'games/$',game_collection),
    url(r'^games/(?P<id>[0-9]+)/$', game_detail),
]



