from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from api.user.views.general_views import UserViewSet
from api.user.authentication import ObtainPairCustomView,LogoutView

urlpatterns = [
    path('login/', ObtainPairCustomView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',UserViewSet.as_view({'get':'list','post':'create'}), name='users')
]
