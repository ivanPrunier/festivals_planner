from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=510)


class Festival(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=510)
    start_date = models.DateField()
    end_date = models.DateField()
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
    
class Stage(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510)
    
    
class FestivalShow(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()