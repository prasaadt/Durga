from django.urls import path
import homecare.views

urlpatterns = [
    path('hi', homecare.views.hi, name='hi'),
]