from rest_framework import serializers
from .models import Combo

class ComboSerializer(serializers.ModelSerializer):

    class Meta:
        model = Combo 
        fields = ('pk', 'damage', 'comboNotation', 'meterCost', 'moonSkillCost', 'moonDrive', 'meterGain', 'location', 'notes', 'videoFile')
