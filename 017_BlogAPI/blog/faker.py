'''
    # https://faker.readthedocs.io/en/master/
    $ pip install faker # install faker module
    python manage.py flush # delete all exists data from db. dont forget: createsuperuser
    python manage.py shell
    from todo.faker import run
    run()
    exit()
'''

from faker import Faker
from .models import Category, Post
from django.contrib.auth.models import User


def run():
    fake = Faker()
    categories = ('Travel', 'Food', 'Sport', 'Economy')

    for category in categories:
        new_category = Category.objects.create(name=category)
        for _ in range(50):
            Post.objects.create(
                title=fake.sentence(),
                content=fake.text(),
                category=new_category,
                user=User.objects.first()

            )

        print('Finished')
