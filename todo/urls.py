from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()
router.register(r'categories',views.CategoryViewSet,basename='category')
router.register(r'todos',views.ToDoViewSet,basename='todo')

urlpatterns=[
    path('',include(router.urls))
    # path('signup/',views.UserRegistrationView.as_view(),name='signup'),
]