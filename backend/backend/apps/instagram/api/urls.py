from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from instagram.api.views import InstauserViews

app_name = "instagram"

router = DefaultRouter()
router.register('insta', InstauserViews)


urlpatterns = [
    #path('html', templateviews),
    path('', include(router.urls)),
]
