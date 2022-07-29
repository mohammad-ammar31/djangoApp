from django.shortcuts import render, HttpResponse
from .models import Food
#from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_food(request):
    foods =Food.objects.all()
    context = {
        'foods': foods
    }
    print(context)
    return render(request, 'all_food.html', context)


def add_food(request):
    if request.method == 'POST':
        foodName = request.POST['foodName']
        foodType = request.POST['foodType']
        pinCode = int(request.POST['pinCode'])
        new_food = Food(foodName= foodName, foodType=foodType, pinCode=pinCode)
        new_food.save()
        return HttpResponse('Food added Successfully')
    elif request.method=='GET':
        return render(request, 'add_food.html')
    else:
        return HttpResponse("An Exception Occured! Food Has Not Been Added")


def remove_food(request, food_id = 0):
    if food_id:
        try:
            food_to_be_removed = Food.objects.get(id=food_id)
            food_to_be_removed.delete()
            return HttpResponse("Food Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Food ID")
    foods = Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'remove_food.html',context)


def filter_food(request):
    if request.method == 'POST':
        pin = int(request.POST['pinCode'])
        foods = Food.objects.all()
        if pin:
            foods = foods.filter(pinCode__icontains = pin)

        context = {
            'foods': foods
        }
        return render(request, 'all_food.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_food.html')
    else:
        return HttpResponse('An Exception Occurred')