"""
URL configuration for rondomusic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
]

from music import views

urlpatterns = [
	path('admin/', admin.site.urls),
    	path("music/", views.index, name="index"),
	path("music/events/<int:event_id>/", views.event_detail, name="event_detail"),
	path("music/who_am_i", views.who_am_i),
	path("pieces/<int:piece_id>/", views.piece_detail, name="piece_detail"),
	path("music/update_part/", views.update_part, name="update_part"),
	path("music/add_piece/", views.add_piece, name="add_piece"),
]