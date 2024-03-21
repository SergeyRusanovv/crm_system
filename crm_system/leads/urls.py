from django.urls import path
from .views import LeadsList, LeadsDetail, LeadsCreate, LeadsUpdate, LeadsDelete


app_name = "leads"


urlpatterns = [
    path("", LeadsList.as_view(), name="leads-list"),
    path("detail/<int:pk>/", LeadsDetail.as_view(), name="lead-detail"),
    path("create/", LeadsCreate.as_view(), name="leads-create"),
    path("update/<int:pk>/", LeadsUpdate.as_view(), name="lead-update"),
    path("delete/<int:pk>/", LeadsDelete.as_view(), name="lead-delete"),
]
