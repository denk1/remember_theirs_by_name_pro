from django.db import models


class Locality(models.Model):
    """
    Населенный пункт
    """
    up_place = models.ForeignKey('District', on_delete=models.CASCADE)
    name = models.CharField(max_length=90)


class District(models.Model):
    """
    Район 
    """
    up_place = models.ForeignKey('Region', on_delete=models.CASCADE)
    name = models.CharField(max_length=90)


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
    born_address_id = models.ForeignKey(Locality, related_name='born', on_delete=models.CASCADE)
    live_address_id = models.ForeignKey(Locality, related_name='live', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class WarUnit(models.Model):
    """
    Подразделения
    """
    above_war_init = models.ForeignKey("WarUnit", null=True, on_delete=models.CASCADE)
    military_personnel = models.ManyToManyField(Person, through='WarServe')
    name = models.CharField(max_length=60)


class WarServe(models.Model):
    """
    Военная служба
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    war_unit = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    period_from = models.DateField(null=False)
    period_to = models.DateField(null=True)


class CallingTeam(models.Model):
    name = models.CharField(max_length=30, null=True)


class MilitaryEnlistmentOffice(models.Model):
    address = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Mobilization(models.Model):
    date_mobilization = models.DateField()
    military_enlistment_office = models.ForeignKey(MilitaryEnlistmentOffice, null=True, on_delete=models.SET_NULL)
    calling_team = models.ForeignKey(CallingTeam, on_delete=models.CASCADE)
    directed_war_unit = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    last_message_from_locality = models.ForeignKey(Locality, null=True, on_delete=models.SET_NULL)


class Hospital(models.Model):
    adress = models.ForeignKey(Locality, on_delete=models.CASCADE)
    patients = models.ManyToManyField(Person, through='Hospitalization')
    name = models.CharField(max_length=256)


class Hospitalization(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    hospital= models.ForeignKey(Hospital, on_delete=models.CASCADE)
    period_from = models.DateField(null=False)
    period_to = models.DateField(null=False)
    war_unit_consist = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    direction_name = models.CharField(max_length=256)


class WarOperation(models.Model):
    name = models.CharField(max_length=256)
    participants = models.ManyToManyField(WarServe, through="WarArchievement")
    period_from = models.DateField(null=False)
    period_to = models.DateField(null=False)
    adding_info = models.CharField(max_length=256, null=True)


class WarArchievement(models.Model):
    war_operation = models.ForeignKey(WarOperation, on_delete=models.CASCADE)
    war_serve = models.ForeignKey(WarServe, on_delete=models.CASCADE)

