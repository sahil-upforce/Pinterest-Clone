from django.urls import path

from pinterest.views import PinCreateView

app_name = 'pins'
urlpatterns = [
    path('pin/create/<str:input_value>', PinCreateView.as_view(), name='create_pin')
]
