from django.urls import path

from MenuIngredientManagement.views import home_view

urlpatterns = [
    path('home/', home_view),
]