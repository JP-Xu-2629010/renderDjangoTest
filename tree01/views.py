from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vxml(request):
    print(request.method)
    return HttpResponse('成功')
