from django.db import models

# Create your models here.
class Drug(models.Model):
    name1 = models.CharField(max_length=50, null= True, blank=True)
    name2 = models.CharField(max_length=500, null= True, blank=True)
    description = models.TextField()
    indication = models.TextField()
    effect_on_dental_tissues = models.TextField()
    effect_on_patient_treatment = models.TextField()
    drug_interaction = models.TextField()

    def __str__(self):
        return self.name1
    class Meta:
        ordering = ['name1']


class Drug2(models.Model):
    name1 = models.CharField(max_length=50, null= True, blank=True)
    name2 = models.CharField(max_length=500, null= True, blank=True)
    description = models.TextField()
    indication = models.TextField()
    Presentations = models.TextField()
    Dose = models.TextField()
    Contraindications = models.TextField()
    Precautions = models.TextField()
    Unwanted_effects = models.TextField()
    drug_interaction = models.TextField()
    def __str__(self):
        return self.name1
    class Meta:
        ordering = ['name1']



class Drug3(models.Model):
    name1 = models.CharField(max_length=50, null= True, blank=True)
    name2 = models.CharField(max_length=500, null= True, blank=True)
    description = models.TextField()
    indication = models.TextField()
    Presentations = models.TextField()
    Dose = models.TextField()
    Contraindications = models.TextField()
    Unwanted_effects = models.TextField()
    drug_interaction = models.TextField()
    def __str__(self):
        return self.name1
    class Meta:
        ordering = ['name1']



