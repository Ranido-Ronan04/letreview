from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="home"),
	path('Participants', views.Participants, name="Participants"),
	path('ReviewCenters', views.ReviewCenters, name="ReviewCenters"),
	path('Enrollmentt', views.Enrollmentt, name="Enrollmentt"),
	path('Paymentt', views.Paymentt, name="Paymentt"),
	path('Reviewerss', views.Reviewerss, name="Reviewerss"),
	path('update_let/<str:pk>/', views.updateResult, name="update_let"),
	path('delete_let/<str:pk>/', views.deleteResult, name="delete_let"),
	# path('seven', views.twice, name="seven"),
	# path('delete/<int:id>', views.destroy),

]