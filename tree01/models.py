from django.db import models
# from django.contrib.gis.db import models as gis_models

# Create your models here.
class UserCase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    tree_type = models.IntegerField(choices=[(i, str(i)) for i in range(9)])
    location = models.CharField(max_length=32)
    audio_file = models.FileField(upload_to='audio_files/')