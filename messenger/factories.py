import factory
from factory.django import ImageField

from messenger import models


class UserFactory(factory.django.DjangoModelFactory):
    nickname = factory.Faker('name')
    first_name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    birth_day = factory.Faker('date_of_birth', minimum_age=18, maximum_age=95)

    class Meta:
        model = models.User


class PostFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    post_subject = factory.Faker('sentence')
    post_text = factory.Faker('text')
    created_at = factory.Faker('date_time')

    class Meta:
        model = models.Post
