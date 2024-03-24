from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Count, Sum, Prefetch
from django.urls import reverse_lazy
from django.views import generic
from products.models import Product
from .models import AdvertisingCompany
from .forms import AdsForm


class AdsList(LoginRequiredMixin, generic.ListView):
    """Просмотр всех рекламных компаний"""
    model = AdvertisingCompany
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdsDetail(UserPassesTestMixin, generic.DetailView):
    """Детальный просмотр рекламной компании"""
    model = AdvertisingCompany
    template_name = "ads/ads-detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        ads = AdvertisingCompany.objects.select_related("product").get(pk=self.object.pk)
        data["ads"] = ads
        return data

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class AdsCreate(UserPassesTestMixin, generic.CreateView):
    """Создание рекламной компании"""
    form_class = AdsForm
    model = AdvertisingCompany
    template_name = "ads/ads-create.html"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class AdsUpdate(UserPassesTestMixin, generic.UpdateView):
    """Изменение рекламной компании"""
    model = AdvertisingCompany
    form_class = AdsForm
    template_name = "ads/ads-edit.html"
    context_object_name = "ads"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class AdsDelete(UserPassesTestMixin, generic.DeleteView):
    """Удаление рекламной компании"""
    model = AdvertisingCompany
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("advertising:ads-list")
    context_object_name = "ads"

    def test_func(self):
        return self.request.user.groups.filter(name="marketolog").exists()


class Statistic(generic.ListView):
    """"Статистики об успешности рекламных кампаний"""
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"

    def get_queryset(self):
        products = Product.objects.prefetch_related("contracts").all()
        queryset = AdvertisingCompany.objects.annotate(
            clients_count=Count('leads'),
            active_clients_count=Count('leads'),
            total_income=Sum('product__contracts__amount'),
            total_expenses=Sum('budget')
        ).prefetch_related(Prefetch("product", queryset=products))
        return queryset
