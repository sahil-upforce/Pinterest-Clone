from django.urls import path

from pinterest.views import PinCreateView

app_name = 'pins'
urlpatterns = [
    path('pin/create', PinCreateView.as_view(), name='create_pin')
]
