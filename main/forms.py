# -*- coding: utf-8 -*-
from django import forms

from django import forms

class DateChartForm(forms.Form):
    start_date = forms.DateField(label='Sdate')
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    end_date = forms.DateField(label='Edate')
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    type = forms.ChoiceField(choices=('5min','1hr','1day'))


