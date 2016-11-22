from django.db import models

USER_EVENT_CHOICES = (
    ('user:create', 'user:create'),
    ('user:delete', 'user:delete'),
    ('field:create', 'field:create'),
    ('field:update', 'field:update'),
    ('field:delete', 'field:delete'),
    ('planting:create', 'planting:create'),
    ('fertilizing:create', 'fertilizing:create'),
)
NATURE_EVENT_CHOICES = (
    ('rainfall', 'rainfall'),
)


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)


class Field(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)


class UserEvent(models.Model):
    user = models.ForeignKey(User)
    event = models.CharField(choice=USER_EVENT_CHOICES)
    entity = models.CharField(max_length=255)


class NatureEvent(models.Model):
    fields = models.ManyToManyField(Field)
    event = models.CharField(choice=NATURE_EVENT_CHOICES)
    entity = models.CharField(max_length=255)
