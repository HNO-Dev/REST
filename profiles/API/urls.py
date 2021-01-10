from django.urls import path,include
from .views import HelloApiView,HelloViewset,UserProfileViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('viewset',HelloViewset,basename='viewset')
router.register('profile',UserProfileViewset)

urlpatterns = [
    path('hello/',HelloApiView.as_view()),
    path('',include(router.urls))
]
