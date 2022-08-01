from django.contrib import admin
from .models import AddressSecret
from .models import GetMessage
from .models import PraiseTread

# Register your models here.
admin.site.register(AddressSecret)
admin.site.register(GetMessage)
admin.site.register(PraiseTread)