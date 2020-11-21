from django.urls import path
from . views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from api import views
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    # path('login/', LoginView.as_view()),
    path('user/', UserView.as_view(), name="all-users"),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
