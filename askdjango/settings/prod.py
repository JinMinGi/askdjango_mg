from .common import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'statc')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'defaults' = {
        'ENGINE':'django.db.backends.mysql',
        'HOST':'mingijin.mysql.pythonanywhere-services.com',
        'NAME':'mingijin$default'
        'USER':'mingijin'
        'PASSWORD':'atkdla930@A'
        'OPTIONS':{
            'sql_mode':'traditional',
        },
    },
}