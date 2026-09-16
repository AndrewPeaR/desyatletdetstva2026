from django.shortcuts import render
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
                else:
                    print("Robot")
            else:
                print('Register Form invalid')
                print(form.errors)

        elif 'feedback_submit' in request.POST:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                if checkCaptcha(request, 'feedback'):
                    feedback = form.save(commit=False)
                    feedback.save()
                else:
                    print("Robot")
            else:
                print('Feedback Form invalid')
    
    context = {
        "feedbackForm": feedbackForm,
        "registerForm": registerForm
    }
    return render(request, 'main/index.html', context)