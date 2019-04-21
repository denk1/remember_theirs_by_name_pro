from django.contrib import admin
from remember_theirs_by_name_pro.models import  Person, \
                                                District, \
                                                CallingTeam, \
                                                Locality, \
                                                Mobilization, \
                                                MilitaryEnlistmentOffice, \
                                                Region, \
                                                WarUnit, \
                                                WarServe


admin.site.register(District)
admin.site.register(CallingTeam)
admin.site.register(Locality)
admin.site.register(Mobilization)
admin.site.register(MilitaryEnlistmentOffice)
admin.site.register(Person)
admin.site.register(Region)
admin.site.register(WarUnit)
admin.site.register(WarServe)