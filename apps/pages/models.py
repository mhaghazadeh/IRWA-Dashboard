from django.db import models
from django.contrib.auth.models import User

# -----------------------
# LOOKUP TABLES
# -----------------------

class WasteType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WasteState(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WasteClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContainerType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=100,default="IRWA")

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=100)
    # site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class OriginFacility(models.Model):
    name = models.CharField(max_length=100)
    # site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



class Radionuclide(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -----------------------
# DYNAMIC FIELD RULES
# -----------------------

class FieldRule(models.Model):
    FIELD_CHOICES = [
        ('mass', 'Mass'),
        ('volume', 'Volume'),
        ('estimated_disposal_volume', 'Estimated Disposal Volume'),
        ('total_activity', 'Total Activity'),
        ('dose_rate_1m', 'Dose Rate 1m'),
        ('dose_rate_surface', 'Dose Rate Surface'),
        ('material', 'Material'),
        ('origin_of_waste', 'Origin of Waste'),
    ]

    waste_type = models.ForeignKey(WasteType, on_delete=models.SET_NULL, null=True)
    field_name = models.CharField(max_length=50, choices=FIELD_CHOICES)

    is_visible = models.BooleanField(default=True)
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.waste_type} - {self.field_name}"


# -----------------------
# MAIN MODEL (COMPLETE)
# -----------------------

class Inventory(models.Model):

    INVENTORY_STATUS = [
        ('current', 'Current Inventory'),
        ('disposed', 'Disposed'),
    ]

    waste_id = models.CharField(max_length=100)

    waste_type = models.ForeignKey(WasteType, on_delete=models.SET_NULL,null=True)
    waste_state = models.ForeignKey(WasteState, on_delete=models.SET_NULL,null=True)
    waste_class = models.ForeignKey(WasteClass, on_delete=models.SET_NULL, null=True)

    site = models.ForeignKey(Site, on_delete=models.SET_NULL,null=True)
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL,null=True)

    origin_of_waste = models.ForeignKey(OriginFacility, on_delete=models.SET_NULL,null=True)
    date_received = models.DateField()

    description = models.TextField(blank=True)

    material = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)

    container_type = models.ForeignKey(ContainerType, null=True, on_delete=models.SET_NULL)


    mass = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    estimated_disposal_volume = models.FloatField(null=True, blank=True)

    total_activity = models.FloatField(null=True, blank=True)

    dose_rate_1m = models.FloatField(null=True, blank=True)
    dose_rate_surface = models.FloatField(null=True, blank=True)

    location = models.CharField(max_length=100, blank=True)

    inventory_status = models.CharField(max_length=20, choices=INVENTORY_STATUS)

    radionuclides = models.ForeignKey(Radionuclide, null=True, on_delete=models.SET_NULL)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.waste_id