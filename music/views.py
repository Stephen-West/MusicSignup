from django.shortcuts import get_object_or_404, render

class This_piece:
	title = ""
	composer = ""
	source = ""
	user = ""
	number_of_parts = 0
	part_list = []
	

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Event, Piece, Player, Part

def index(request):
	#return HttpResponse("Hello, world. You're at the polls index.")

	events_list = Event.objects.order_by("-date")
	template = loader.get_template("music/index.html")
	context = {
        "events": events_list,
	}
	return HttpResponse(template.render(context, request))

def event_detail(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, "music/sign_up_page.html", {"event": event})

def who_am_i(request):
	return HttpResponse("You are " + request.user.username)

def piece_detail(request, piece_id):
	if request.method == "POST":
		#return HttpResponse("Hello, world. "+ " ".join(list(request.POST.keys())))
		#message =dict(request.POST.items()) +" " + request.POST['PartID']
		#return HttpResponse(request.POST['PartID'])

		PartID = request.POST['PartID']
		#new_player_name = request.POST['players']
		new_player = Player.objects.get(player_name = request.POST['players'])
		part_update = Part.objects.get(pk = PartID)
		#part_update.id = PartID
		part_update.player = new_player
		part_update.save()
	

	piece = get_object_or_404(Piece, pk=piece_id)
	this_piece = This_piece()
	this_piece.title = piece.piece_name
	this_piece.composer = piece.composer
	this_piece.source = piece.source
	this_piece.user = request.user.username
	this_piece.part_list = []


	return render(request, "music/piece_detail.html", {"piece": piece})

def add_piece(request):
	return render(request, "music/new_piece.html", )


def update_part(request):
	pass