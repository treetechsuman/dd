import re
from django.db import models
ACTIVE = 'Active'
INACTIVE = 'Inactive'
    
STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    ]
# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=200)
    status =  models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACTIVE,
    )
    coordinate = models.TextField(blank = True)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ##db_table = "dynamicform_dform"
        verbose_name = "Province"
        verbose_name_plural = "Provinces"
        ordering=['-created_at','-updated_at']

class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE,related_name='districts')
    name = models.CharField(max_length=200)  
    status=  models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACTIVE,
    )
    coordinate = models.TextField(blank = True)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['display_order']
    def __str__(self):
        return self.name
class Municipality(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE,related_name='municipalities')
    name = models.CharField(max_length=200)  
    status=  models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACTIVE,
    )
    coordinate = models.TextField(blank = True)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['display_order']
    def __str__(self):
        return self.name

class Ward(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    ward_number = models.IntegerField() 
    status=  models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACTIVE,
    )
    coordinate = models.TextField(blank = True)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['display_order']
    