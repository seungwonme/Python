from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def a(request):
    return render(request, "main/a.html")


def b(request):
    return render(request, "main/b.html")


def c(request):
    return render(request, "main/c.html")


def seunan(request):
    return render(request, "main/seunan.html")


def orm(request):
    return render(request, "main/orm.html")
