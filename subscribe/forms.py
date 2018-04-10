from django import forms
from .models import *

class NewsletterSignUpForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model = NewsLetterUser
        fields = ['email']


class intrestform(forms.ModelForm):
    class Meta:
        model = intrest
        fields = ['actor','Feature_Film_Production','TV_Corporates_or_AV','Filming_OR_Event_Permissions','Augmented_Reality_Campaigns','Third_Dimension_Design_OR_Modelling_OR_WalkThrough_Or_Animations','IT_Consultancy','Application_Devalopment_Or_Web_Designing','Mobile_Application_Development','Webcasting_Services_End_to_End','Coperate_Identities_or_Brand_Building','Creative_Consultancy','Print_Designing']