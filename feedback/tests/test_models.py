from django.test import TestCase
from ..models import Feedback
from user.models import UserAccount


class FeedbackModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        dentist = UserAccount.objects.create(email='dent1@gmail.com', name='dent', password='1234', phone=None, address=None, years=10, image=None, is_dentist=True)
        patient = UserAccount.objects.create(email='tim tom@gmail.com', name='Tim Tom', password='1234', phone=None, address=None, years=18, image=None, is_dentist=False)

        Feedback.objects.create(text='I am very pleased with the service', created_by=patient, dentist=dentist)



    def test_text_label(self):
        feedback = Feedback.objects.get(id=1)
        field_label = feedback._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')


    def test_text_max_length(self):
        feedback = Feedback.objects.get(id=1)
        max_length = feedback._meta.get_field('text').max_length
        self.assertEqual(max_length, 500)


    def test_dentist_label(self):
        feedback = Feedback.objects.get(id=1)
        field_label = feedback._meta.get_field('dentist').verbose_name
        self.assertEqual(field_label, 'dentist')


    def test_patient_label(self):
        feedback = Feedback.objects.get(id=1)
        field_label = feedback._meta.get_field('created_by').verbose_name
        self.assertEqual(field_label, 'created by')


    def test_object_name_consists_of_text_dentist_and_created_by(self):
        feedback = Feedback.objects.get(id=1)
        expected_object_name = f'Feedback: {feedback.text}, about {feedback.dentist}, created by {feedback.created_by}, {feedback.creation_date_time}'
        self.assertEqual(str(feedback), expected_object_name)