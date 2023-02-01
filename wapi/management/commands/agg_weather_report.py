from django.core.management.base import BaseCommand
from wapi.models import Weather, WeatherAgg


class Command(BaseCommand):
    help = 'Command to Load weather data to Database from a file or directory of files'

    def handle(self, *args, **options):
        final = {}
        data = Weather.objects.all()
        for row in data:
            year = row.tdate.year
            record = {}
            if row.max_temp:
                record["avg_max_temp"] = [int(row.max_temp)]
            if row.min_temp:
                record["avg_min_temp"] = [int(row.min_temp)]
            if row.amount:
                record["amount"] = [int(row.amount)]

            if record:
                if year not in final:
                    final[year] = {
                        row.station: record
                    }
                else:
                    if row.station not in final[year]:
                        final[year][row.station] = record
                    else:
                        # print("Record Here::", record, year , row.station, final[year][row.station])
                        if record.get("avg_max_temp"):
                            if final[year][row.station].get("avg_max_temp"):
                                final[year][row.station]["avg_max_temp"].append(record.get("avg_max_temp")[0])
                            else:
                                final[year][row.station]["avg_max_temp"] = record.get("avg_max_temp")
                        if record.get("avg_min_temp"):
                            if final[year][row.station].get("avg_min_temp"):
                                final[year][row.station]["avg_min_temp"].append(record.get("avg_min_temp")[0])
                            else:
                                final[year][row.station]["avg_min_temp"] = record.get("avg_min_temp")
                        if record.get("amount"):
                            if final[year][row.station].get("amount"):
                                final[year][row.station]["amount"].append(record.get("amount")[0])
                            else:
                                final[year][row.station]["amount"] = record.get("amount")

        for data in final.keys():
            for cols in final[data].keys():
                record = final[data][cols]
                total_res = sum(record['amount'])
                avg_max_temp = sum(record['avg_max_temp'])/len(record['avg_max_temp'])
                avg_min_temp = sum(record['avg_min_temp'])/len(record['avg_min_temp'])
                print(f"Checking : Total : {total_res}, Avg Max Temp : {avg_max_temp}, Avg Min Temp : {avg_min_temp}")
                WeatherAgg.objects.create(
                    year=data,
                    avg_max_temp=avg_max_temp,
                    avg_min_temp=avg_min_temp,
                    total=total_res,
                    station=cols
                )
        print("Data Loaded to Weather Status Successfully..")
