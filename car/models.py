from django.db import models

class Car(models.Model):
    reg_num = models.CharField(max_length=20, verbose_name="reg_munber", blank=True)
    vin = models.CharField(max_length=20, verbose_name="vin_munber", blank=True )
    manifactures = models.ForeignKey("Manifactures", on_delete=models.CASCADE)
    owner_car = models.ForeignKey("Owner", on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(verbose_name='date created', auto_now_add=True, blank=True)

    def __str__(self):
        out_string = "{} --- {}".format(self.reg_num, self.vin)
        return out_string

class Owner(models.Model):
    f_name = models.CharField(max_length=100, verbose_name="first name", blank=False)
    l_name = models.CharField(max_length=100, verbose_name="last name", blank=True)
    phone = models.CharField(max_length=100, verbose_name="phone", blank=True)
    owner_data = models.TextField(verbose_name = "description owner")
    date_created = models.DateTimeField(verbose_name='date created', auto_now_add=True, blank=True)


class Manifactures(models.Model):
    title_manifactures = models.CharField(max_length=200, verbose_name="maifactures", blank=False)
    
class Repair(models.Model):
    title_repair = models.CharField(max_length=200, verbose_name="rapair description", blank=False)
    car_repair = models.ForeignKey("Car", on_delete=models.CASCADE)
    date_repair = models.DateTimeField(verbose_name='date repair', auto_now_add=True, blank=True)

class Parts(models.Model):
    title_part = models.CharField(max_length=200, verbose_name="title part", blank=False)
    price_patr = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="price part", blank=False)
    repair = models.ForeignKey("Repair", on_delete=models.CASCADE)

    
class Works(models.Model):
    title_work = models.CharField(max_length=200, verbose_name="title work", blank=False)
    price_patr = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="price part", blank=False)
    repair = models.ForeignKey("Repair", on_delete=models.CASCADE)

