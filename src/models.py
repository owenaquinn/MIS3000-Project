from django.db import models

# Constant Models
class Days(models.Model):

    abbrev = models.CharField(max_length=1, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.text
 
# Create your models here.
class ClassList(models.Model):

    crn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    title = models.TextField()

    def __str__(self):
        return self.name

class Offerings(models.Model):

    crn = models.ForeignKey(ClassList, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
    
class OfferingDays(models.Model):

    offeringID = models.ForeignKey(Offerings, on_delete=models.CASCADE)
    day = models.ForeignKey(Days, on_delete=models.RESTRICT, null=True, editable=True)
    startTime = models.TextField(null=True, editable=True)
    endTime = models.TextField(null=True, editable=True)

    models.UniqueConstraint(name='times_must_be_unique', fields=['startTime', 'endTime'], violation_error_message='Times Cannot Match')

    def __str__(self):
        return self.id
    

   