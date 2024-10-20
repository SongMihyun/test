# python manage.py create_dummy_users

import random
from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

class Command(BaseCommand):
    help = 'Creates 10 dummy users'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=70)
            gender = random.choice(['male', 'female', 'other'])
            user_type = random.choice(['guest', 'host', 'admin'])

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                birth_date=birth_date,
                gender=gender,
                user_type=user_type,
                password='password123'  # 각 유저에게 동일한 기본 비밀번호 설정
            )
            user.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 dummy users'))
