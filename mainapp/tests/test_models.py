from django.test import TestCase
from django.contrib.auth.models import User
from mainapp.models import *


class BaseTestCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_manager = User.objects.create(
            username='test_user_manager',
            password='password',
            first_name='Иван',
            last_name='Иванов'
        )
        test_user_teacher = User.objects.create(
            username='test_user_teacher',
            password='password',
            first_name='Александра',
            last_name='Александрова'
        )
        test_user_student = User.objects.create(
            username='test_user_student',
            password='password',
            first_name='Петр',
            last_name='Петров'
        )
        cls.test_manager = EducationalManager.objects.create(
            user=test_user_manager,
            middle_name='Иванович',
            gender='m',
            phone='+79100001112',
            city='London',
            date_of_birthday='1990-01-01',
            user_group='manager',
        )
        cls.test_teacher = Teacher.objects.create(
            user=test_user_teacher,
            middle_name='Александровна',
            gender='f',
            phone='+79100001113',
            city='London',
            date_of_birthday='1980-01-01',
            user_group='teacher',
        )
        cls.test_student = Student.objects.create(
            user=test_user_student,
            middle_name='Петрович',
            gender='m',
            phone='+79100001114',
            city='London',
            date_of_birthday='2000-01-01',
            user_group='student',
        )

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCases, cls).tearDownClass()


class ProfilesTestCases(BaseTestCases):

    def test_student_data(self):
        self.assertEqual(self.test_student.user.first_name, 'Петр')
        self.assertEqual(self.test_student.user.last_name, 'Петров')
        self.assertEqual(self.test_student.middle_name, 'Петрович')
        self.assertEqual(self.test_student.phone, '+79100001114')
        self.assertEqual(self.test_student.city, 'London')
        self.assertEqual(self.test_student.date_of_birthday, '2000-01-01')
        self.assertEqual(self.test_student.user_group, 'student')
        self.assertEqual(self.test_student.gender, 'm')

    def test_student_str(self):
        self.assertEqual(self.test_student.__str__(), 'Петр Петров')

    def test_student_fullname(self):
        self.assertEqual(self.test_student.get_fio(), 'Петров Петр Петрович')

    def test_teacher_data(self):
        self.assertEqual(self.test_teacher.user.first_name, 'Александра')
        self.assertEqual(self.test_teacher.user.last_name, 'Александрова')
        self.assertEqual(self.test_teacher.middle_name, 'Александровна')
        self.assertEqual(self.test_teacher.phone, '+79100001113')
        self.assertEqual(self.test_teacher.city, 'London')
        self.assertEqual(self.test_teacher.date_of_birthday, '1980-01-01')
        self.assertEqual(self.test_teacher.user_group, 'teacher')
        self.assertEqual(self.test_teacher.gender, 'f')

    def test_teacher_str(self):
        self.assertEqual(self.test_teacher.__str__(), 'Александра Александрова')

    def test_teacher_fullname(self):
        self.assertEqual(self.test_teacher.get_fio(), 'Александрова Александра Александровна')


class GroupTestCases(BaseTestCases):

    @classmethod
    def setUpTestData(cls):
        super(GroupTestCases, cls).setUpTestData()
        cls.test_group = Group.objects.create(name='test_group', teacher=cls.test_teacher, manager=cls.test_manager)

    def test_add_group_to_student(self):
        self.test_student.group_list.add(self.test_group)
        self.assertIn(self.test_group, self.test_student.group_list.all())

    def test_add_group_to_teacher(self):
        self.test_teacher.group_list.add(self.test_group)
        self.assertIn(self.test_group, self.test_teacher.group_list.all())
