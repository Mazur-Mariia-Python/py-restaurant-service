from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import DishType, Ingredient, Specialization, Cook, Dish
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    num_dish_types = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_specializations = Specialization.objects.count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dish_types": num_dish_types,
        "num_ingredients": num_ingredients,
        "num_specializations": num_specializations,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_visits": num_visits + 1,

    }
    return render(request, "menu/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "menu/dish_type_list.html"
    paginate_by = 5


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "menu/dish_type_detail.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("menu:dish-type-list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    template_name = "menu/ingredient_list.html"
    context_object_name = "ingredient_list"
    paginate_by = 5


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient
    template_name = "menu/ingredient_detail.html"


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("menu:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("menu:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("menu:ingredient-list")


class SpecializationListView(LoginRequiredMixin, generic.ListView):
    model = Specialization
    template_name = "menu/specialization_list.html"
    context_object_name = "specialization_list"
    paginate_by = 2


class SpecializationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Specialization
    template_name = "menu/specialization_detail.html"


class SpecializationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Specialization
    fields = "__all__"
    success_url = reverse_lazy("menu:specialization-list")


class SpecializationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Specialization
    fields = "__all__"
    success_url = reverse_lazy("menu:specialization-list")


class SpecializationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Specialization
    success_url = reverse_lazy("menu:specialization-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "menu/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 2


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "menu/cook_detail.html"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("menu:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("menu:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("menu:cook-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "menu/dish_list.html"
    context_object_name = "dish_list"
    paginate_by = 2


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "menu/dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("menu:dish-list")
