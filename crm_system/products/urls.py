from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete


app_name = "products"


urlpatterns = [
    path("", ProductsList.as_view(), name="products"),
    path("detail/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("update/<int:pk>/", ProductUpdate.as_view(), name="product-update"),
    path("create/", ProductCreate.as_view(), name="product-create"),
    path("delete/<int:pk>/", ProductDelete.as_view(), name="product-delete")
]
