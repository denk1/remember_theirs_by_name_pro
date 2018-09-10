from django.db import models


class Locality(models.Model):
    """
    Населенный пункт
    """
    district_id = models.ForeignKey('District', on_delete=models.CASCADE)
    locality_name = models.CharField(max_length=90)


class District(models.Model):
    """
    Район 
    """
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE)
    district_name = models.CharField(max_length=90)


class Region(models.Model):
    """
    Область
    """
    region_name = models.CharField(max_length=90)


class Address(models.Model):
    locality_id = models.ForeignKey(Locality, null=True, on_delete=models.SET_NULL)


class Person(models.Model):
    name = models.CharField(max_length=30, default='Неизвестно')
    name_distortion = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, default='Неизвестно')
    surname_distortion = models.CharField(max_length=30, null=True)
    father_name = models.CharField(max_length=30, null=True)
    father_name_distortion = models.CharField(max_length=30, null=True)
    birthday = models.DateField(null=True)
    mobilization_id = models.ForeignKey("Mobilization", null=True, on_delete=models.SET_NULL)
    last_message_id = models.ForeignKey("LastMessage", null=True, on_delete=models.SET_NULL)


class PersonBornAddress(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    place_of_born_id = models.ForeignKey(Address, on_delete=models.CASCADE)


class PersonLiveAddress(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    place_of_live_id = models.ForeignKey(Address, on_delete=models.CASCADE)


class WarUnit(models.Model):
    above_unit_id = models.ForeignKey("WarUnit", null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=60)


class DraftTeam(models.Model):
    team_number = models.CharField(max_length=10)
    name = models.CharField(max_length=30, null=True)

class MilitaryEnlistmentOffice(models.Model):
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class DraftTeamMilitaryEnlistmentOffice(models.Model):
    draft_team_id = models.ForeignKey(DraftTeam, on_delete=models.CASCADE)
    military_enlistment_office_id = models.ForeignKey(MilitaryEnlistmentOffice, on_delete=models.CASCADE)


class LastMessage(models.Model):
    location_id = models.ForeignKey(Address, on_delete=models.CASCADE)


class Mobilization(models.Model):
    date_mobilization = models.DateField()
    military_enlistment_office_id = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    draft_team_military_enlistment_office_id = models.ForeignKey(DraftTeamMilitaryEnlistmentOffice,\
                                                                 on_delete=models.CASCADE)


class Direction(models.Model):
    war_unit_id = models.ForeignKey(WarUnit, null=True, on_delete=models.SET_NULL)


class MobilizationDirection(models.Model):
    direction_id = models.ForeignKey(Direction, on_delete=models.CASCADE)
    mobilization_id = models.ForeignKey(Mobilization, on_delete=models.CASCADE)
