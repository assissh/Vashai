
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class NewsLetterUser(models.Model):
    email = models.CharField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.email


class intrest(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
   # intrest = models.CharField(max_length=10)
    actor = models.BooleanField( default=False )
    Feature_Film_Production = models.BooleanField(default=False)
    TV_Corporates_or_AV  = models.BooleanField(default=False)
    Filming_OR_Event_Permissions = models.BooleanField(default=False)
    Augmented_Reality_Campaigns = models.BooleanField(default=False)
    Third_Dimension_Design_OR_Modelling_OR_WalkThrough_Or_Animations  = models.BooleanField(default=False)
    IT_Consultancy = models.BooleanField(default=False)
    Application_Devalopment_Or_Web_Designing = models.BooleanField(default=False)
    Mobile_Application_Development = models.BooleanField(default=False)
    Webcasting_Services_End_to_End = models.BooleanField(default=False)
    Coperate_Identities_or_Brand_Building = models.BooleanField(default=False)
    Creative_Consultancy = models.BooleanField(default=False)
    Print_Designing = models.BooleanField(default=False)


    def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile = intrest.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile,sender=User)