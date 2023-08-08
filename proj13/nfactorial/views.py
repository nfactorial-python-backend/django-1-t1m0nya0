from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, nfactorial school!")


def sum_two_integers(request, first: int, second: int) -> int:
    result_add_two_numbers = first + second
    return HttpResponse(f"result_add_two_numbers: {result_add_two_numbers}")


def transform_text_to_uppercase(request, text: str) -> str:
    transformed_text = text.upper()
    return HttpResponse(f"transformed_text: {transformed_text}")


def palindrome_check(request, word: str) -> str:
    cleaned_word = word.lower().replace(" ", "")  # Удаление пробелов и перевод в нижний регистр
    is_palindrome = cleaned_word == cleaned_word[::-1]
    return HttpResponse(f"word_is_palindrome: {is_palindrome}")


def calculate_numbers(request,first: int, operation: str, second: int) -> [int, float]:
    # operation_list = ['add', 'sub', 'mult', 'div']
    calculated_result = 0
    match operation:
        case 'add':
            calculated_result = first + second
        case 'sub':
            calculated_result = first - second
        case 'mult':
            calculated_result = first * second
        case 'div':
            calculated_result = first / second

    return HttpResponse(f"calculated_result: {calculated_result}")
