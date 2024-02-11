from django.urls import reverse_lazy
from django.views import generic
from .models import AdvertisingCompany
from .forms import AdsForm


class AdsList(generic.ListView):
    model = AdvertisingCompany
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdsDetail(generic.DetailView):
    model = AdvertisingCompany
    template_name = "ads/ads-detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        ads = AdvertisingCompany.objects.select_related("product").get(pk=self.object.pk)
        data["ads"] = ads
        return data


class AdsCreate(generic.CreateView):
    form_class = AdsForm
    model = AdvertisingCompany
    template_name = "ads/ads-create.html"

    def get_success_url(self):
        return self.object.get_absolute_url()


class AdsUpdate(generic.UpdateView):
    model = AdvertisingCompany
    form_class = AdsForm
    template_name = "ads/ads-edit.html"
    context_object_name = "ads"

    def get_success_url(self):
        return self.object.get_absolute_url()


class AdsDelete(generic.DeleteView):
    model = AdvertisingCompany
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("advertising:ads-list")
    context_object_name = "ads"
