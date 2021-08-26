from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('<int:id>/', views.get_measurement, name='measurementRetrieval'),
    path('delete/<int:id>/', views.delete_measurement, name='measurementDeletion'),
    path('update/<int:id>/<str:value>/<str:unit>/<str:place>/', views.update_measurement, name='measurementUpdate')
]
