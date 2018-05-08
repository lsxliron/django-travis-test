from django import forms
import models

class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ('fname', 'lname', 'age')