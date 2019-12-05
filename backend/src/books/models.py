from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)    
    author = models.CharField(max_length=60, blank=True, null=True)
    date_of_publish = models.DateField(blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
