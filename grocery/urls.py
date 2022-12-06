from django.urls import path
import grocery.views

urlpatterns = [
    path('afternoon', grocery.views.afternoon, name='noon'),
    path('wish',grocery.views.wish,name='wish')
]