from django.urls import path
from . import views
from .views import RecipeList, RecipeDetail

urlpatterns = [
    #path('recipes/list', views.recipes_list),
    #path('recipe/1', views.recipe_1),
    #path('recipe/2', views.recipe_2),

    path('recipes/list', RecipeList.as_view(), name = 'recipes'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name = 'recipe')
]