from django.db import models

# Create your models here.

class Bash_Command(models.Model):
    # the literal name of the command
    bash_command = models.CharField(max_length=100)
    # corresponding cmd command
    cmd_translation = models.OneToOneField('Cmd_Command', null=True, blank=True)
    # what the command does
    purpose = models.CharField(max_length=200)
    # link to man page for command
    man_page_url = models.CharField(max_length=100)

    # this lets us get a string representation of the object rather than a bare object descriptor
    def __str__(self):
        return self.purpose

class Cmd_Command(models.Model):
    # the literal name of the command
    cmd_command = models.CharField(max_length=100)
    # corresponding bash command
    bash_translation = models.OneToOneField(Bash_Command, null=True, blank=True)
    # what the command does
    purpose = models.CharField(max_length=200)
    # link to man page for command
    man_page_url = models.CharField(max_length=100)

    def __str__(self):
        return self.purpose
