from import_export import resources, fields
from .models import Register

class RegisterResource(resources.ModelResource):
    # Если нужно переименовать колонки в Excel/CSV — делай это через column_name
    fio = fields.Field(attribute='fio', column_name='ФИО')
    category = fields.Field(attribute='city', column_name='Категория')
    city = fields.Field(attribute='city', column_name='Город')
    city_other = fields.Field(attribute='city_other', column_name='Другой город')
    phone = fields.Field(attribute='phone', column_name='Телефон')
    email = fields.Field(attribute='email', column_name='Электронная почта')
    place = fields.Field(attribute='place', column_name='Место')
    format = fields.Field(attribute='format', column_name='Формат участия')
    message = fields.Field(attribute='message', column_name='Сообщение')
    policy = fields.Field(attribute='policy', column_name='Согласие с политикой')

    def dehydrate_place(self, obj):
        return obj.get_place_display()
    
    def dehydrate_category(self, obj):
        return obj.get_category_display()
    
    def dehydrate_city(self, obj):
        return obj.get_city_display()

    def dehydrate_format(self, obj):
        return obj.get_format_display()

    def dehydrate_policy(self, obj):
        return 'Да' if obj.policy else 'Нет'

    class Meta:
        model = Register
        # Порядок колонок при экспорте
        export_order = ('id', 'fio', 'category', 'city', 'city_other', 'phone', 'email', 'place', 'format', 'message', 'policy')
        # Можно явно указать, какие поля выгружать. Если не указать — выгрузятся все поля модели
        fields = ('id', 'fio', 'category', 'city', 'city_other', 'phone', 'email', 'place', 'format', 'message', 'policy')