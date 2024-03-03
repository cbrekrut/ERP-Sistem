from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request,'erp/index.html',{})

def customers(request):
    user = request.user
    return render(request,'erp/erpCustomers.html',{'user': user})

def profile(request):
    user = request.user
    return render(request,'erp/erp_director.html',{'user': user})

@csrf_exempt
def save_task(request, user_id):
    if request.method == 'POST' or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print(request.POST)
        email = request.POST.get('email')
        user = CustomUser.objects.get(email=email)
        task_description = request.POST.get('task_description')
        print(task_description)
        if task_description:
            task = Task.objects.create(description=task_description, assigned_to=user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Task description is required'})
    else:
        print('failed to')
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def erp(request):
    user = request.user  # Получаем текущего пользователя
    if user.role =='worker':
        tasks = Task.objects.filter(assigned_to=user,created_at__date=datetime.now().date())
        return render(request, 'erp/erp_worker.html', {'user': user, 'tasks':tasks})
    else:
        return render(request, 'erp/erp_analytics.html', {'user': user})
    
def director_erp(request, email):
    now_user = request.user
    user = CustomUser.objects.get(email=email)
    tasks = Task.objects.filter(assigned_to=user, created_at__date=datetime.now().date())
    return render(request, 'erp/erp_worker.html', {'user': user, 'tasks': tasks, 'now_user': now_user})




@csrf_exempt
@require_POST
def change_task_status(request):
    task_id = request.POST.get('task_id')
    new_status = request.POST.get('new_status')

    task = get_object_or_404(Task, id=task_id)
    task.status = new_status
    task.created_at = datetime.now()
    task.save()

    return JsonResponse({'status': 'success'})
