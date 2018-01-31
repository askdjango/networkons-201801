from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    x = 100
    y = 200
    return render(request, 'blog/post_list.html', {
        'x': x,
        'y': y,
    })


def mysum(request, numbers):
    # numbers  # '123/456/789/123/456'

    # style #1
    # result = 0
    # for number in numbers.split('/'):  # ['123', '456', '789', '123', '456']
    #     if number:
    #         result += int(number)  # result = result + int(number)

    # style #2
    # result = 0
    # for number in numbers.split('/'):
    #     result += int(number or 0)

    # style #3: list comprehension
    numbers = [
        int(number or 0)
        for number in numbers.split('/')]
    result = sum(numbers)

    # return HttpResponse(result)

    return render(request, 'blog/mysum.html', {
        'numbers': numbers,
        'result': result,
    })


def hello(request, name, age):
    return render(request, 'blog/hello.html', {
        'name': name,
        'age': age,
    })

