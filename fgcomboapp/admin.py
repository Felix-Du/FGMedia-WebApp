from django.contrib import admin
from .models import Game
from .models import Combo

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date')

class ComboAdmin(admin.ModelAdmin):
    def game_title(self, obj):
        if obj.game:
            return obj.game.title
    game_title.title = "Game Title"
    list_display = ('game_title', 'comboNotation', 'damage', 'meterCost', 'moonSkillCost', 'moonDrive', 'meterGain', 'location', 'notes', 'videoFile')

# Register your models here.

admin.site.register(Game, GameAdmin)
admin.site.register(Combo, ComboAdmin)
