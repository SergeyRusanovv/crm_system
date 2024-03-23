from django.urls import reverse_lazy
from django.views import generic
from .models import Contract


class ContractList(generic.ListView):
    template_name = "contracts/contracts-list.html"
    model = Contract
    context_object_name = "contracts"


class ContractDetail(generic.DetailView):
    template_name = "contracts/contracts-detail.html"
    model = Contract

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        contract = Contract.objects.select_related("product").get(pk=self.object.pk)
        data["contract"] = contract
        return data


class ContractCreate(generic.CreateView):
    template_name = "contracts/contracts-create.html"
    model = Contract
    fields = "__all__"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ContractUpdate(generic.UpdateView):
    template_name = "contracts/contracts-edit.html"
    model = Contract
    fields = "__all__"
    context_object_name = "contract"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ContractDelete(generic.DeleteView):
    template_name = "contracts/contracts-delete.html"
    model = Contract
    context_object_name = "contract"
    success_url = reverse_lazy("contracts:contracts-list")
