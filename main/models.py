# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

class AcctBgp(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    agent_id = models.IntegerField()
    class_id = models.CharField(max_length=16)
    iface_in = models.IntegerField()
    iface_out = models.IntegerField()
    vlan = models.IntegerField()
    peer_as_src = models.IntegerField()
    peer_as_dst = models.IntegerField()
    peer_ip_src = models.CharField(max_length=15)
    peer_ip_dst = models.CharField(max_length=15)
    as_src = models.IntegerField()
    as_dst = models.IntegerField()
    ip_src = models.CharField(max_length=15, blank=True)
    ip_dst = models.CharField(max_length=15, blank=True)
    src_net = models.CharField(max_length=15, blank=True)
    dst_net = models.CharField(max_length=15, blank=True)
    packets = models.IntegerField()
    bytes = models.BigIntegerField()
    flows = models.IntegerField()
    stamp_inserted = models.DateTimeField()
    stamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acct_bgp'


class AcctBgp1Day(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    agent_id = models.IntegerField()
    class_id = models.CharField(max_length=16)
    vlan = models.IntegerField()
    iface_in = models.IntegerField()
    iface_out = models.IntegerField()
    peer_as_src = models.IntegerField()
    peer_as_dst = models.IntegerField()
    peer_ip_src = models.CharField(max_length=15)
    peer_ip_dst = models.CharField(max_length=15)
    as_src = models.IntegerField()
    as_dst = models.IntegerField()
    ip_src = models.CharField(max_length=15, blank=True)
    ip_dst = models.CharField(max_length=15, blank=True)
    src_net = models.CharField(max_length=15, blank=True)
    dst_net = models.CharField(max_length=15, blank=True)
    packets = models.IntegerField()
    bytes = models.BigIntegerField()
    flows = models.IntegerField()
    stamp_inserted = models.DateTimeField()
    stamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acct_bgp_1day'


class AcctBgp1Hr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    agent_id = models.IntegerField()
    class_id = models.CharField(max_length=16)
    vlan = models.IntegerField()
    iface_in = models.IntegerField()
    iface_out = models.IntegerField()
    peer_as_src = models.IntegerField()
    peer_as_dst = models.IntegerField()
    peer_ip_src = models.CharField(max_length=15)
    peer_ip_dst = models.CharField(max_length=15)
    as_src = models.IntegerField()
    as_dst = models.IntegerField()
    ip_src = models.CharField(max_length=15, blank=True)
    ip_dst = models.CharField(max_length=15, blank=True)
    src_net = models.CharField(max_length=15, blank=True)
    dst_net = models.CharField(max_length=15, blank=True)
    packets = models.IntegerField()
    bytes = models.BigIntegerField()
    flows = models.IntegerField()
    stamp_inserted = models.DateTimeField()
    stamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acct_bgp_1hr'


class AcctBgp5Mins(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    agent_id = models.IntegerField()
    class_id = models.CharField(max_length=16)
    vlan = models.IntegerField()
    iface_in = models.IntegerField()
    iface_out = models.IntegerField()
    peer_as_src = models.IntegerField()
    peer_as_dst = models.IntegerField()
    peer_ip_src = models.CharField(max_length=15)
    peer_ip_dst = models.CharField(max_length=15)
    as_src = models.IntegerField()
    as_dst = models.IntegerField()
    ip_src = models.CharField(max_length=15, blank=True)
    ip_dst = models.CharField(max_length=15, blank=True)
    src_net = models.CharField(max_length=15, blank=True)
    dst_net = models.CharField(max_length=15, blank=True)
    packets = models.IntegerField()
    bytes = models.BigIntegerField()
    flows = models.IntegerField()
    stamp_inserted = models.DateTimeField()
    stamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acct_bgp_5mins'
