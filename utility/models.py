from django.db import models
from django.utils.text import slugify
import uuid 

class LocationModel(models.Model):
    region = models.CharField(max_length=150, unique=True, verbose_name="Region")
    province = models.CharField(max_length=150, unique=True, verbose_name="Province")
    district = models.CharField(max_length=150, verbose_name="District")
    village = models.CharField(max_length=200, verbose_name="Village")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return f"{self.district}-district  -- {self.village}-Village -- {self.region} Region"

    #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.village)

            while LocationModel.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.village)}-{uuid.uuid4().hex[:8]}"
        super(LocationModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

class SectorModel(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

        #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while SectorModel.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.name)}-{uuid.uuid4().hex[:8]}"
        super(SectorModel, self).save(*args, **kwargs)

    class Meta: 
        verbose_name = "Secotr"
        verbose_name_plural = "Sectors"

class DonorModel(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name 

    #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while DonorModel.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.name)}-{uuid.uuid4().hex[:8]}"
        super(DonorModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donors"