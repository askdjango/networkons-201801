from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    x = 100
    y = 200
    return render(request, 'blog/post_list.html', {
        'x': x,
        'y': y,
    })


def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x) + int(y) + int(z))

