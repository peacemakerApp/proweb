from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core import serializers

from .models import Campany
import csv
from pprint import pprint as pp

def index(request):
    row_number = 0
    with open('frozenb2b_all.csv', newline='', encoding='latin-1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        i = 0
        for row in spamreader:
            if i != 0:   
                activity = row[18].split(',')
                activity = [x for x in activity if x != '']
                prodf = row[6].split(',')
                prodnf = row[7].split(',')
                all_prodcust = prodf + prodnf
                all_prodcust = [x for x in all_prodcust if x != '']
                type_campan = row[17].split(',')
                type_campan = [x for x in type_campan if x != '']
                for act in activity:
                    for prod in all_prodcust:
                        for tp in type_campan:
                            camp = Campany()                
                            camp.company_fich = row[0]
                            camp.company_name = row[1]
                            camp.address = row[2]
                            camp.state = row[3]
                            camp.country = row[4]
                            camp.postal = row[5]
                            camp.products = prod  # row[6]
                            camp.city = row[8]
                            camp.brands = row[9]
                            camp.certificate = row[10]
                            camp.certifications = row[11]
                            camp.url = row[12]
                            camp.telephone_1 = row[13]                    
                            camp.telephone_2 = row[14]
                            camp.fax = row[15]
                            camp.bus_area = row[16]
                            camp.type_camp = tp  # row[17]
                            camp.activity = act
                            camp.turnover = "Null"
                            camp.save()
                            # data = serializers.serialize('json', camp)
                            
                            row_number = row_number + 1            
            i = i + 1
            # output = "Finished with {} row and serialize object {}".format(row_number, data)                                
    return HttpResponse(row_number)
