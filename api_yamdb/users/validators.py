from api_yamdb.settings import DENY_LIST
from django.core.exceptions import ValidationError


def validate_username(value):
    if value in DENY_LIST:
        raise ValidationError(
            f'Имя пользователя не может быть{DENY_LIST}',
            params={'value': value},
        )
