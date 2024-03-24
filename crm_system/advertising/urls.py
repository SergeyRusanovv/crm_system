from django.urls import path
from .views import AdsList, AdsDetail, AdsCreate, AdsUpdate, AdsDelete, Statistic

app_name = "advertising"


urlpatterns = [
    path("", AdsList.as_view(), name="ads-list"),
    path("detail/<int:pk>/", AdsDetail.as_view(), name="ads-detail"),
    path("create/", AdsCreate.as_view(), name="ads-create"),
    path("update/<int:pk>/", AdsUpdate.as_view(), name="ads-update"),
    path("delete/<int:pk>", AdsDelete.as_view(), name="ads-delete"),
    path("statistic/", Statistic.as_view(), name="statistic")
]
