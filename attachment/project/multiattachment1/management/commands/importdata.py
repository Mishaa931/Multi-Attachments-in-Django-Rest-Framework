import pandas as pd
from django.apps import apps
from django.core.management.base import BaseCommand
from multiattachment1.serializers import LeaveApplySerializer
from datetime import datetime
from multiattachment1.models import *

class Command(BaseCommand):
    help = 'Import data from a CSV file into a Django model'

    def add_arguments(self, parser):
        parser.add_argument('app_name', help='The name of the Django app')
        parser.add_argument('model_name', help='The name of the model')
        parser.add_argument('file_path', help='The path to the CSV file')

    def handle(self, *args, **options):
        app_name = options['app_name']
        model_name = options['model_name']
        file_path = options['file_path']

        model = apps.get_model('multiattachment1', 'LeaveApply')

        # queryset = model.objects.all()
        # data = list(queryset.values())
        # df = pd.DataFrame(data)
        # df.to_csv('C:/Users/Mishaa/Desktop/leaveapplydata1.csv', index=False)

        
        df = pd.read_csv(file_path,index_col=False)
        print(df.head())
        print(df.dtypes)
        
        df = df.drop(['Unnamed: 0', 'leave_type_id'], axis=1)
        headers= df.columns
        rows = df.to_dict(orient='records')
        print('rows',rows)

        for row in rows:
            rec=model.objects.create(**row)
            print(rec)
            
           
        print('imported!')

