from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from adverts.forms import AdvertForms, AdvertCreationForms
from adverts.models import Advert, VehicleModel, ModelYear


class AdvertListView(ListView):
    model = Advert
    template_name = "index.html"
    queryset = (
        Advert
        .objects
        .select_related("author")
        .filter(~Q(status=False))
        .all()
    )


class AdvertDetailsView(DetailView):
    model = Advert
    queryset = (Advert
                .objects
                .all()
                )


class AdvertCreateView(LoginRequiredMixin, CreateView):
    model = Advert
    form_class = AdvertCreationForms
    success_url = reverse_lazy("adverts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Advert
    form_class = AdvertCreationForms

    def get_success_url(self):
        return reverse("adverts:advert", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Advert.objects.filter(author=self.request.user)


class AdvertDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("adverts:user-adverts")
    queryset = (
        Advert
        .objects
        .all()
    )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = False
        self.object.save()
        return redirect(success_url)


class AdvertActivateView(LoginRequiredMixin, DeleteView):
        template_name = "adverts/advert_comfirm_activate.html"
        success_url = reverse_lazy("adverts:user-adverts")
        queryset = (
            Advert
            .objects
            .all()
        )

        def form_valid(self, form):
            success_url = self.get_success_url()
            self.object.status = True
            self.object.save()
            return redirect(success_url)

        def get_queryset(self):
            return Advert.objects.filter(author=self.request.user)


class UserAdvertView(ListView):
    model = Advert
    template_name = "adverts/user-adverts.html"

    queryset = (
        Advert
        .objects
        .all()
    )

    def get_queryset(self):
        return Advert.objects.filter(author=self.request.user)


def load_models(request):
        vehicle_id = request.GET.get("vehicle")
        models = VehicleModel.objects.filter(vehicle_id=vehicle_id)
        return render(request, "adverts/model_options.html", {"models": models})


def load_years(request):
    model_id = request.GET.get("model")
    years = ModelYear.objects.filter(model_id=model_id)
    return render(request, "adverts/year_options.html", {"years": years})













