from django.contrib import admin

# Register your models here.
from endpoints.models import Endpoint

admin.site.register(Endpoint)