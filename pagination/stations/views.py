from django.shortcuts import render
import csv
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


STATION_DATA = []

def bus_stations(request):
    # Load Data
    if not STATION_DATA:
        load_csv_data()

    # Pagination with 10 stations per page
    paginator = Paginator(STATION_DATA, 10)
    page_number = request.GET.get('page', 1)
    try:
        stations = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        stations = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        stations = paginator.page(paginator.num_pages)
    return render(request, 'stations/index.html', {'bus_stations': stations})


def load_csv_data():
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        global STATION_DATA
        STATION_DATA = list(csv.DictReader(csvfile, delimiter=',', quotechar='"',))

