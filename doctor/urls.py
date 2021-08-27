from django.urls import path

from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('', views.NutritionView.as_view(), name="index"),
    path('nutrition/', views.NutritionView.as_view(), name="nutrition"),
]
