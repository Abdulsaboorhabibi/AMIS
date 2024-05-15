from django.db import models
from django.utils.text import slugify
import uuid 

class Location(models.Model):
    region = models.CharField(max_length=150, verbose_name="Region")
    province = models.CharField(max_length=150, verbose_name="Province")
    district = models.CharField(max_length=150, verbose_name="District")
    village = models.CharField(max_length=200, verbose_name="Village")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return f"{self.region} Region -- {self.province} Province --{self.district}"

    #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.village)

            while Location.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.village)}-{uuid.uuid4().hex[:8]}"
        super(Location, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

class Sector(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

        #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while Sector.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.name)}-{uuid.uuid4().hex[:8]}"
        super(Sector, self).save(*args, **kwargs)

    class Meta: 
        verbose_name = "Secotr"
        verbose_name_plural = "Sectors"

class Donor(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Name")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    abbr = models.CharField(max_length=8, verbose_name="Tag Name")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name 

    #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while Donor.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.name)}-{uuid.uuid4().hex[:8]}"
        super(Donor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donors"