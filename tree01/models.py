from django.db import models
# from django.contrib.gis.db import models as gis_models

# Create your models here.
class UserCase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    tree_type = models.IntegerField(choices=[(i, str(i)) for i in range(6)])
    user_quantity = models.IntegerField(choices=[(i, str(i)) for i in range(2)])
    actual_quantity = models.IntegerField()
    location = models.CharField(max_length=32)
    audio_file = models.FileField(upload_to='audio_files/')
    checked = models.IntegerField(choices=[(i, str(i)) for i in range(4)])
    # 0 not, 1 invalid, 2 checked, 3 other