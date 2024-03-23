from django.urls import path
from .views import CustomersList, CustomerDetail, CustomerCreate, CustomerUpdate, CustomerDelete

app_name = "customers"


urlpatterns = [
    path("", CustomersList.as_view(), name="customers-list"),
    path("detail/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
    path("create/", CustomerCreate.as_view(), name="customer-create"),
    path("update/<int:pk>/", CustomerUpdate.as_view(), name="customer-update"),
    path("delete/<int:pk>/", CustomerDelete.as_view(), name="customer-delete")
]
