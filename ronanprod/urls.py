from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="home"),
	path('Participants', views.Participants, name="Participants"),
	path('revcen', views.revcen, name="revcen"),
	path('ReviewCenters', views.ReviewCenters, name="ReviewCenters"),
	path('enrol', views.enrol, name="enrol"),
	path('Enrollmentt', views.Enrollmentt, name="Enrollmentt"),
	path('pay', views.pay, name="pay"),
	path('Paymentt', views.Paymentt, name="Paymentt"),
	path('rev', views.rev, name="rev"),
	path('Reviewerss', views.Reviewerss, name="Reviewerss"),
	path('update_let/<str:pk>/', views.updateResult, name="update_let"),
	path('delete_let/<str:pk>/', views.deleteResult, name="delete_let"),
	# path('seven', views.twice, name="seven"),
	# path('delete/<int:id>', views.destroy),

]