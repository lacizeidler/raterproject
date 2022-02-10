from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from raterprojectapi.views import register_user, login_user
from raterprojectapi.views.category import CategoryView
from raterprojectapi.views.game import GameView
from raterprojectapi.views.review import ReviewView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'reviews', ReviewView, 'review')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login', login_user),
    path('register', register_user),
]
