from django.contrib import admin

# Register your models here.
from .models import Province
from .models import District
from .models import Municipality
from .models import Ward

admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Ward)