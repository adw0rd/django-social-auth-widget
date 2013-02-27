from django import template
from django.conf import settings


def social_auth_widget(context):
    return {
        'providers': settings.SOCIAL_AUTH_PROVIDERS,
    }

register = template.Library()
register.inclusion_tag('auth/social_auth_widget.html', takes_context=True)(social_auth_widget)
