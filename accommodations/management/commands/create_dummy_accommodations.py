# your_app/management/commands/create_dummy_accommodations.py
# python manage.py create_dummy_accommodations
from django.core.management.base import BaseCommand
from django.utils import timezone
from accommodations.models import Accommodation, AccommodationType, Accommodation_Image, GPS_Info
from users.models import BusinessUser, User
import random

class Command(BaseCommand):
    help = "Create dummy accommodations"

    def handle(self, *args, **kwargs):
        # 슈퍼유저와 연결된 BusinessUser 가져오기
        superuser = User.objects.filter(is_superuser=True).first()
        if not superuser:
            self.stdout.write(self.style.ERROR("슈퍼유저가 존재하지 않습니다. 먼저 슈퍼유저를 생성해주세요."))
            return

        business_user, created = BusinessUser.objects.get_or_create(user=superuser)

        if created:
            business_user.business_name = "Default Business"
            business_user.business_registration_number = "000-00-00000"
            business_user.save()

        # 더미 데이터 생성
        for i in range(10):
            # Accommodation 생성
            accommodation = Accommodation.objects.create(
                host=business_user,
                name=f"Accommodation {i + 1}",
                phone_number=f"010-1234-56{i:02d}",
                description=f"This is the description for Accommodation {i + 1}.",
                rules="No smoking, No pets allowed",
                average_rating=random.uniform(3.0, 5.0),
                is_active=True,
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )

            # AccommodationType 생성
            AccommodationType.objects.create(
                accommodation=accommodation,
                is_customized=bool(random.getrandbits(1)),
                type_name=random.choice(["Hotel", "Motel", "Apartment", "Hostel"]),
            )

            # GPS_Info 생성
            GPS_Info.objects.create(
                accommodation=accommodation,
                city=f"City {i + 1}",
                states=f"State {i + 1}",
                road_name=f"Road {i + 1}",
                address=f"Address {i + 1}",
                latitude=37.5665 + random.uniform(-0.01, 0.01),  # 서울 근처의 위도
                longitude=126.9780 + random.uniform(-0.01, 0.01),  # 서울 근처의 경도
            )

            # Accommodation_Image 생성
            for j in range(3):  # 이미지 3개씩 추가
                Accommodation_Image.objects.create(
                    accommodation=accommodation,
                    image=f"accommodation_images/dummy_image_{i + 1}_{j + 1}.jpg",
                )

        self.stdout.write(self.style.SUCCESS("10개의 더미 Accommodation 데이터가 성공적으로 생성되었습니다."))
