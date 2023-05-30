from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from common.api.views import templateview, templateviews

app_name = "common"

router = DefaultRouter()
router.register('template', templateview)


urlpatterns = [
    path('html', templateviews),
    path('', include(router.urls)),
]
