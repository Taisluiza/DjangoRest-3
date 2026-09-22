import re
from django.core.exceptions import ValidationError

def cpf_invalido(value):
    if not re.match(r'^\d{11}$', value):
        raise ValidationError("CPF inválido. Deve conter 11 dígitos.")

def nome_invalido(value):
    if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', value):
        raise ValidationError("Nome inválido. Use apenas letras e espaços.")

def celular_invalido(value):
    if not re.match(r'^\d{11}$', value):
        raise ValidationError("Celular inválido. Deve conter 11 dígitos.")
