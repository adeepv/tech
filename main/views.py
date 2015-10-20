# -*- coding: utf-8 -*-
from django.shortcuts import render
from libs.ripequery import ripe_get_asn_holder
from django.core.cache import cache

# Create your views here.
from django.shortcuts import render
import datetime
from main.models import AcctBgp,AcctBgp1Day,AcctBgp1Hr,AcctBgp5Mins
from main.forms import DateChartForm
from django.db.models import Sum
from graphos.sources.model import ModelDataSource
from graphos.renderers import gchart,highcharts,yui

def index(request):
    r = {} # result var
    sdate = datetime.date.today()
    ddate = datetime.date.today()
    stime = '00:00:00'
    dtime = '23:59:59'
    vlan = '777'
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

    fsdate = datetime.datetime.combine(sdate,datetime.time(sstime.hour,sstime.minute,sstime.second,0,None))
    fddate = datetime.datetime.combine(ddate,datetime.time(ddtime.hour,ddtime.minute,ddtime.second,0,None))
    #result = AcctBgp5Mins.objects.only().extra(select={'peer_as_s':'CAST(peer_as_src AS CHAR(50))'}).filter(
    #stamp_inserted__gte=datetime.datetime.combine(sdate,datetime.time(sstime.hour,sstime.minute,sstime.second)),
    #stamp_inserted__lte=datetime.datetime.combine(ddate,datetime.time(ddtime.hour,ddtime.minute,ddtime.second)),vlan='777').annotate(Sum('bytes')).order_by('-bytes__sum')
    result = AcctBgp5Mins.objects.raw('SELECT id, CAST(`peer_as_src` AS CHAR(50)) AS `peer_as_s`, CAST(SUM(`bytes`) AS INTEGER) as `bytes__sum`,id FROM `acct_bgp_5mins` WHERE vlan="%s" AND stamp_inserted >= "%s" AND stamp_inserted <= "%s" GROUP BY `peer_as_s` ORDER BY SUM(`bytes`) DESC'%(vlan,fsdate.strftime('%Y-%m-%d %H:%M:%S'),fddate.strftime('%Y-%m-%d %H:%M:%S')))
    data_source = ModelDataSource(result,fields=['peer_as_s', 'bytes__sum'])
    tdata = []
    ii = 0
    for i in data_source.data:
        if ii == 0:
            pass
            #tdata = tdata + [i]
        else:
            asholder = cache.get('asnh%s'%i[0])
            if asholder == None:
                asholder = ripe_get_asn_holder(i[0])
                cache.set('asnh%s'%i[0],asholder,864000)
            tdata = tdata + [['%s - %s'%(i[0],asholder),i[1]]]
        ii = ii + 1
    r['charttitle'] = 'Traffic for vlan %s from %s to %s'%(vlan,fsdate.strftime('%Y-%m-%d %H:%M:%S'),fddate.strftime('%Y-%m-%d %H:%M:%S'))
    r['chartlegend'] = 'By ASN'
    r['chartdata'] = tdata
    return render(request, 'result.html', r)
