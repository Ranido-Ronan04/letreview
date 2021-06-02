from django.urls import path
from . import views

urlpatterns = [
	path('', views.html1),
	path('oks', views.Let, name="oks"),
	path('nan', views.Center, name="nan"),
	# path('nan', views.Exam, name="nan"),
	# path('success', views.Nextpage, name="success"),
]