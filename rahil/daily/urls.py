from django.urls import path
from . import views

urlpatterns = [
    path('list',views.dailyList.as_view()),
    path('create',views.dailyCreate.as_view()),
    path('delete/<int:id>',views.dailyDestroy.as_view()),
]
