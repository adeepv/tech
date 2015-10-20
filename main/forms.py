# -*- coding: utf-8 -*-
from django import forms

from django import forms

class DateChartForm(forms.Form):
    sdt = forms.DateTimeField(label='From:')
    ddt = forms.DateTimeField(label='To:')
    type = forms.ChoiceField(choices=(('5min','5 min'),('1hr','1 hour'),('1day','1 day')))
    vlan = forms.ChoiceField(label='VLAN', choices=(("126",'Dataline UA'),
        ("2755",'Dataline World ACS'),
        ("2768",'Dataline World KCT'),
        ("777",'DTEL-IX'),
        ("556",'Giganet-IX'),
        ("557",'UA-IX'),
        ("872",'Gigatrans-IX'),
        ("929",'Yandex-IX'),
        ("1013",'MailRu-IX'),
        ("1730",'Fiord-IX'),
        ("1740",'Fiord-World'),
        ("2639",'TopNet-UA ACS'),
        ("3317",'TopNet-UA KCT'),
        ("3337",'Google-IX'),
        ("3332",'Internal UANG-SMF'),
        ("2715",'Multicast Kiev-SMF')
                                                    ))


