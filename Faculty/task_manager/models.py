""" models for the task_manager app """
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Department(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name

class UserData(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "UserData"

    def __str__(self):
        return str(self.user)

class KRA(models.Model):
    category = models.CharField(max_length=300)

    def __str__(self):
        return self.category

class Metric(models.Model):
    description = models.CharField(max_length=200)
    category = models.ForeignKey(KRA, related_name='metrics', on_delete=models.CASCADE)
    # TODO: add marks field

    def __str__(self):
        return self.description

class Task(models.Model):
    key_area = models.ForeignKey('KRA', on_delete=models.CASCADE)
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("is_chairman", "is the Chairman"),
            ("is_principal", "is the principal"),
            ("is_Faculty", "is a Faculty Member"),
            ("is_HOD", "is HOD of the Department")
        )
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
