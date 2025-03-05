from django.urls import path
from .views import SensorReadingCreateView, SensorExceptionCreateView

urlpatterns = [
    path('reading/', SensorReadingCreateView.as_view(), name='sensor-create'),
    path('exception/', SensorExceptionCreateView.as_view(), name='sensor-exception-create'),
]