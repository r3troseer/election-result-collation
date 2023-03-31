from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path("poll_result/", views.polling_unit_result, name="poll_result"),
    path("lga_results/", views.lga_results, name="lga_results"),
    path('add_polling_unit_result/', views.add_polling_unit_result, name='add_polling_unit_result'),
]
