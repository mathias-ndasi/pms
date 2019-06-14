from django.urls import path
from search import views


app_name = 'search'

urlpatterns = [
    path('', views.DrugSearchListView.as_view(), name="list"),
    # path('pharmacist_list', views.PharmacistSearchListView.as_view(), name="pharmacist_list"),
]
