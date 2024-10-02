from django.urls import path, include
from . import views
from .ClassViews import FirstPageView

urlpatterns = [
    path('test', views.index, name="main"),
    path('', FirstPageView.as_view(), name="firstpage"),
    # path('login', views.logForm, name="logform"),
    # path('test', views.test, name="test"),
]