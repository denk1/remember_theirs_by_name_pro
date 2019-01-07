from django.contrib import admin
from remember_theirs_by_name_pro.models import Person, \
Address, \
Direction, \
District, \
DraftTeam, \
DraftTeamMilitaryEnlistmentOffice, \
LastMessage, \
Locality, \
Mobilization, \
MobilizationDirection, \
MilitaryEnlistmentOffice, \
PersonBornAddress, \
PersonLiveAddress, \
Region, \
WarUnit 


admin.site.register(Direction)
admin.site.register(District)
admin.site.register(DraftTeam)
admin.site.register(DraftTeamMilitaryEnlistmentOffice)
admin.site.register(LastMessage)
admin.site.register(Locality)
admin.site.register(Mobilization)
admin.site.register(MobilizationDirection)
admin.site.register(MilitaryEnlistmentOffice)
admin.site.register(Person)
admin.site.register(PersonBornAddress)
admin.site.register(PersonLiveAddress)
admin.site.register(Region)
admin.site.register(WarUnit)
admin.site.register(Address)