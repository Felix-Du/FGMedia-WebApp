from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .formatChecker import ContentTypeRestrictedFileField

# Create your models here.

class Game(models.Model):
    title = models.TextField("Game Title")
    release_date = models.DateField("Release Date", null=True,default=None)
    
    # Make sure to define __str__ when creating one-to-many relationships
    # admin will see object instead of a defined field
    def __str__(self):
        return self.title

#
class Combo(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, default=None)
    comboNotation = models.TextField("Combo Notation")
    damage = models.PositiveBigIntegerField(
        "Damage",
    )
    meterCost = models.PositiveBigIntegerField(
        "Meter Cost",
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )
    moonSkillCost = models.PositiveBigIntegerField(
        "Moon Skill Cost",
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    moonDrive = models.BooleanField("Moon Drive")
    meterGain = models.PositiveBigIntegerField(
        "Meter Gain",
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )
    ANYWHERE = "ANY"
    MIDSCREEN = "MID"
    CORNER = "COR"
    LOCATION_CHOICES = [
        (ANYWHERE, "Anywhere"),
        (MIDSCREEN, "Midscreen"),
        (CORNER, "Corner"),
    ]
    location = models.CharField(
        max_length = 3,
        choices = LOCATION_CHOICES,
        default=ANYWHERE
    )
    notes = models.TextField(
        "Notes",
        blank=True
    )
    videoFile = ContentTypeRestrictedFileField(
        "Video File",
        upload_to='uploads/',
        content_types=['video/mp4', ],
        max_upload_size=5242880,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.comboNotation
