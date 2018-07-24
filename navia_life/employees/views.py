# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import UserForm,UserProfileInfoForm,UpdateUserDetails,UpdateProfileDetails,ReportForm,ShareReports
from .models import UserProfileInfo,User,UploadReport

# Create your views here.
def index(request):
    #val = UserProfileInfo.objects.filter(user=request.user)
    return render(request,'employees/index.html',{'page_title':'Home Page'})

''' view for logging out the user  '''
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    ''' view for login request
        login view is same for every user
        Type of user is checked from the database and redirected to the respected page
     '''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/emp')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                message="Account Not Active"
                return render(request,'employees/login.html',{'message':message})
        else:
            print "Someone tried to Login"
            print ("Username: {} and tried Password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'employees/login.html',{'page_title':'Login'})



''' view for viewing the user profile '''
def view_profile(request):
    val = UserProfileInfo.objects.filter(user=request.user)
    return render(request,'employees/profile.html',{'val':val,'page_title':'Profile Page'})



''' view for updating the profile '''
def update_profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/emp/user_login')
    else:
        if request.method=='POST':
            user_form = UpdateUserDetails(data=request.POST, instance=request.user)
            profile = UserProfileInfo.objects.filter(user=request.user).first()
            profile_form = UpdateProfileDetails(data=request.POST, instance=profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_obj=profile_form.save(commit=False)
                profile_obj.user = request.user
                profile_obj.save()
                return HttpResponseRedirect('/emp/profile')

        val = User.objects.get(username=request.user)
        val1 = UserProfileInfo.objects.get(user=request.user)
        data = {'username':val.username,'email':val.email,'portfolio_site':val1.portfolio_site,'about_me':val1.about_me}
        user_form=UpdateUserDetails(initial=data)
        profile_form = UpdateProfileDetails(initial=data)
        return render(request,'employees/update_profile.html',{'user_form':user_form,'profile_form':profile_form})


''' view for uploading report '''
def upload_report(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            report_form = ReportForm(request.POST,request.FILES)
            print report_form
            if report_form.is_valid():
                report = report_form.save(commit=False)
                report.user = request.user

                if 'report_file' in request.FILES:
                    report.report_file = request.FILES['report_file']
                report.save()
                return HttpResponseRedirect('/emp/profile')
            else:
                return HttpResponseRedirect('/emp/submit_report')
        else:
            report_form = ReportForm()
            return render(request,'employees/submit_report.html',{
                    'report_form':report_form,
                    'page_title':'Upload Report'
            })
    else:
        return HttpResponseRedirect('/emp/user_login')


''' view for viewing report '''
def view_reports(request):
    if request.method == 'POST':
        share_report = ShareReports(data=request.POST)
        if share_report.is_valid():
            ids = request.POST.get('idx')
            x= share_report.cleaned_data['Share_With_Doctors']
            y = share_report.cleaned_data['Share_With_Nurses']
            z = share_report.cleaned_data['Share_With_Receptionists']
            x = UploadReport.objects.filter(id=ids).update(Doctor=x,Nurse=y,Receptionist=z)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Error Sharing report")
    else:
        form = ShareReports()
        val = UploadReport.objects.all().filter(user=request.user)
        return render(request,'employees/view_reports.html',{'val':val,'form':form})



''' view for checking shared reports '''
def shared_reports(request):
    val1 = UserProfileInfo.objects.get(user=request.user)
    x={}
    x[val1.type]=True
    reports = UploadReport.objects.filter(**x)
    return render(request,'employees/shared.html',{'reports':reports})


''' view for registering a user '''
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/emp')

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False   #this is done to prevent unauthrised users to register and login
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.type = profile_form.cleaned_data['type']
            #print profile.type

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            return render(request,'employees/login.html',{'message':'Thank You For Registering'})
        else:
            print (user_form.errors,profile_form.errors)
    else:
        user_form =UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'employees/registration.html',{
            'user_form':user_form,
            'profile_form':profile_form,
            'page_title':'Register'
    })
