from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import os


class FileUpload(models.Model):
    file = models.FileField(null=False, blank=False, default='')
    filename = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    file_fk = models.ForeignKey(User, default=1)


@receiver(models.signals.post_delete, sender=FileUpload)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
