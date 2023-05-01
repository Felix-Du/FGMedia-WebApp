from rest_framework import serializers
from .models import Game
from .models import Combo

class gameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = ('gameTitle', 'release_date')
        
class ComboSerializer(serializers.ModelSerializer):

    class Meta:
        model = Combo 
        fields = ('pk', 'damage', 'comboNotation', 'meterCost', 'moonSkillCost', 'moonDrive', 'meterGain', 'location', 'notes', 'videoFile')