django-social-auth-widget
============================

Add to settings::

    SOCIAL_AUTH_PROVIDERS = [
        {'id': p[0], 'name': p[1], 'position': {'width': p[2][0], 'height': p[2][1], }}
        for p in (
            ('github', u'Login via GitHub', (0, -70)),
            ('facebook', u'Login via Facebook', (0, 0)),
            ('twitter', u'Login via Twitter', (0, -35)),
        )
    ]

How to use::

    {% load social_auth_widget %}

    <form action="" method="post">
        <input name="username" />
        <input name="password" />
        <input type="submit" value="Sign in" />
        {% social_auth_widget %}
    </form>

See also:

* http://adw0rd.com/2013/django-social-auth/

