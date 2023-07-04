from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import Event, Piece,  Part, Instrument

##################################
# Index view
##################################

def index(request):
	events_list = Event.objects.order_by("date")
	#attendees = [e.attendees.first_name for e in events_list]
	context = {
        "events": events_list,
	}
	return render(request, "music/index.html", {"events": events_list})

##################################
# Event detail view
##################################

def event_detail(request, pk):
	event = get_object_or_404(Event, pk=pk)
	request.session['event'] = pk
	return render(request, "music/event_detail.html", {"event": event})

##################################
# Piece detail view
##################################
def piece_detail(request, piece_id):
	piece = get_object_or_404(Piece, pk=piece_id)
	request.session['piece'] = piece_id
	#piece = get_object_or_404(Piece, pk=piece_id)
	event_id = request.session['event']
	return render(request, "music/piece_detail.html", {"piece" : piece, "event" : event_id})

##################################
# Add piece view
# for future work
##################################

def add_piece(request):
	instruments = Instrument.objects
	instrument_list =[]
	for i in instruments:
		instrument_list.append(i['instrument_name'])
	return render(request, "music/new_piece.html", {'instruments' : instrument_list})
	if request.method =="POST":
		new_piece = Piece()
		new_piece.piece_name = requesst.POST['piece_name']
		new_piece.composer = requesst.POST['composer']
		new_piece.source = requesst.POST['source']
		new_piece.notes = requesst.POST['notes']
		#new_piece.save()
	

##################################
# Update part view
##################################

def update_part(request):
	if request.method == "POST":
		piece = request.session['piece']
		PartID = request.POST['PartID']
		new_player_name = request.POST['players']
		new_player = None
		if new_player_name != "Unassigned":
			new_player = User.objects.get(first_name = new_player_name)
		part_update = Part.objects.get(pk = PartID)
		part_update.player = new_player
		part_update.save()
	event_id = request.session['event']	
	return redirect(event_detail, pk=event_id)


