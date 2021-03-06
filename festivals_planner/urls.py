from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Festivals API'
API_DESCRIPTION = 'An API for your favorite festivals.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^api/', include(('festivals.urls', 'api'), namespace='api')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]