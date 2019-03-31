from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views

from festivals import views


router = DefaultRouter()
router.register(r'^artists', views.ArtistViewSet, 'artist')
router.register(r'^festivals', views.FestivalViewSet, 'festival')
router.register(r'^shows', views.ShowViewSet, 'show')
router.register(r'^participations', views.ParticipationViewSet, 'participation')
router.register(r'^attendances', views.AttendanceViewSet, 'attendance')
router.register(r'^parties', views.PartyViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', auth_views.obtain_auth_token)
]