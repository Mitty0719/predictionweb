#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
import csv

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PredictionService.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#db에 데이터 넣기
# os.chdir(".")
# print("Current dir=", end=""), print(os.getcwd())
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print("BASE_DIR=", end=""), print(BASE_DIR)
#
# sys.path.append(BASE_DIR)
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PredictionService.settings")    # 1. 여기서 프로젝트명.settings입력
# django.setup()
 #
 # # 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과
 #
# from cardUse.models import CardUsedata    # 2. App이름.models
#
# CSV_PATH = 'C:/Users/sprou/Documents/src/usecard.csv'    # 3. csv 파일 경로
#
# with open(CSV_PATH, newline='') as csvfile:    # 4. newline =''
    # data_reader = csv.DictReader(csvfile)
    #
    # for row in data_reader:
        # print(row)
        # CardUsedata.objects.create(        # 5. class명.objects.create
            # # use_seq = row['idx'],
            # use_date = row['date'],
            # use_loc = row['loc'],
            # use_ctg = row['ctg'],
            # use_ctg_detail = row['ctg_detail'],
            # use_age = row['age'],
            # # gen = row['gen'],
            # use_pay = row['pay'],
             # # 6
        # )