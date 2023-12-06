# models.py
from django.db import models
from django.utils.text import slugify




class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='static/main/img/cotigory-foto')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='')
    text = models.TextField(max_length=255)  # Set the maximum length for the text field
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

class Work(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Example for a salary field, adjust as needed
    vaqti = models.DateTimeField()
    text = models.TextField(max_length=255)  # Set the maximum length for the text field
    desc = models.TextField()
    status = models.BooleanField(default=True)  # Example for a boolean status field, adjust as needed
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

class JobApplication(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    resume = models.FileField(upload_to='static/main/resum ')
    work = models.ForeignKey(Work, on_delete=models.SET_NULL, blank=True, null=True )