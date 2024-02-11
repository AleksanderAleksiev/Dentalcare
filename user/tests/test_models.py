from django.test import TestCase
from ..models import UserAccount
from django.core.files.uploadedfile import SimpleUploadedFile


class UserAccountModel(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        UserAccount.objects.create(email='user@gmail.com', name='New User', password='1234', phone=None, address=None, years=10, image=None, is_dentist=False)
        UserAccount.objects.create(email='dent@gmail.com', name='Dr. Dent', password='1234', phone=None, address=None, years=15, image=None, is_dentist=True)


    def test_email_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    
    def test_email_max_length(self):
        user = UserAccount.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 40)

    
    def test_name_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    
    def test_name_max_length(self):
        user = UserAccount.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)


    def test_phone_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    
    def test_phone_max_length(self):
        user = UserAccount.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 20)

    
    def test_address_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    
    def test_address_max_length(self):
        user = UserAccount.objects.get(id=1)
        max_length = user._meta.get_field('address').max_length
        self.assertEqual(max_length, 50)

    
    def test_years_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('years').verbose_name
        self.assertEqual(field_label, 'years')

    
    def test_image_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')


    # def test_image_upload(self):
    #     user = UserAccount.objects.get(id=1)
    #     user.image = SimpleUploadedFile(name='test_image.jpg', content=open('media/user/assets/images', 'rb').read(), content_type='image/jpeg')
    #     user.save()
    #     self.assertEqual(user.objects.count(), 1)


    def test_is_active_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('is_active').verbose_name
        self.assertEqual(field_label, 'is active')

    
    def test_is_staff_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('is_staff').verbose_name
        self.assertEqual(field_label, 'is staff')


    def test_is_dentist_label(self):
        user = UserAccount.objects.get(id=1)
        field_label = user._meta.get_field('is_dentist').verbose_name
        self.assertEqual(field_label, 'is dentist')


    def test_object_name_is_appropriate_for_normal_user(self):
        user = UserAccount.objects.get(id=1)
        expected_object_name = f'{user.name}, {user.years}, lives in {user.address}'
        self.assertEqual(str(user), expected_object_name)


    def test_object_name_is_appropriate_for_dentist_user(self):
        dentist = UserAccount.objects.get(id=2)
        expected_object_name = f'{dentist.name}, working as a dentist for {dentist.years}'
        self.assertEqual(str(dentist), expected_object_name)
