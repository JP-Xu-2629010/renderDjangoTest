from django.shortcuts import render
from django.http import HttpResponse
from tree01.models import UserCase

# Create your views here.
def vxml(request):
    print(request.method)
    return HttpResponse('成功')

def viewdb(request):

    if not UserCase.objects.exists():
        # 如果为空，则创建一个新的UserCase实例
        UserCase.objects.create(
            tree_type=0,  
            user_quantity=0,  
            actual_quantity=0,  
            location='unknown',  
            audio_file=None,  
            checked=1  
        )

    cases = UserCase.objects.all()  # 获取UserCase表中的所有记录
    #print(cases)
    return render(request, 'viewdb.html', {'cases': cases})
    #return HttpResponse('db成功')

def test(request):
    print("test running")
    return render(request, "test.html")

# def addCase(request):
