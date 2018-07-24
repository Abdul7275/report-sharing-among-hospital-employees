from django.conf.urls import url
from employees import views

app_name = 'employees'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'register/$',views.register, name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^profile/$',views.view_profile,name='profile'),
    url(r'^update_profile/$',views.update_profile,name='update_profile'),
    url(r'^submit_report/$',views.upload_report,name='submit_report'),
    url(r'^view_reports/$',views.view_reports,name='view_reports'),
    url(r'^shared_reports/$',views.shared_reports,name='shared_reports'),
]
