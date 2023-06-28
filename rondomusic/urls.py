
from django.contrib import admin
from django.urls import path, include



from music import views

urlpatterns = [
	path("accounts/", include("django.contrib.auth.urls")),
	path('admin/', admin.site.urls),
    	path("music/", views.index, name="index"),
    	path("music/index.html", views.index, name="index"),
	path("music/events/<int:pk>/", views.event_detail, name="event_detail"),
	path("pieces/<int:piece_id>/", views.piece_detail, name="piece_detail"),
	path("music/update_part/", views.update_part, name="update_part"),
	path("music/add_piece/", views.add_piece, name="add_piece"),
	
]