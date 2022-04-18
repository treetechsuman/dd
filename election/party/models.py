from django.db import models
ACTIVE = 'Active'
INACTIVE = 'Inactive'
    
STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    ]
# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=200)
    status =  models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACTIVE,
    )
    description = models.TextField(blank = True)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"
        ordering=['-created_at','-updated_at']
