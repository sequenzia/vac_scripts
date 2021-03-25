#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

st = 'FL'

ref = 'https://www.cvs.com/immunizations/covid-19-vaccine'
url = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.' + st + '.json?vaccineinfo'

s = requests.Session()
s.headers.update({'referer': ref})

r = s.get(url)
r_data = r.json()['responsePayloadData']['data'][st]

for city_idx, data in enumerate(r_data):

    city_name = data['city']
    city_status = data['status']

    print(city_idx, city_name, city_status)

