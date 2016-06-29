from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^patient_search_results$', views.patient_list, name='patient_list'),
    #url(r'^reports$', views.report_list, name='report_list'),
    #url(r'^alerts$', views.alert_list, name='alert_list'),
    #url(r'^users$', views.user_list, name='user_list'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^alerts/builder$', views.alert_builder, name='alert_builder'),
    ]