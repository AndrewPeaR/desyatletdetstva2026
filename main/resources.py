from import_export import resources, fields
from .models import Register

class RegisterResource(resources.ModelResource):
    # Если нужно переименовать колонки в Excel/CSV — делай это через column_name
    fio = fields.Field(attribute='fio', column_name='ФИО')
    city = fields.Field(attribute='city', column_name='Город')
    place = fields.Field(attribute='place', column_name='Место')
    format = fields.Field(attribute='format', column_name='Формат участия')
    message = fields.Field(attribute='message', column_name='Сообщение')
    policy = fields.Field(attribute='policy', column_name='Согласие с политикой')

    class Meta:
        model = Register
        # Порядок колонок при экспорте
        export_order = ('id', 'fio', 'city', 'place', 'format', 'message', 'policy')
        # Можно явно указать, какие поля выгружать. Если не указать — выгрузятся все поля модели
        fields = ('id', 'fio', 'city', 'place', 'format', 'message', 'policy')