from django.urls import path
from . import views
from .views import PasswordsChangeView
from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings
import os


def download_template(request):
    file_path = settings.BASE_DIR / 'line' / 'static' / 'xlsx' / 'ImportTemplate.xlsx'
    
    if file_path.exists():
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='ImportTemplate.xlsx')
    else:
        return HttpResponseNotFound("File not found")

urlpatterns = [
    path('', views.index, name='index'),
    path('member/', views.member, name='member'),
    path('capacity/', views.capacity, name='capacity'),
    path('capacity/selector/', views.selector, name='selector'),
    path('select/', views.select, name='select'),
    path('select/loggedout_manual/', views.loggedout_manual, name='loggedout_manual'),
    path('select/selected/', views.selected, name='selected'),
    path('pas/', views.pas, name='pas'),
    path('pas/change_password/', PasswordsChangeView.as_view(template_name = 'change_password.html')),
    path('userdata/', views.userdata, name='userdata'),
    path('get_real_time_data/', views.get_real_time_data, name='get_real_time_data'),
    path('get_selection_data/', views.get_selection_data, name='get_selection_data'),
    path('realtime_data_page/', views.realtime_data_page, name='realtime_data_page'),
    path('update_real_time_data/', views.update_real_time_data, name='update_real_time_data'),
    path('select/concurrentlogincheck/', views.concurrentlogincheck, name='concurrentlogincheck'),
    path('validate_selections/', views.validate_selections, name='validate_selections'),
    path('select/validate_selections/', views.validate_selections, name='validate_selections'),
    path('get_selected_options/', views.get_selected_options, name='get_selected_options'),
    path('select/get_selected_options/', views.get_selected_options, name='get_selected_options'),
    path('admin/download-template/', download_template, name='admin_download_template'),
]
