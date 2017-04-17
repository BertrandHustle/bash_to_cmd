from django.contrib import admin
from .models import Bash_Command, Cmd_Command

# Register your models here.

admin.site.register(Bash_Command)
admin.site.register(Cmd_Command)
