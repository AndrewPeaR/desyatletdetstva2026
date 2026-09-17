from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import RegisterForm, FeedbackForm, checkCaptcha
# Create your views here.

def index(request):
    feedbackForm = FeedbackForm()
    registerForm = RegisterForm()

    if request.method == 'POST':
        # print('register_submit' in request.POST)
        if 'register_submit' in request.POST:
            form = RegisterForm(request.POST)
            # print(form)
            if form.is_valid():
                if checkCaptcha(request, 'register'):
                    register = form.save(commit=False)
                    register.save()
                    messages.success(request, 'Регистрация прошла успешно!')
                    return redirect('/')
                else:
                    messages.error(request, 'Проверка капчи не пройдена')
                    registerForm = form
            else:
                messages.error(request, 'Форма заполнена неверно')
                registerForm = form

        elif 'feedback_submit' in request.POST:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                if checkCaptcha(request, 'feedback'):
                    feedback = form.save(commit=False)
                    feedback.save()
                    messages.success(request, 'Сообщение отправлено!')
                    return redirect('/')
                else:
                    messages.error(request, 'Проверка капчи не пройдена')
                    feedbackForm = form
            else:
                messages.error(request, 'Форма заполнена неверно')
                feedbackForm = form

    
    context = {
        "feedbackForm": feedbackForm,
        "registerForm": registerForm
    }
    return render(request, 'main/index.html', context)