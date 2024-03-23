from django.urls import path
from .views import ContractList, ContractDetail, ContractCreate, ContractUpdate, ContractDelete

app_name = "contracts"


urlpatterns = [
    path("", ContractList.as_view(), name="contracts-list"),
    path("detail/<int:pk>/", ContractDetail.as_view(), name="contract-detail"),
    path("create/", ContractCreate.as_view(), name="contract-create"),
    path("update/<int:pk>/", ContractUpdate.as_view(), name="contract-update"),
    path("delete/<int:pk>/", ContractDelete.as_view(), name="contract-delete")
]
