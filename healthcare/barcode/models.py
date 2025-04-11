from django.db import models

# Create your models here.
class ScannedBarcode(models.Model):
    scannedBarcode_id = models.AutoField(primary_key=True)
    scannedBy = models.CharField(max_length=40)
    medicineName = models.CharField(max_length=100)
    usedFor = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.scannedBy} {self.medicineName}'