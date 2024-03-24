from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import ActiveLead


class CustomersList(UserPassesTestMixin, generic.ListView):
    """Просмотр активных клиентов"""
    model = ActiveLead
    template_name = "customers/customers-list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        customers = ActiveLead.objects.select_related("lead", "contract").all()
        data["customers"] = customers
        return data

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


class CustomerDetail(UserPassesTestMixin, generic.DetailView):
    """Детальный просмотр активного клиента"""
    model = ActiveLead
    template_name = "customers/customers-detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        customer = ActiveLead.objects.select_related("lead", "contract").get(pk=self.object.pk)
        data["customer"] = customer
        return data

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


class CustomerCreate(generic.CreateView):
    """Создание активного клиента"""
    model = ActiveLead
    fields = "__all__"
    context_object_name = "customer"
    template_name = "customers/customers-create.html"

    def get_success_url(self):
        return self.object.get_absolute_url()


class CustomerUpdate(generic.UpdateView):
    """Изменение активного клиента"""
    model = ActiveLead
    fields = "__all__"
    context_object_name = "customer"
    template_name = "customers/customers-edit.html"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


class CustomerDelete(generic.DeleteView):
    """Удаление активного клиента"""
    model = ActiveLead
    template_name = "customers/customers-delete.html"
    context_object_name = "customer"
    success_url = reverse_lazy("customers:customers-list")
