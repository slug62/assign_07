from django.db import models


class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def number_of_locations(self):
        return len(Location.objects.filter(area=self.id))

    def average_measurement(self):
        avg = 0
        locations = Location.objects.filter(area=self.id)
        measurement_values = []
        for l in locations:
            measurement_values.append(Measurement.objects.filter(location=l.id))
        for m in measurement_values:
            for i in range(m):
                avg = sum(m[i].value)
        #avg = sum(measurement_values[1].value)
        return avg

    def category_names(self):
        catagories = Category.objects.filter(members=self.id)
        clist = ""
        for c in catagories:
            clist += c.name + ','
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
        return 'Measurement@' + self.location


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    members = models.ManyToManyField(Area)

    def __str__(self):
        return self.name

