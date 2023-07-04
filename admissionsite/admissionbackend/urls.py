

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    
    path('studentadmission/', views.studentAdmission, name='studentadmission'),
    path('studentadmission/<int:id>/', views.studentAdmission, name='studentadmission'),
    path('studentadmission/<int:id>/delete/', views.studentAdmissionDelete, name='studentadmissiondelete'),
    path('studentadmission/<int:id>/update/', views.studentAdmissionUpdate, name='studentadmissionupdate'),

]
