from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from rest_framework import viewsets
from crm.models import *
from crm.serializers import CustomerSerializer


class CustomerListView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    


class CustomerDetailView(DetailView):
    model = Customer


class CustomerUpdateView(UpdateView):
    model = Customer


class CustomerDeleteView(DeleteView):
    model = Customer


class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact


class ContactUpdateView(UpdateView):
    model = Contact


class ContactDeleteView(DeleteView):
    model = Contact


class LeadListView(ListView):
    model = Lead


class LeadDetailView(DetailView):
    model = Lead


class LeadUpdateView(UpdateView):
    model = Lead


class LeadDeleteView(DeleteView):
    model = Lead


class OpportunityListView(ListView):
    model = Opportunity


class OpportunityDetailView(DetailView):
    model = Opportunity


class OpportunityUpdateView(UpdateView):
    model = Opportunity


class OpportunityDeleteView(DeleteView):
    model = Opportunity

class ActivityListView(ListView):
    model = Activity


class ActivityDetailView(DetailView):
    model = Activity


class ActivityUpdateView(UpdateView):
    model = Activity


class ActivityDeleteView(DeleteView):
    model = Activity