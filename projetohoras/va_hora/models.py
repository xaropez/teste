from django.db import models
from django.utils import timezone


# Create your models here.

class Va_hora (models.Model):
    name = models.CharField(max_length = 200)
    date = models.DateField()
    hours = models.TimeField()
    work_type = models.CharField(max_length = 200)
    customer = models.CharField(max_length = 200)
    customer_oportunity = models.CharField(max_length = 200)

    #Apenas para retornar o nome
    def __unicode__(self):
        return '/%s/' % self.name

    def get_absolute_url(self):
        return'/%s/' % self.id


    # Fomulario com setinha:

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )
    teste = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=' ',
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
