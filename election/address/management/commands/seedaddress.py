from django.core.management.base import BaseCommand
import random
import faker.providers
from faker import Faker
from address.models import Province,District,Municipality,Ward
import json
import datetime
with open('address/management/commands/address.json', 'r') as f:
    my_json_obj = json.load(f)

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        i=0
        for key, value in my_json_obj:
            name = my_json_obj[i][key]
            print(name)
            #insert in form table
            province = Province.objects.create(
                name=name, 
                display_order=random.choice([1, 4,3, 5, 6,2, 7]),
                created_at = datetime.datetime.now(),
                updated_at = datetime.datetime.now(),
                status="Active")
            print(province.id)
            for district in my_json_obj[i]["districts"]:
                #insert in districts table
                print(district["name"])
                newdistrict=District.objects.create(
                    name=district["name"],
                    coordinate=district["coordinate"],
                    display_order=random.choice([1, 4,3, 5, 6,2, 7]),
                    province = province,
                    created_at = datetime.datetime.now(),
                    updated_at = datetime.datetime.now(),
                    status="Active")
                
                for municipality in district["municipality"]:
                    #insert in option table
                    print(municipality["name"])
                    newmunicipality=Municipality.objects.create(
                        name=municipality["name"], 
                        coordinate=municipality["coordinate"],
                        display_order=i,
                        district = newdistrict,
                        created_at = datetime.datetime.now(),
                        updated_at = datetime.datetime.now(),
                        status="Active")
                    for ward in municipality["wards"]:
                        print(ward)
                        newward= Ward.objects.create(
                            ward_number=ward, 
                            display_order=i,
                            municipality = newmunicipality,
                            created_at = datetime.datetime.now(),
                            updated_at = datetime.datetime.now(),
                            status="Active"
                        )
            i=i+1

        