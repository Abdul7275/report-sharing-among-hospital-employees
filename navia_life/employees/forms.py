from django import forms
from django.contrib.auth.models import User
from employees.models import UserProfileInfo,UploadReport
from .choices import TYPE_CHOICES



class ReportForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    #share_with = forms.MultipleChoiceField(choices=TYPE_CHOICES,widget=forms.CheckboxSelectMultiple)
    report_file = forms.FileField()

    class Meta():
        model = UploadReport
        fields = ('title','description','report_file')

class ShareReports(forms.ModelForm):
    Share_With_Doctors = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    Share_With_Nurses = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    Share_With_Receptionists = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    class Meta():
        model = UploadReport
        fields = ('Share_With_Doctors','Share_With_Nurses','Share_With_Receptionists')

class UserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    portfolio_site = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    about_me = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
    type = forms.ChoiceField(choices=TYPE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class UpdateUserDetails(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','readonly':'readonly'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email')

class UpdateProfileDetails(forms.ModelForm):
    portfolio_site = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    about_me = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))

    class Meta():
        model = User
        fields = ('portfolio_site','about_me')
