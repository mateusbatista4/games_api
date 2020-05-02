from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$',
        ApiRoot.as_view(),
        name= ApiRoot.name
        ),
    url(r'^esrb-rating/$',
        EsrbRatingList.as_view(),
        name = EsrbRatingList.name
        ),
    url(r'^esrb-ratings/(P<pk>[0-9]+)/$',
        EsrbRatingDetail.as_view(),
        name= EsrbRatingDetail.name
        ),
    url(r'^games/$',
        GameList.as_view(),
        name= GameList.name
        ),
    url(r'^games/(P<pk>[0-9]+)/$',
        GameDetail.as_view(),
        name= GameDetail.name
        ),
    url(r'^players/$',
        PlayerList.as_view(),
        name = PlayerList.name
        ),
    url(r'^players/(P<pk>[0-9]+)/$',
        PlayerDetail.as_view(),
        name = PlayerDetail.name
        ),
    url(r'^player-scores/$',
        PlayerScoreList.as_view(),
        name= PlayerScoreList.name
        ),
    url(r'^player-scores/(P<pk>[0-9]+)/$',
        PlayerScoreDetail.as_view(),
        name= PlayerScoreDetail.name
        )

]



