from django.urls import path
from . import views

urlpatterns = [
    path('photos',views.photoList.as_view()),
    path('photos/<int:id>',views.photoView.as_view()),
    path('create/photos',views.photoCreate.as_view()),
    path('delete/photo/<int:id>',views.photoDestroy.as_view()),
]