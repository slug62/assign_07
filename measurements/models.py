from django.db import models


class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def number_of_locations(self):
        return len(self.location_set.all())

    def average_measurement(self):
        avg = 0
        locations = self.location_set.all()
        sum = 0
        counter = 0
        for l in locations:
            measurement = l.measurement_set.all()
            if measurement:
                for m in measurement:
                    sum += m.value
                    counter += 1
        if counter != 0:
            avg = sum / counter
        return avg

    def category_names(self):
        catagories = self.category_set.all()
        clist = ""
        for c in catagories:
            clist += c.name + ', '
        return clist

    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    altitude = models.IntegerField(default=0)
    area = models.ForeignKey(Area, on_delete=None)

    def __str__(self):
        return self.area.name + ': ' + self.name


class Measurement(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.FloatField(default=0.0)
    date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=None)

    def __str__(self):
        return 'Measurement@' + self.location.name


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    members = models.ManyToManyField(Area)

    def __str__(self):
        return self.name

