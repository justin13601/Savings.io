from django.shortcuts import render
from .budget_planner import *

# Create your views here.
def first(request):
    return render(request,'userinput/prompt.html')

def home(request):
    dict = prompt(request)
    city = dict['city']
    income = dict['income']
    house = dict['house']
    food = dict['food']
    lis = calculate_budget(city, income, house, food)

    context = {
        'lifestyle': lis[0],
        'hosing': lis[1],
        'food': lis[2],
        'emergencyfunds': lis[3],
    }

    return render(request, 'home.html', context)

def prompt(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    city = request.POST.get('city')
    income = request.POST.get('income')
    q1 = request.POST.get('q1')
    support = request.POST.get('support')
    familiar = request.POST.get('likert1')
    major = request.POST.get('major')
    house = request.POST.get('house')
    food = request.POST.get('likert2')

    print(name)
    print(age)
    print(city)
    print(income)
    print(q1)
    print(support)
    print(familiar)
    print(major)
    print(house)
    print(food)

    context = {
        'name':name,
        'age': age,
        'city': city,
        'income': income,
        'q1': q1,
        'support': support,
        'familiar': familiar,
        'major': major,
        'house' : house,
        'food': food,
    }

    return context