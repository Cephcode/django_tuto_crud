from django.db import models

# Create your models here.


class singhor(models.Model):
    autheur = models.CharField(max_length=250)
    photo_autheur = models.ImageField(upload_to="images",)
    age_autheur = models.IntegerField(default=0, null=True)
    singhor = models.CharField(max_length=200)

    def __str__(self):
        return self.autheur
