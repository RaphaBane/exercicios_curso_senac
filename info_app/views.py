from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

def welcome_view(request):
    response = {"message": "Welcome to the Personal Info API!"}
    return JsonResponse(response)

def goodbye_view(request):
    response = {"message": "Goodbye, see you next time"}
    return JsonResponse(response)

def time_view(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    response = {"time": current_time}
    return JsonResponse(response)

def greet_view(request):
    name = request.GET.get('name', 'Stranger')
    response = {"message": f"Hello, {name}!",}
    return JsonResponse(response)

def age_category_view(request):
    age_param = request.GET.get('age')

    if age_param is None:
        return JsonResponse({"error": "Missing 'age' parameter."})

    age = int(age_param)

    if 0 <= age <= 12:
        return JsonResponse({"category": "Child"})
    elif 13 <= age <= 17:
        return JsonResponse({"category": "Teenager"})
    elif 18 <= age <= 59:
        return JsonResponse({"category": "Adult"})
    elif age >= 60:
        return JsonResponse({"category": "Senior"})
    else:
        return JsonResponse({"error": "Invalid 'age' value."}, status=400)

def sum_view(request, num1, num2):
    try:
        n1 = int(num1)
        n2 = int(num2)
    except ValueError:
        return JsonResponse({"error": "Invalid input, please provide two integers."},)

    return JsonResponse({"sum": n1 + n2})