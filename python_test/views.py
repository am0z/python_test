from django.db.models import Q
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Client


class ClientListView(ListView):

    model = Client
    query = None
    ordering = "name"
    ordering_list = [
        "name",
        "-name",
        "email",
        "-email",
        "phone_number",
        "-phone_number",
        "suburb",
        "-suburb",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query
        return context

    def get_ordering(self):
        self.ordering = self.request.GET.get("ordering", self.ordering)
        return self.ordering

    def get_queryset(self):
        self.query = self.request.GET.get("query", "")
        queryset = super().get_queryset()
        if self.query:
            queryset = queryset.filter(
                Q(name__icontains=self.query)
                | Q(email__icontains=self.query)
                | Q(phone_number__icontains=self.query)
                | Q(suburb__icontains=self.query)
            )
        return queryset


class ClientCreateView(CreateView):

    model = Client
    fields = "__all__"
    success_url = reverse_lazy("list")


class ClientUpdateView(UpdateView):

    model = Client
    fields = "__all__"
    success_url = reverse_lazy("list")
