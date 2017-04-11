from django.db import models

# Create your models here.

class Bash_Command(models.Model):
    # the literal name of the command
    bash_command = models.CharField(max_length=100)
    # what the command does
    purpose = models.CharField(max_length=200)
    # link to man page for command
    man_page_url = models.CharField(max_length=100)

class Cmd_Command(models.Model):
    # the literal name of the command
    cmd_command = models.CharField(max_length=100)
    # corresponding bash command
    bash_command = models.OneToOneField()
    # what the command does
    purpose = models.CharField(max_length=200)
    # link to man page for command
    man_page_url = models.CharField(max_length=100)
