from django.urls import path
from . import views

urlpatterns = [
    # 이 부분을 채울 겁니다!
    # URL과 그 URL이 들어올 떄 어떻게 처리할지 명시해 주면 됩니다.
    path('', views.index),
]