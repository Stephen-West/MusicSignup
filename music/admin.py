from django.contrib import admin

# Register your models here.

from django.contrib import admin





from .models import Player
admin.site.register(Player)

from .models import Instrument
admin.site.register(Instrument)

from .models import Part
class partInline(admin.TabularInline):
	model=Part

admin.site.register(Part)

from .models import Event
admin.site.register(Event)

from .models import Piece
class PieceAdmin(admin.ModelAdmin):
	inlines = [partInline,]
admin.site.register(Piece, PieceAdmin,)


