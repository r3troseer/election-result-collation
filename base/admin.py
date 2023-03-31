from django.contrib import admin
from .models import Agentname, AnnouncedLgaResults, AnnouncedPuResults, AnnouncedStateResults, AnnouncedWardResults, Lga, Party, PollingUnit, States, Ward
# Register your models here.
admin.site.register(Agentname)
admin.site.register(AnnouncedLgaResults)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedWardResults)
admin.site.register(Lga)
admin.site.register(Party)
admin.site.register(PollingUnit)
admin.site.register(States)
admin.site.register(Ward)
