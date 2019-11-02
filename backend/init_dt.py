from datetime import datetime, timedelta
from random import randrange, randint, choice
import radar

from models.worker import *
from models.meta import Base
from models.activity_log import *


def create_worker(ean13, login, name, surname, middle_name, type):

  worker = Worker()
  worker.ean13 = ean13
  worker.login = login
  worker.password = Worker.generate_worker_password()
  worker.name = name
  worker.surname = surname
  worker.middle_name = middle_name
  worker.type = type
  worker.deleted = False
  worker.save()
  worker.db_session.commit()

  if worker.type == WorkerType.INSPECTOR:
    print(worker.login, worker.password)

  return worker

first_collector = create_worker(
  ean13=1111,
  login="ivan", 
  name="Иван", 
  surname="Иванович", 
  middle_name="Иванов",
  type=WorkerType.COLLECTOR
)

second_collector = create_worker(
  ean13=2222,
  login="petr", 
  name="Петр", 
  surname="Петрович", 
  middle_name="Петров",
  type=WorkerType.COLLECTOR
)

third_collector = create_worker(
  ean13=3333,
  login="anton", 
  name="Антон", 
  surname="Антонович", 
  middle_name="Антонов",
  type=WorkerType.COLLECTOR
)

four_collector = create_worker(
  ean13=4444,
  login="boris", 
  name="Борис", 
  surname="Борисович", 
  middle_name="Борисов",
  type=WorkerType.COLLECTOR
)

five_collector = create_worker(
  ean13=5555,
  login="egor", 
  name="Егор", 
  surname="Егорович",
  middle_name="Егоров",
  type=WorkerType.COLLECTOR
)

six_collector = create_worker(
  ean13=6666,
  login="roman", 
  name="Роман", 
  surname="Романович",
  middle_name="Романов",
  type=WorkerType.COLLECTOR
)

seven_collector = create_worker(
  ean13=7777,
  login="mixail", 
  name="Михаил", 
  surname="Михаилович",
  middle_name="Макаров",
  type=WorkerType.COLLECTOR
)

eight_collector = create_worker(
  ean13=8888,
  login="alexei", 
  name="Алексей", 
  surname="Алексеевич",
  middle_name="Алексеев",
  type=WorkerType.COLLECTOR
)

nine_collector = create_worker(
  ean13=9999,
  login="konstantin", 
  name="Константин", 
  surname="Константинович",
  middle_name="Константинов",
  type=WorkerType.COLLECTOR
)

inspector = create_worker(
  ean13=1010,
  login="denis", 
  name="Денис", 
  surname="Денисович", 
  middle_name="Денисов",
  type=WorkerType.INSPECTOR
)


def make_collect(collector, box_code, datetime):

  activity = ActivityLog()
  activity.local_time = datetime
  activity.server_time = datetime
  activity.box_code = box_code
  activity.type = ActivityType.COLLECT
  activity.payload = collector.ean13
  activity.status = ActivityStatus.SUCCESS
  activity.worker_id = collector.id
  activity.save()
  activity.db_session.commit()


def make_review(reviewer, box_code, payload, datetime):

  activity = ActivityLog()
  activity.local_time = datetime
  activity.server_time = datetime
  activity.box_code = box_code
  activity.type = ActivityType.REVIEW
  activity.payload = payload
  activity.status = ActivityStatus.SUCCESS
  activity.worker_id = reviewer.id
  activity.save()
  activity.db_session.commit()


def generate_datetime():

  date = radar.random_datetime(
    start = datetime(year=2019, month=5, day=1),
    stop = datetime(year=2019, month=12, day=31)
  )

  if date.hour == 0:
    date = generate_datetime()
  
  return date


for i in range(0, 5000):
  date = generate_datetime()
  make_collect(
    collector = choice([first_collector, second_collector, third_collector, four_collector, \
      five_collector, six_collector, seven_collector, eight_collector, nine_collector]),
    box_code = i,
    datetime = date
  )
  make_review(
    reviewer = inspector,
    box_code = i,
    payload = choice([1000, 2000, 3000, 2500, 4000, 3500]),
    datetime = date + timedelta(minutes=5)
  )
