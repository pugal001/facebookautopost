from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from Facebook.api.views import Detailview

app_name = "facebook"

router = DefaultRouter()
router.register('Details', Detailview)


urlpatterns = [
    path('', include(router.urls)),
]
