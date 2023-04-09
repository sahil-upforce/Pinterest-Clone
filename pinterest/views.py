from django.views import generic

from pinterest.forms import PinCreateModelForm
from pinterest.models import Pin


class PinCreateView(generic.CreateView):
    model = Pin
    form_class = PinCreateModelForm
    template_name = 'pinterest/create_pin.html'
    success_url = '/'