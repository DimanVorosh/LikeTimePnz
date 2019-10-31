#!./env/bin/python3

import hashlib
import datetime

from models.settings import set_settings
from models.user import User
from models.personal_data import PersonalData
from libs.logger import logger
from config import config


logger.info('Creating default settings..')

settings_list = {
    'first_payment_amount': '99',
    'first_payment_at': '02:25',
    'first_payment_count': '5',
    'first_payment_period': '1',
    'payment_period': '1',
    'payment_amount': '299',
    'payment_at': '03:00',
    'payment_count': '5'
}

for key, value in settings_list.items():

    set_settings(key, value)

logger.success('Default settings created')

logger.info('Creating defaultuser..')

user = User()

user.email = 'admin@finicom.ru'
user.phone = '+79998422616'
password = 'djnj*A8enn!8eNJEks' + config['secure']['salt_password']
user.password = hashlib.sha256(password.encode()).hexdigest()
user.is_admin = True
user.save()

pd = PersonalData()
pd.personal_first_name = 'Иванов'
pd.personal_second_name = 'Иванов'
pd.personal_middle_name = 'Иванович'
pd.personal_birth_date = datetime.date(1980, 1, 1)
pd.personal_sex = 'male'
pd.passport_series = '0000'
pd.passport_number = '000002'
pd.passport_issue_date = datetime.date(2000, 2, 1)
pd.passport_department_code = '000-001'
pd.passport_birth_place = 'г. Москва'
pd.passport_authority = "ОВД Москвы 'Первое'"
pd.address_main_regions = '1'
pd.address_main_city = 'Москва'
pd.address_main_street = 'Тверская'
pd.address_main_house_number = '1А'
pd.address_main_apartment = '31'
pd.address_main_and_actual_equal = False
pd.address_actual_regions = '1'
pd.address_actual_city = 'Москва'
pd.address_actual_street = 'Ленина'
pd.address_actual_house_number = '2'
pd.address_actual_apartment = '11'
pd.user = user
pd.save()

logger.success('Default user created')
