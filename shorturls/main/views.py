from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

def index(request):
    # testUsers = TestUsers.objects.all()
    # myUsers = list(testUsers)
    # print(myUsers[1].name)
    return HttpResponse("<h2>Hello world!</h2>")