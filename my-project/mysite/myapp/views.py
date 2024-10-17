from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
#def index_page(request):
#    return render(request, 'index.html')

def index_page(request):
    start_time = datetime.strptime("6:00", "%H:%M")
    time_labels = [(start_time + timedelta(hours=i)).strftime("%H:%M") for i in range(17)]  # From 6:00 to 19:00

    tasks = [
        {'time': time_label, 'task': ''} for time_label in time_labels
    ]

    # Example predefined tasks
    # tasks[0]['task'] = 'Wake up'
    # tasks[1]['task'] = 'Stretching, Breakfast, Run'
    # tasks[2]['task'] = ''
    # tasks[3]['task'] = 'School'
    # tasks[4]['task'] = 'Learning'
    # tasks[12]['task'] = 'Dinning'

    return render(request, 'index.html', {'tasks': tasks})