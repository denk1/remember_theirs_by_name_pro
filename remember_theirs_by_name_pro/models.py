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


class WarUnit(models.Model):
    """
    Подразделения
    """
    above_war_init = models.ForeignKey("WarUnit", null=True, on_delete=models.CASCADE)
    military_personnel = models.ManyToManyField("Person", through='WarServe')
    name = models.CharField(max_length=60)


class WarServe(models.Model):
    """
    Военная служба
    """
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    war_unit = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    

class CallingTeam(models.Model):
    """
    Призывная команда
    """
    name = models.CharField(max_length=30, null=True)


class CallingTeamDirection(models.Model):
    calling_team = models.ForeignKey(CallingTeam, on_delete=models.CASCADE)
    war_unit_direction = models.ForeignKey("WarUnit", on_delete=models.CASCADE)


class MilitaryEnlistmentOffice(models.Model):
    """
    Военкомат
    """
    address = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobilizations = models.ManyToManyField("Mobilization", through="Call")


class Mobilization(models.Model):
    date_mobilization = models.DateField()
    military_enlistment_officies = models.ManyToManyField("MilitaryEnlistmentOffice", through="Call")


class Call(models.Model):
    military_enlistment_office = models.ForeignKey(MilitaryEnlistmentOffice, on_delete=models.CASCADE)
    mobilization = models.ForeignKey(Mobilization, on_delete=models.CASCADE)


class Hospital(models.Model):
    address = models.ForeignKey(Locality, on_delete=models.CASCADE)
    patients = models.ManyToManyField("Person", through='Hospitalization')
    name = models.CharField(max_length=256)


class Hospitalization(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    hospital= models.ForeignKey(Hospital, on_delete=models.CASCADE)
    period_from = models.DateField(null=False)
    period_to = models.DateField(null=False)
    war_unit_consist = models.ForeignKey(WarUnit, on_delete=models.CASCADE)
    direction_name = models.CharField(max_length=256)


class WarOperation(models.Model):
    name = models.CharField(max_length=256)
    participants = models.ManyToManyField(WarServe, through="WarArchievement")
    def __str__(self):
        return self.name


class WarArchievement(models.Model):
    war_operation = models.ForeignKey(WarOperation, on_delete=models.CASCADE)
    war_serve = models.ForeignKey(WarServe, on_delete=models.CASCADE)
    period_from = models.DateField(null=False)
    period_to = models.DateField(null=False)
    


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
    born_locality = models.ForeignKey(Locality, related_name='born', on_delete=models.CASCADE)
    live_locality = models.ForeignKey(Locality, related_name='live', on_delete=models.CASCADE)
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.father_name