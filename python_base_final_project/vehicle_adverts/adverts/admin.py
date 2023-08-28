from django.contrib import admin


from adverts.models import (Advert,
                            Vehicle,
                            Category,
                            VehicleModel,
                            ModelYear,
                            )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
                    "name",
                    "description",
                    )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
                    "name",

                    )


@admin.register(VehicleModel)
class ModelAdmin(admin.ModelAdmin):
    list_display = (
                    "name",
                    "vehicle",
    )


@admin.register(ModelYear)
class ModelAdmin(admin.ModelAdmin):
    list_display = (
                    "year",
                    "model",
    )


@admin.register(Advert)
class AdvertsAdmin(admin.ModelAdmin):
    list_display = (
                    "name",
                    "category",
                    "photo",
                    "price",
                    "engine_volume",
                    "engine_type",
                    "transmission",
                    "author",
                    "condition",
                    "status",
                    "created_at",
                    "updated_at",
                    )
