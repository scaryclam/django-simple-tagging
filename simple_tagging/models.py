from django.db import models
from django.contrib.contenttypes import generic


class Tag(models.Model):
    tag = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class TagMixin(models.Model):
    tags = generic.GenericRelation(Tag)

    def get_tags(self):
        return tags

    def add_tag(self, tag_name):
        new_tag = Tag.objects.create(tag=new_tag, content_object=self)
        


