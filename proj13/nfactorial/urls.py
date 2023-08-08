from django.urls import path

from .views import (index, sum_two_integers, transform_text_to_uppercase,
                    palindrome_check, calculate_numbers)

urlpatterns = [
    path('', index),
    path('calc/<int:first>/<str:operation>/<int:second>/', calculate_numbers),
    path('check/<str:word>/', palindrome_check),
    path('transform/<str:text>/', transform_text_to_uppercase),
    path('<int:first>/add/<int:second>/', sum_two_integers),

]
