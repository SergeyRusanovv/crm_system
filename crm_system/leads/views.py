from django.urls import reverse_lazy
from django.views import generic
from .models import Leads
from .forms import LeadsForm


class LeadsList(generic.ListView):
    model = Leads
    template_name = "leads/leads-list.html"
    context_object_name = "leads"


class LeadsDetail(generic.DetailView):
    model = Leads
    template_name = "leads/leads-detail.html"
    context_object_name = "lead"


class LeadsCreate(generic.CreateView):
    model = Leads
    template_name = "leads/leads-create.html"
    form_class = LeadsForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class LeadsUpdate(generic.UpdateView):
    model = Leads
    template_name = "leads/leads-edit.html"
    form_class = LeadsForm
    context_object_name = "lead"

    def get_success_url(self):
        return self.object.get_absolute_url()


class LeadsDelete(generic.DeleteView):
    model = Leads
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:leads-list")
    context_object_name = "lead"
