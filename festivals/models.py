from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510, blank=True, null=True)

    def __str__(self):
        return self.name


class Festival(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510, blank=True, null=True)

    def __str__(self):
        return self.name


class Show(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name='line_up')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tour')
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='shows')
    name = models.CharField(max_length=255, null=True, blank=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.artist} presents {self.name}' if self.name else f'{self.artist}'
