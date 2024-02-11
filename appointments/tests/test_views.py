from django.test import TestCase
from ..models import Appointment
from user.models import UserAccount
from django.contrib.auth import get_user_model
User = get_user_model()



class AppointmentListViewTest(TestCase):
    @classmethod
    def setUp(self) -> None:

        test_user = User.objects.create(email='test_user@gmail.com', name='Test User', password='1234', phone=None, address=None, years=20, image=None, is_dentist=False)
        test_user.save()

        dentist = UserAccount.objects.create(email='dent1@gmail.com', name='dent', password='1234', phone=None, address=None, years=10, image=None, is_dentist=True)
        patient = UserAccount.objects.create(email='timtom@gmail.com', name='Tim Tom', password='1234', phone=None, address=None, years=20, image=None, is_dentist=False)
        

        Appointment.objects.create(
            title='Teeth lookthrough',
            description='It might take long',
            start_date='2024-02-14T16:00:00.000Z',
            end_date='2024-02-14T18:00:00.000Z',
            dentist=dentist,
            patient=patient,
            is_all_day=False,
            recurrence_rule='',
            excluded_dates='',
        )

        Appointment.objects.create(
            title='Tooth removal',
            description='It will not take long',
            start_date='2024-02-14T16:00:00.000Z',
            end_date='2024-02-14T17:00:00.000Z',
            dentist=dentist,
            patient=patient,
            is_all_day=False,
            recurrence_rule='',
            excluded_dates='',
        )


    def test_logged_in_user_can_retrive_all_appointments(self):
        login = self.client.login(email='test_user@gmail.com', password='1234')

        response = self.client.get('/api/appointments/all')

        self.assertEqual(str(response.context['user']), 'test_user@gmail.com')
        self.assertEqual(response.status_code, 200)
        