from django.conf import settings

ALWAYS_UPDATE_USER = getattr(settings, 'AUTH_CROWD_UPDATE_USER', True)
MIRROR_GROUPS = getattr(settings, 'AUTH_CROWD_MIRROR_GROUPS', True)
STAFF_GROUP = getattr(settings, 'AUTH_CROWD_STAFF_GROUP', 'staff')
SUPERUSER_GROUP = getattr(settings, 'AUTH_CROWD_SUPERUSER_GROUP', 'superusers')
APPLICATION_USER = getattr(settings, 'AUTH_CROWD_APPLICATION_USER', 'django')
APPLICATION_PASSWORD = getattr(settings, 'AUTH_CROWD_APPLICATION_PASSWORD', 'django')
SERVER_URI = getattr(settings, 'AUTH_CROWD_SERVER_URI', 'http://127.0.0.1:8095/crowd/services/SecurityServer?wsdl')