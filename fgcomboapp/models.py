from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .formatChecker import ContentTypeRestrictedFileField

# Create your models here.


class Combo(models.Model):
    comboNotation = models.TextField("Combo Notation")
    damage = models.PositiveBigIntegerField(
        "Damage",
    )
    meterCost = models.PositiveBigIntegerField(
        "Meter Cost",
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )
    moonSkillCost = models.PositiveBigIntegerField(
        "Moon Skill Cost",
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    moonDrive = models.BooleanField("Moon Drive")
    meterGain = models.PositiveBigIntegerField(
        "Meter Gain",
        default=0,
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

    def _str_(self):
        return self.comboNotation
