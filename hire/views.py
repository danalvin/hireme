from django.shortcuts import render
from .models import Event
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.utils.decorators import method_decorator
from  .forms import CreateEventForm
from django.views.generic import ListView, DetailView, CreateView



# Create your views here.


class HomeView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'events'

    def get_queryset(self):
        """
        docstring
        """
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context


class EventListView(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'
    paginate_by = 5


class EventDetailsView(DetailView):
    model = Event
    template_name = 'details.html'
    context_object_name = 'event'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(EventDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Event doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # raise error
            raise Http404("Event doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class EventCreateView(CreateView):
    template_name = 'create.html'
    form_class = CreateEventForm
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('hire:home')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
