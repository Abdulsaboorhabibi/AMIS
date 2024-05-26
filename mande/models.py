from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from datetime import datetime, timedelta
from django.utils import timezone
import uuid

from utility.models import Location, Sector, Donor


# achive 6 month after now
def six_month_after_now():
    return datetime.now() + timedelta(days=30 * 6)


class Project(models.Model):

    PROJECT_OVERALL_STATUS_CHOICES = [
        ("N", "Not Started"),
        ("S", "On Start"),
        ("P", "In Progress"),
        ("C", "Completed"),
        ("PN", "Pendding"),
        ("CN", "Canncelled"),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="sluge")
    sector = models.ForeignKey(
        Sector, models.SET_NULL, null=True, blank=True, verbose_name="Sector"
    )
    donor = models.ForeignKey(Donor, models.CASCADE, verbose_name="Donor")
    location = models.ForeignKey(
        Location, models.SET_NULL, null=True, blank=True, verbose_name="Location"
    )
    start_date = models.DateField(auto_now=True, verbose_name="Start Date")
    end_date = models.DateField(default=six_month_after_now, verbose_name="End Date")
    idp = models.BooleanField(default=False, verbose_name="IDP")
    idp_returnee = models.BooleanField(default=False, verbose_name="IDP/Returnee")
    refugee = models.BooleanField(default=False, verbose_name="Refugee")
    host = models.BooleanField(default=False, verbose_name="Host")
    kochi = models.BooleanField(default=False, verbose_name="Kochi")
    male = models.BooleanField(default=False, verbose_name="Male")
    female = models.BooleanField(default=False, verbose_name="Female")
    childern = models.BooleanField(default=False, verbose_name="Childern")
    childern_age_from = models.IntegerField(
        verbose_name="Childer Start age",
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        blank=True,
        null=True,
    )
    childern_age_end = models.IntegerField(
        verbose_name="Childer End age",
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        blank=True,
        null=True,
    )
    plw = models.BooleanField(default=False, verbose_name="PLW")
    pwd = models.BooleanField(default=False, verbose_name="PWd")
    overall_Status = models.CharField(
        max_length=50,
        choices=PROJECT_OVERALL_STATUS_CHOICES,
        default=PROJECT_OVERALL_STATUS_CHOICES,
        verbose_name="Overall Status",
    )
    remarks = models.TextField(max_length=300, blank=True, null=True)
    doc = models.DateField(auto_now_add=True)
    dou = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    # auto generate the sluge
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            while Project.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{uuid.uuid4().hex[:8]}"
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-doc"]


class MonitorProject(models.Model):

    PROGRESS_STATUS_CHOICES = [
        ("P", "Within The Plane"),
        ("PD", "Pendding"),
        ("NS", "Lag Behind Plane"),
        ("E", "Execute Plane"),
    ]
    activity = models.CharField(max_length=255)
    project = models.ForeignKey(Project, models.CASCADE, verbose_name="Project")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    pregress_percentage = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name="Progress Percentage(%)",
    )
    progress_status = models.CharField(max_length=200, choices=PROGRESS_STATUS_CHOICES)
    description = models.CharField(
        max_length=255, verbose_name="Description", blank=True, null=True
    )
    doc = models.DateField(auto_now_add=True)
    dou = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.project.title} - {self.get_progress_status_display()}"

    # auto generate the sluge
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"{self.get_progress_status_display()}-{datetime.now()}"
            )

            while MonitorProject.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.get_progress_status_display())}-{uuid.uuid4().hex[:8]}"
        super(MonitorProject, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Project Monitor"
        verbose_name_plural = "Project Monitors"
        ordering = ["-doc"]
