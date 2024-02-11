from django.test import TestCase
from ..models import Appointment
from user.models import UserAccount


class AppointmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):        
        dentist = UserAccount.objects.create(email='dent1@gmail.com', name='dent', password='1234', phone=None, address=None, years=10, image=None, is_dentist=True)

        Appointment.objects.create(title='Test appointment', description='Some description', start_date='2024-02-14T18:59:59.999Z', end_date='2024-02-14T21:59:59.999Z', patient=None, dentist=dentist, is_all_day=False, recurrence_rule='', excluded_dates='')


    def test_title_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')


    def test_title_max_length(self):
        appointment = Appointment.objects.get(id=1)
        max_length = appointment._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)


    def test_description_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    
    def test_description_max_length(self):
        appointment = Appointment.objects.get(id=1)
        max_length = appointment._meta.get_field('description').max_length
        self.assertEqual(max_length, 200)


    def test_start_date_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('start_date').verbose_name
        self.assertEqual(field_label, 'start date')


    def test_end_date_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('end_date').verbose_name
        self.assertEqual(field_label, 'end date')


    def test_start_date_is_earlier_than_end_date(self):
        appointment = Appointment.objects.get(id=1)
        start_date = appointment.start_date
        end_date = appointment.end_date
        self.assertLess(start_date, end_date)

    
    def test_dentist_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('dentist').verbose_name
        self.assertEqual(field_label, 'dentist')


    def test_patient_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('patient').verbose_name
        self.assertEqual(field_label, 'patient')


    def test_is_all_day_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('is_all_day').verbose_name
        self.assertEqual(field_label, 'is all day')

    
    def test_recurrence_rule_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('recurrence_rule').verbose_name
        self.assertEqual(field_label, 'recurrence rule')

    
    def test_recurrence_rule_max_length(self):
        appointment = Appointment.objects.get(id=1)
        max_length = appointment._meta.get_field('recurrence_rule').max_length
        self.assertEqual(max_length, 50)

    
    def test_excluded_dates_label(self):
        appointment = Appointment.objects.get(id=1)
        field_label = appointment._meta.get_field('excluded_dates').verbose_name
        self.assertEqual(field_label, 'excluded dates')

    
    def test_excluded_dates_max_length(self):
        appointment = Appointment.objects.get(id=1)
        max_length = appointment._meta.get_field('excluded_dates').max_length
        self.assertEqual(max_length, 400)


    def test_object_name_consists_of_start_date_and_end_date(self):
        appointment = Appointment.objects.get(id=1)
        expected_object_name = f'{appointment.title}, occurs from {appointment.start_date} until {appointment.end_date}'
        self.assertEqual(str(appointment), expected_object_name)