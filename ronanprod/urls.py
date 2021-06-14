from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage),
	path('firstpage.html', views.homepage, name="firstpage.html"),
	path('reviewcenter.html', views.Participants, name="reviewcenter.html"),
	# path('nan', views.ReviewCenterr, name="nan"),
	path('enrollment.html', views.Enroll, name='enrollment.html'),
	path('feedback.html', views.Feed, name='feedback.html'),
	path('reviewer.html', views.Review, name='reviewer.html'),
	# path('nan', views.Exam, name="nan"),
	# path('success', views.Nextpage, name="success"),
]