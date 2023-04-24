from django.contrib import admin
from .models import Combo

class FGComboAppAdmin(admin.ModelAdmin):
    list_display = ('comboNotation', 'damage', 'meterCost', 'moonSkillCost', 'moonDrive', 'meterGain', 'location', 'notes', 'videoFile')

# Register your models here.

admin.site.register(Combo, FGComboAppAdmin)