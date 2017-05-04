#!/usr/bin/env python3
#models.py
#
# Copyright 2017 José Lopes de Oliveira Jr.
#
# Use of this source code is governed by a MIT-like
# license that can be found in the LICENSE file.
##


'''Tesla's database models.'''

__author__ = 'José Lopes de Oliveira Jr.'


from datetime import datetime

from app.database import db


class Packet(db.Model):
    __tablename__ = 'Packets'
    id = db.Column(db.BigInteger, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    length = db.Column(db.Integer)
    ip_src = db.Column(db.String(128))
    ip_src_geo = db.Column(db.String(2))
    ip_dst = db.Column(db.String(128))
    ip_dst_geo = db.Column(db.String(2))
    transport_proto = db.Column(db.String(10))
    transport_sport = db.Column(db.Integer)
    transport_dport = db.Column(db.Integer)

    def __init__(self, d, l, ips, ipsg, ipd, ipdg, tp, tsp, tdp):
        self.date = d
        self.length = l
        self.ip_src = ips
        self.ip_src_geo = ipsg
        self.ip_dst = ipd
        self.ip_dst_geo = ipdg
        self.transport_proto = tp
        self.transport_sport = tsp
        self.transport_dport = tdp

    def __repr__(self):
        return '<Packet lenght: {}>'.format(self.length)

