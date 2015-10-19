# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime
from main.models import AcctBgp,AcctBgp1Day,AcctBgp1Hr,AcctBgp5Mins
from main.forms import DateChartForm
from django.db.models import Sum
from graphos.sources.model import ModelDataSource
from graphos.renderers import gchart

def index(request):
    r = {} # result var
    sdate = datetime.date.today()
    ddate = datetime.date.today()
    stime = '00:00:00'
    dtime = '23:59:59'
    type = '5min'
    if request.method == 'POST':
        form = DateChartForm(request.POST)
        if form.is_valid():
            ddate = form.end_date
            sdate = form.start_date
            stime = form.start_time
            dtime = form.end_time
            type = form.type

    sstime = datetime.datetime.strptime(stime,'%H:%M:%S')
    ddtime = datetime.datetime.strptime(dtime,'%H:%M:%S')

    result = AcctBgp5Mins.objects.values('peer_as_src').filter(stamp_inserted__gte=datetime.datetime.combine(sdate,datetime.time(sstime.hour,sstime.minute,sstime.second)),stamp_inserted__lte=datetime.datetime.combine(ddate,datetime.time(ddtime.hour,ddtime.minute,ddtime.second)),vlan='777').annotate(Sum('bytes')).order_by('-bytes__sum')
    data_source = ModelDataSource(result,
                                  fields=['peer_as_src', 'bytes__sum'])
    chart = gchart.PieChart(data_source)
    r{'chart'} = chart
    return render(request, 'result.html', r)
