from django.db import models

class ShortNames(models.Model):
    link = models.CharField(max_length=250, db_collation='utf8_unicode_ci', blank=True, null=True)
    url = models.TextField()


    class Meta:
        managed = False
        db_table = 'short_names'