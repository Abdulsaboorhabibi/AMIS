from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from datetime import datetime, timedelta
from django.utils import timezone
import uuid

from utility.models import LocationModel, SectorModel, DonorModel

# achive 6 month after now 
def six_month_after_now():
    return datetime.now() + timedelta(days=30*6)

class ProjectModel(models.Model):

    OVERALL_STATUS_CHOICES = [
        ('N','Not Started'),
        ('S', 'On Start'),
        ('P', 'In Progress'),
        ('C', 'Completed'),
        ('PN', 'Pendding'),
        ('CN', 'Canncelled')
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="sluge")
    sector = models.ForeignKey(SectorModel, models.SET_NULL, null=True, blank=True, verbose_name="Sector")
    donor = models.ForeignKey(DonorModel, models.CASCADE, verbose_name="Donor")
    location = models.ForeignKey(LocationModel,models.SET_NULL, null=True, blank=True,  verbose_name="Location")
    start_date = models.DateField(auto_now=True, verbose_name="Start Date")
    end_date = models.DateField(default=six_month_after_now, verbose_name="End Date")
    idp = models.BooleanField(default=False, verbose_name="IDP")
    idp_returnee = models.BooleanField(default=False, verbose_name="IDP/Returnee")
    refugee = models.BooleanField(default=False, verbose_name="Refugee")
    host = models.BooleanField(default=False, verbose_name='Host')
    kochi = models.BooleanField(default=False, verbose_name="Kochi")
    male = models.BooleanField(default=False, verbose_name="Male")
    female = models.BooleanField(default=False, verbose_name="Female")
    childern = models.BooleanField(default=False, verbose_name="Childern")
    childern_age = models.CharField(max_length=10, verbose_name="Childer age", blank=True, null=True)
    plw = models.BooleanField(default=False, verbose_name="PLW")
    pwd = models.BooleanField(default=False, verbose_name="PWd")
    overall_Status = models.CharField(max_length=50, choices=OVERALL_STATUS_CHOICES, default=OVERALL_STATUS_CHOICES, verbose_name="Overall Status")
    Major_Activity = models.TextField(max_length=1000, verbose_name="Major Activity / Delivery")
    remarks = models.TextField(max_length=300, blank=True, null=True)
    doc = models.DateField(auto_now_add=True)
    dou = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            while ProjectModel.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.title)}-{uuid.uuid4().hex[:8]}"
        super(ProjectModel, self).save(*args, **kwargs)
    
    class Meta: 
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-doc']



class MonitorProjectModel(models.Model):

    PROGRESS_STATUS_CHOICES = [
        ('P', 'Within The Plane'),
        ('PD', "Pendding"),
        ('NS', 'Lag Behind Plane'),
        ('E', 'Execute Plane'),
    ]

    project = models.ForeignKey(ProjectModel, models.CASCADE, verbose_name="Project")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    pregress_percentage = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name="Progress Percentage(%)")
    progress_status = models.CharField(max_length=200, choices=PROGRESS_STATUS_CHOICES)
    doc = models.DateField(auto_now_add=True)
    dou = models.DateField(auto_now=True)

    def __str__(self):
        return self.project.title + self.overall_Status

    #auto generate the sluge 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.overall_Status)

            while MonitorProjectModel.objects.filter(slug = self.slug).exists():
                self.slug = f"{slugify(self.overall_Status)}-{uuid.uuid4().hex[:8]}"
        super(MonitorProjectModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Project Monitor"
        verbose_name_plural = "Project Monitors"
        ordering = ['-doc']

