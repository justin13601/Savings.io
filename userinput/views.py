from django.shortcuts import render
from .scripts.budget_planner import *
from .scripts.investment_portfolio import *

# Create your views here.
def first(request):
    return render(request,'userinput/prompt.html')

def home(request):
    dict = prompt(request)
    name = dict['name']
    city = dict['city']
    income = dict['income']
    house = dict['house']
    food = dict['food']
    major = dict['major']

    lis = calculate_budget(city, income, house, food)

    lis2 = return_results(investment_portfolio(major))[:5]

    context = {
        'list': lis,
        'listtwo': lis2,
        'lifestyle': round(lis[0], 2),
        'housing': round(lis[1], 2),
        'food': round(lis[2], 2),
        'remaining_funds': round(lis[3], 2),
        'emergency_funds': round(lis[4], 2),
        'name': name
    }

    return render(request, 'home.html', context)

def prompt(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    city = request.POST.get('city')
    income = request.POST.get('income')
    income = int(income)
    q1 = request.POST.get('q1')
    support = request.POST.get('support')
    familiar = request.POST.get('likert1')
    major = request.POST.get('major')
    house = request.POST.get('house')
    food = request.POST.get('likert2')

    print(name)
    print(age)
    print(city)
    print(type(income))
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