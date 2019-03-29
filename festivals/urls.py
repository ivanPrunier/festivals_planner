from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from festivals import views


router = DefaultRouter()
router.register(r'^artists', views.ArtistViewSet, 'artist')
router.register(r'^festivals', views.FestivalViewSet, 'festival')
router.register(r'^shows', views.ShowViewSet, 'show')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^scrap', views.scrap),
]