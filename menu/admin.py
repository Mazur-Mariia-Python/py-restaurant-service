from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from menu.models import DishType, Dish, Ingredient, Cook, Specialization


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["ingredient_name", ]
    list_filter = ["ingredient_name", ]
    search_fields = ["ingredient_name", ]


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["dish_type_name", ]
    list_filter = ["dish_type_name", ]
    search_fields = ["dish_type_name", ]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["specialization_name", ]
    list_filter = ["specialization_name", ]
    search_fields = ["specialization_name", ]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", "specialization", )
    list_filter = UserAdmin.list_filter + ("years_of_experience", "specialization", )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience", "specialization", )}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                        "specialization",

                    )
                },
            ),
        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["dish_name", "get_ingredients", "description", "price", "dish_type", ]
    list_filter = ["dish_name", "price", "dish_type", "cooks", ]
    search_fields = ["dish_name", ]

    @admin.display(description="ingredients")
    def get_ingredients(self, obj):
        return ", ".join(
            [
                ingredient.ingredient_name
                for ingredient in obj.ingredients.all()
            ]
        )
