from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=255)
    

    class Meta:
        abstract = True


class TagMixin(models.Model):
    def get_tags(self):
        pass

