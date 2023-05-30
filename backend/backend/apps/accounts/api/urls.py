from django.urls import URLPattern, path, include
from accounts.api.views import user_registration_view, user_login_view, user_profile_view, logout_View, user_terms_accept
from rest_framework.routers import DefaultRouter




app_name = "account"

router = DefaultRouter()
router.register('profile', user_profile_view)


urlpatterns = [
    path('register', user_registration_view, name="register"),
    path('login', user_login_view, name="login"),
    path('logout', logout_View, name="logout"),
    path('terms', user_terms_accept, name="terms"),
    path('', include(router.urls)),
   
]
