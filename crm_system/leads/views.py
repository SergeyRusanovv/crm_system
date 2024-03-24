from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from .models import Leads
from .forms import LeadsForm


class LeadsList(UserPassesTestMixin, generic.ListView):
    """Просмотр потенциальных клиентов"""
    model = Leads
    template_name = "leads/leads-list.html"
    context_object_name = "leads"

    def test_func(self):
        return self.request.user.groups.filter(Q(name='operator') | Q(name='manager')).exists()


class LeadsDetail(UserPassesTestMixin, generic.DetailView):
    """Детальный просмотр потенциального клиента"""
    model = Leads
    template_name = "leads/leads-detail.html"
    context_object_name = "lead"

    def test_func(self):
        return self.request.user.groups.filter(name='operator').exists()


class LeadsCreate(UserPassesTestMixin, generic.CreateView):
    """Создание потенциального клиента"""
    model = Leads
    template_name = "leads/leads-create.html"
    form_class = LeadsForm

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user.groups.filter(name='operator').exists()


class LeadsUpdate(UserPassesTestMixin, generic.UpdateView):
    """Изменение потенциального клиента"""
    model = Leads
    template_name = "leads/leads-edit.html"
    form_class = LeadsForm
    context_object_name = "lead"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user.groups.filter(name='operator').exists()


class LeadsDelete(UserPassesTestMixin, generic.DeleteView):
    """Удаление потенциального клиента"""
    model = Leads
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:leads-list")
    context_object_name = "lead"

    def test_func(self):
        return self.request.user.groups.filter(name='operator').exists()
