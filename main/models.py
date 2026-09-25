from django.db import models

# Create your models here.

class Register (models.Model):
    CHOISES = {
        "off": "Очно",
        "onn": "Заочно"
    }

    CATEGORIES = {
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

    CITIES = {
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

    PLACE_ONE = {
        "prozvet": "Лаборатория «Здоровье семьи – здоровье нации»",
        "history": "Лаборатория «Социальная безопасность семьи и детства»",
        "inklusion": "Лаборатория «Развитие родительских компетенций»",
    }

    fio = models.CharField(max_length=250, verbose_name="ФИО")
    category = models.CharField(max_length=15, choices=CATEGORIES, verbose_name='Категория участника')
    city = models.CharField(max_length=15, choices=CITIES, verbose_name='Муниципальное образование')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Email')
    place = models.CharField(max_length=20, choices=PLACE_ONE, verbose_name='Площадка, которую хотите посетить')
    format = models.CharField(max_length=3, choices=CHOISES, verbose_name='Формат участия')
    message = models.TextField(verbose_name='Доп. информация для организаторов', null=True, blank=True)
    policy = models.BooleanField(default=False, verbose_name='Согласие на обработку')

    class Meta:
        verbose_name_plural = "Регистрационные заявки"
        verbose_name = "Регистрация"

    def __str__(self):
        return self.fio

class Feedback (models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.CharField(max_length=110, verbose_name="Электронная почта")
    message = models.TextField(verbose_name='Текст сообщения')
    policy = models.BooleanField(default=False, verbose_name='Согласие на обработку')

    class Meta:
        verbose_name_plural = "Обратная связь"
        verbose_name = "Ответ"

    def __str__(self):
        return self.name