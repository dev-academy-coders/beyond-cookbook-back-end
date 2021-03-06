"""beyond_cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from ingredients.views import ProductViewSet
from recipes.views import RecipeViewSet, RecipeIngredientsViewSet
from users.views import UserViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('recipe-ingredients', RecipeIngredientsViewSet, basename='recipe-ingredients')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
