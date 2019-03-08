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

class Person(models.Model):
    """
    ФИО, дата рождения, мобилизация, последнее сообщение
    """
    name = models.CharField(max_length=30, default='Неизвестно')
    name_distortion = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, default='Неизвестно')
    surname_distortion = models.CharField(max_length=30, null=True)
    father_name = models.CharField(max_length=30, null=True)
    father_name_distortion = models.CharField(max_length=30, null=True)
    birthday = models.DateField(null=True)
    mobilization_id = models.ForeignKey("Mobilization", null=True, on_delete=models.SET_NULL)
    born_address_id = models.ForeignKey(Locality, related_name='born', null=True, on_delete=models.SET_NULL)
    live_address_id = models.ForeignKey(Locality, related_name='live', null=True, on_delete=models.SET_NULL)


class WarUnit(models.Model):
    """
    Подразделения
    """
    above_unit_id = models.ForeignKey("WarUnit", null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=60)


class CallingTeam(models.Model):
    team_number = models.CharField(max_length=30)
    name = models.CharField(max_length=30, null=True)


class MilitaryEnlistmentOffice(models.Model):
    address_id = models.ForeignKey(Locality, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Mobilization(models.Model):
    date_mobilization = models.DateField()
    military_enlistment_office_id = models.ForeignKey(MilitaryEnlistmentOffice, null=True, on_delete=models.SET_NULL)
    calling_team_id = models.ForeignKey(CallingTeam, on_delete=models.CASCADE)
    directed_war_unit_id = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    last_message_from_locality_id = models.ForeignKey(Locality, null=True, on_delete=models.SET_NULL)


class ArchievementList(models.Model):
    personal_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    period_from = models.DateField(null=False)
    period_to = models.DateField(null=False)
    war_unit_id = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    war_operation_id = models.ForeignKey("WarOperation", on_delete=models.CASCADE)
    adding_info = models.CharField(max_length=256)


class Hospitalization(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    period_from = models.DateField(null=False)
    period_to = models.DateField(null=False)
    name = models.CharField(max_length=256)
    locality_id = models.ForeignKey(Locality, on_delete=models.CASCADE)
    war_unit_consist_id = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    direction_name = models.CharField(max_length=256)


class WarOperation(models.Model):
    name = models.CharField(max_length=256)