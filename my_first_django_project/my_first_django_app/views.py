from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import Portfolio, Teams


def index(request):
    # to fetch all the datas from the table
    obj = Portfolio.objects.all()
    obj_1 = Teams.objects.all()
    results = {
        'result': obj,
        'result_2': obj_1
    }
    return render(request,'index.html',results)
