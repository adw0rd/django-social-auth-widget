from django import template
from django.conf import settings


def social_auth_widget():
    return {
        'providers': settings.SOCIAL_AUTH_PROVIDERS,
    }

register = template.Library()
register.inclusion_tag('social_auth_widget.html')(social_auth_widget)
