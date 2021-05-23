from django.contrib import admin
from .models import Cosplay, General, SkinGeneral, AbilityGeneral, IntroduceGeneral

admin.site.register(SkinGeneral)
admin.site.register(General)
admin.site.register(AbilityGeneral)
admin.site.register(IntroduceGeneral)
admin.site.register(Cosplay)



# Register your models here.
