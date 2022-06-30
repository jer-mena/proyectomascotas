from datetime import timedelta
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
# los modelos son las tablas de nuestra base de datos.

#from Apps.usuario.models import Usuario