from remember_theirs_by_name_pro.models import Person, \
                                               Mobilization, \
                                               MilitaryEnlistmentOffice, \
                                               Region, \
                                               District, \
                                               Locality, \
                                               CallingTeam, \
                                               WarUnit, \
                                               WarServe, \
                                               CallingTeamDirection, \
                                               MilitaryEnlistmentOfficeCallingTeam, \
                                               Call, \
                                               Hospital, \
                                               Hospitalization, \
                                               WarOperation, \
                                               WarArchievement

address_data = [Region, District, Locality]


def find_record(set_objects, object_value):
    aim_object = set_objects.objects.filter(object_value)
    if aim_object.count() > 0:
        return aim_object[0]
    else:
        return None


def fill_address(address, level):
    is_new = False
    addr_prev = None
    addr = None
    for i in range(level):
        addr = find_record(address_data[i],  {'region_name__iexact': address[i]})
        if addr is None or is_new is True:
            if i == 0:
                address_data[i].objects.create(region_name = address[i])
            else:
                address_data[i].objects.create(up_place=addr_prev, name=address)
            is_new = True

        addr_prev = addr
    return addr 


def fill_war_unit(war_units):
    count_item = len(war_units)
    for unit_name in war_units:
        unit = find_record(WarUnit, {'name__iexact' : unit_name})
        if unit is None:
            WarUnit.objects
        
        
def find_record(war_units, d_name):
    war_units = war_units.objects.filters(d_name)
    if war_units.count() > 0:
        return war_units[0]
    elif:
        return None


def fill_new_line(post_obj):
    # personalization
    surname = post_obj.get("surname")
    surname_distortion = post_obj.get("surname_distortion")
    name = post_obj.get("name")
    name_distortion = post_obj.get("name_distortion")
    father_name = post_obj.get("father_name")
    father_name_distortion = post_obj.get("father_name_distortion")
    birthday = post_obj.get("birthday")
    data_mobilization = post_obj.get("date_mobilization")
    born_region_name = post_obj.get("born_region_name")
    born_district_name = post_obj.get("born_district_name")
    born_locality_name = post_obj.get("born_locality_name")
    born_address = [born_region_name, born_district_name, born_locality_name]
    born_locality = fill_address(born_address, 3)
    live_region_name = post_obj.get("live_region_name")
    live_district_name = post_obj.get("live_district_name")
    live_locality_name = post_obj.get("live_locality_name")
    live_address = [live_region_name, live_district_name, live_locality_name]
    live_locality = fill_address(live_address, 3)

    # mobilization
    data_mobilization = post_obj.get("date_mobilization")
    region_military_enlistment_office = post_obj.get("region_region_military_enlistment_office")
    district_military_enlistment_office = post_obj.get("district_military_enlistment_office")
    military_enlistment_office_address = [region_military_enlistment_office, district_military_enlistment_office]
    military_enlishment_name = post_obj.get("military_enlishment_name")
    military_enlishment_office_district = fill_address(military_enlistment_office_address, 2)
    calling_team_name = post_obj.get("draft_team_name")
    front_name = post_obj.get("front_name")
    army_name = post_obj.get("army_name")
    warunit_name = post_obj.get("warunit_name")
    war_units = [front_name, army_name, warunit_name]
    warunit = None
    if warunits.count() > 0:
        warunit = warunits[0]
    else:
        WarUnit.objects.create(name=warunit_name, )
        WarServe.objects.create()


    moblization = Mobilization.objects.create(data_mobilization=data_mobilization,
                                              military_enlistment_office=military_enlistment_office,
                                              calling_team=calling_team)
    
    new_person = Person.objects.create(surname = surname,
                          surname_distortion = surname_distortion,
                          name = name, 
                          name_distortion = name_distortion,
                          father_name = father_name_distortion,
                          born_locality = born_locality,
                          live_locality = live_locality)
    
#    war_serve = WarServe(person = new_person,
#                         war_unit = warunit,
#                         period_from )

    
     





