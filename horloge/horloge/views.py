from django.shortcuts import render
from datetime import datetime


def home(request):
    date = datetime.today()
    return render(request, "index.html", context={"date": date})
