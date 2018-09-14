from django.contrib import admin
from pkiproject import models
from .models import Profile
# Register your models here.

from .models import User

admin.site.register(models.Profile)