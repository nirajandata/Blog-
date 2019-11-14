from django.urls import path
from .views import HomeView , EntryView
urlpatterns=[
	path('home/',HomeView.as_view(),name='blog-home'),
	path('entry/<int:pk>/',EntryView.as_view(),name="entry-detail")
]