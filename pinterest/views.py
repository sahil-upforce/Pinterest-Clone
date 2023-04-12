from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import never_cache

from pinterest.forms import PinCreateModelForm
from pinterest.models import Pin


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class PinCreateView(generic.CreateView):
    model = Pin
    form_class = PinCreateModelForm
    template_name = 'pinterest/create_pin.html'
    success_url = '/'

    def get_form(self, form_class=None):
        form = super(PinCreateView, self).get_form(form_class)
        form.instance.user = self.request.user
        if self.kwargs.get('input_value') == 'idea_pin':
            form.instance.is_idea = True
        return form


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class PinDetailView(generic.DetailView):
    model = Pin
    template_name = 'pinterest/detail_pin.html'
    slug_url_kwarg = 'id'
    slug_field = 'id'
    context_object_name = 'pin_obj'

    def get_context_data(self, **kwargs):
        context = super(PinDetailView, self).get_context_data(**kwargs)
        context['suggested_pins'] = self.model.objects.filter(
            category__name__in=list(context['pin_obj'].category.values_list('name', flat=True))
        ).distinct().exclude(id=context['pin_obj'].id)
        return context
