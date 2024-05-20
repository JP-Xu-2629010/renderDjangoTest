from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from tree01.models import UserCase

@csrf_exempt

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

    cases = UserCase.objects.all().order_by('id')  # 获取UserCase表中的所有记录
    #print(cases)
    return render(request, 'viewdb.html', {'cases': cases})
    #return HttpResponse('db成功')

def test(request):
    print("test running")
    return render(request, "test.html")


def caseCheck(request, case_id):
    case = get_object_or_404(UserCase, id=case_id)
    return render(request, 'caseCheck.html', {'case': case})

def checkUpload(request):
    if request.method == 'POST':
        selectedId = request.POST.get('case_id')
        tree_type = request.POST.get('new_tree_type')
        actual_quantity = request.POST.get('new_actual_quantity')
        location = request.POST.get('new_location')
        checked = request.POST.get('new_checked')

        user_case = UserCase.objects.get(id=selectedId)
        user_case.tree_type = tree_type
        user_case.actual_quantity = actual_quantity
        user_case.location = location
        user_case.checked = checked

        user_case.save()

        return HttpResponse(f'Submitted, id {selectedId}, quantity {actual_quantity}, location {location}, checked {checked}<br><a href="/viewdb/">return to  viewdb</a>')
    return HttpResponse('error: not POST')

def vxmlUpload(request):
    if request.method == 'POST':
        return HttpResponse('success')
    else:
        return HttpResponse('Method not allowed.')
        """ new_user_quantity = "0"
        new_tree_type = request.POST.get('treeType')
        new_record = request.FILES.get('record')

        UserCase.objects.create(
            tree_type=new_tree_type,  
            user_quantity=new_user_quantity,  
            actual_quantity=0,  
            location='unknown',  
            audio_file=new_record,  
            checked=0  
        ) """

        # return HttpResponse(f'Submitted, id {selectedId}, quantity {actual_quantity}, location {location}, checked {checked}',<br><a href="/viewdb/">return to  viewdb</a>)
        # return HttpResponse('success')
    # return HttpResponse('error: not POST')

def create088(request):
    UserCase.objects.create(
            tree_type=0,  
            user_quantity=0,  
            actual_quantity=0,  
            location='unknown',  
            audio_file=None,  
            checked=1  
        )
    return HttpResponse('created')
# def addCase(request):
