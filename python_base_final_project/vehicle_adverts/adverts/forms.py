from django import forms
from .models import Advert, VehicleModel, Vehicle, ModelYear


class AdvertForms(forms.ModelForm):

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertCreationForms(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "vehicle" in self.data:
            vehicle_id = int(self.data.get("vehicle"))
            self.fields["model"].queruset = VehicleModel.objects.filter(vehicle_id=vehicle_id).order_by("name")

        elif self.instance.pk and self.instance.vehicle:
            self.fields["model"].queryset = self.instance.vehicle.model_set.order_by("name")

        if "model" in self.data:
            model_id = int(self.data.get("model"))
            self.fields["model_year"].queruset = ModelYear.objects.filter(model_id=model_id).order_by("year")

        elif self.instance.pk and self.instance.model:
            self.fields["model_year"].queryset = self.instance.model.year_set.order_by("year")

    class Meta:
        model = Advert
        fields = ("name",
                  "category",
                  "vehicle",
                  "model",
                  "model_year",
                  "photo",
                  "price",
                  "color",
                  "engine_volume",
                  "engine_type",
                  "transmission",
                  "condition",
                  "status",
                  )

