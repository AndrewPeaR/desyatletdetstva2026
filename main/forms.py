from dotenv import load_dotenv
load_dotenv()

from django import forms
from .models import Register, Feedback

import os
import sys
import json
import requests

class RegisterForm(forms.Form, forms.ModelForm):
    format_choices = [
        ('', 'Выберете элемент'),
        ('off', 'Очно'),
        ('onn', 'Заочно')
    ]

    category_choices = {
        "": "Выберете элемент",
        "youngfamily": "Молодая семья",
        "manyfamily": "Многодетная семья",
        "studyfamily": "Студенческая семья",
        "invalidfamily": "Семья, воспитывающая ребенка инвалида, ребенка с ограниченными возможностями здоровья",
        "zameshaushie": "Замещающая семья (опекуны, попечители, приемные родители и усыновители)",
        "kandidatzamesh": "Кандидаты в замещающие семьи (слушатели школы приемных родителей)",
        "regorganspred": "Представитель региональных и муниципальных органов государственной власти",
        "peoplepred": "Представитель общественной организации",
        "healthpred": "Представитель организации здравоохранения",
        "studypred": "Представитель образовательной организации",
        "socialpred": "Представитель организации социального обслуживания",
        "culturepred": "Представитель организации культуры",
        "sportpred": "Представитель организации физической культуры и спорта",
        "study": "Студент",
        "volonteer": "Волонтер",
        "another": "Другое",
    }

    cities_choises = {
        "": "Выберете элемент",
        "belraion": "Белоярский район",
        "berezraion": "Берёзовский район",
        "kondraion": "Кондинский район",
        "neftraion": "Нефтеюганский район",
        "nijneraion": "Нижневартовский район",
        "oktybrraion": "Октябрьский район",
        "sovetraion": "Советский район",
        "surgutraion": "Сургутский район",
        "khantyraion": "Ханты-Мансийский район",
        "kogalym": "Когалым",
        "langepas": "Лангепас",
        "megion": "Мегион",
        "neftegansk": "Нефтеюганск",
        "nijnevartovsk": "Нижневартовск",
        "nyagan": "Нягань",
        "pokachi": "Покачи",
        "pytyach": "Пыть-Ях",
        "radujnyi": "Радужный",
        "surgut": "Сургут",
        "yrai": "Урай",
        "khanty": "Ханты-Мансийск",
        "ugorsk": "Югорск",
    }

    placeOne_choises = {
        "": "Выберете элемент",
        "prozvet": "Проектная мастерская «Процветание»",
        "history": "Проектная мастерская «История»",
        "inklusion": "Проектная мастерская «Инклюзия»",
        "family": "Проектная мастерская  «Семья»",
        "mir": "Проектная мастерская «Мир»",
        "laboratory": "Проектная мастерская «Лаборатория»",
        "iniciativa": "Проектная мастерская «Инициатива»",
    }

    fio = forms.CharField(widget=forms.TextInput(attrs={"class":"register__input register__input_height", "id": "fio"}), label='', required=True)
    category = forms.ChoiceField(choices=category_choices, widget=forms.Select(attrs={"class": 'format-select__native', 'tabindex': '-1', 'aria-hidden': 'true', "id": 'category', "required": "required"}), label='', required=True)
    city = forms.ChoiceField(choices=cities_choises ,widget=forms.Select(attrs={"class": 'format-select__native', 'tabindex': '-1', 'aria-hidden': 'true', "id": 'city', "required": "required"}), label='', required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"register__input register__input_height", "id": "phone"}), label='', required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"register__input register__input_height", "id": "email"}), label='', required=True)
    place = forms.ChoiceField(choices=placeOne_choises ,widget=forms.Select(attrs={"class": 'format-select__native', 'tabindex': '-1', 'aria-hidden': 'true', "id": 'place', "required": "required"}), label='', required=True)
    format = forms.ChoiceField(choices=format_choices, widget=forms.Select(attrs={"class": 'format-select__native', 'tabindex': '-1', 'aria-hidden': 'true', "required": "required"}), label='', required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"register__input", 'rows': 5, "id": "message"}), label='', required=True)
    policy = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"register__checkbox-input", 'id': 'register__input-policy'}), label='', required=True)

    class Meta:
        model = Register
        fields = ('fio', 'category', 'phone', 'email', 'city', 'place', 'format', 'message', 'policy')


class FeedbackForm(forms.Form, forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"footer__input", 'id': 'name'}), label='', required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"footer__input", 'id': 'email'}), label='', required=True)
    policy = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"footer__checkbox-input", 'id': 'footer__input-policy'}), label='', required=True)

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'policy')

# Запрос на проверку введеной капчи
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def checkCaptcha(request, type):
    match type:
        case 'register':
            secret=os.getenv('SMARTCAPTCHA_SERVER_KEY_REGISTER')
        case 'feedback':
            secret=os.getenv('SMARTCAPTCHA_SERVER_KEY_FEEDBACK')
    
    resp = requests.post(
       "https://smartcaptcha.yandexcloud.net/validate",
       data={           
          "secret": secret,
          "token": request.POST.get("smart-token"),
          "ip": get_client_ip(request)
       },
       timeout=1
    )
    
    server_output = resp.content.decode()
    if resp.status_code != 200:
       print(f"Allow access due to an error: code={resp.status_code}; message={server_output}", file=sys.stderr)
       return True
    return json.loads(server_output)["status"] == "ok"