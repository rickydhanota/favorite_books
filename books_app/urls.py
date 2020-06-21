from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_books', views.adding_a_book),
    path('<int:id>', views.display_book),
    path('editandsave/<int:id>', views.edit_and_save),
    path('delete/<int:id>', views.delete_book),
    path('favorite/<int:id>', views.favorite),
    path('unfavorite/<int:id>', views.unfavorite),
]