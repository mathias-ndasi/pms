# from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views import generic

from drug.models import Drugs
from core.models import Pharmacy


class ProductSearchListView(LoginRequiredMixin, generic.ListView):
    template_name = 'search/view.html'
    context_object_name = 'drugs'

    def get_context_data(self, **kwargs):
        context = super(ProductSearchListView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['pharmacy'] = Pharmacy.objects.filter(name=self.request.user.pharmacyuser.works_at)[0]
        context['pharmacy_drugs'] = Drugs.objects.filter(pharmacy=self.request.user.pharmacyuser.works_at)
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')

        if query is not None:
            return Drugs.objects.search(query)
        return Drugs.objects.none()
