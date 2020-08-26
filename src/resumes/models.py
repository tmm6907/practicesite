from django.db import models

# Create your models here.

class User(models.Model):
    full_name        = models.CharField(max_length=64, blank=False)
    email            = models.EmailField(blank=False)
    address          = models.CharField(max_length=64, blank=False)
    phone            = models.CharField(max_length=11, blank=False)

class Education(models.Model):
    EDUCATION_LEVEL = [
        ('Some_High_School' , 'Some High School'),
        ('Diploma_GED', 'High School Diploma / GED'),
        ('Some_College', 'Some College'),
        ('Associates', 'Associates Degree'),
        ('Bachelors', 'Bachelor\'s Degree'),
        ('Higher', 'Master\'s Degree or Higher'),
    ]
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    level            = models.CharField(max_length=16,choices=EDUCATION_LEVEL)
    school_name      = models.CharField(max_length=64)
    start_year       = models.IntegerField()
    end_year         = models.IntegerField()
    location         = models.CharField(max_length=64,blank=True)

class Work(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    position         = models.CharField(max_length=32, blank=True)
    description      = models.TextField(max_length=240, blank=False)
    start_date       = models.CharField(max_length=24)
    end_date         = models.CharField(max_length=24, default = 'present')

