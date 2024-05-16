from django.shortcuts import render
from django.http import HttpResponse
from tree01.models import UserCase

# Create your views here.
def vxml(request):
    print(request.method)
    return HttpResponse('成功')

def viewdb(request):
    cases = UserCase.objects.all()  # 获取UserCase表中的所有记录
    #print(cases)
    return render(request, 'viewdb.html', {'cases': cases})
    #return HttpResponse('db成功')

def test(request):
    print("test running")
    return render(request, "test.html")
# def addCase(request):
