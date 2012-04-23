import datetime

from django.db import models

class Place(models.Model):
    
    RATINGS = (
        ('1', u'schlecht'),
        ('2', u'eher schlecht'),
        ('3', u'in Ordnung'),
        ('4', u'gut'),
        ('5', u'super'),
    )
    
    title = models.CharField(u'Name', max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Beschreibung')
    route = models.TextField(u'Wegbeschreibung')
    latitude = models.FloatField(u'Latitude')
    longitude = models.FloatField(u'Longitude')
    landscape = models.CharField(u'Landschaft', max_length=1, choices=RATINGS)
    bbq = models.CharField(u'Grillen', max_length=1, choices=RATINGS)
    swimming = models.CharField(u'Schwimmen', max_length=1, choices=RATINGS)
    privacy = models.CharField(u'Privatsspaehre', max_length=1, choices=RATINGS)
    author = models.CharField(u'Autor', max_length=255)
    image = models.ImageField(u'Bild', upload_to="images/", blank=True, null=True)
    thumb = models.ImageField(u'Bild', upload_to="images/", blank=True, null=True)
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = u'Ort'
        verbose_name_plural = u'Orte'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = datetime.datetime.now()
        self.date_updated = datetime.datetime.now()
        super(Place, self).save(*args, **kwargs)
        
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return unicode("%s: %s" % (self.place, self.body[:60]))