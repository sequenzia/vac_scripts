#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import requests
import threading
import smtplib
import ssl
from email.message import EmailMessage

# region: ..... settings .....

eml_config = {'sender': 'steve@sequenzia.com',
              'password': '',
              'recipient': 'sequenzia@gmail.com',
              'smtp_server': 'smtp.gmail.com',
              'ssl_port': 465,
              'context': ssl.create_default_context()}

alert_st = 'FL'
alert_cities = ['ORLANDO', 'WINTER PARK', 'JACKSONVILLE']
alert_secs = 60

# endregion:

ref = 'https://www.cvs.com/immunizations/covid-19-vaccine'
url = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.' + alert_st + '.json?vaccineinfo'

def run_alerts(alert_secs=alert_secs, alert_st=alert_st, ref=ref, url=url):

    print('Checking Availability... \n')

    threading.Timer(alert_secs, run_alerts).start()

    s = requests.Session()
    s.headers.update({'referer': ref})

    r = s.get(url)
    r_data = r.json()['responsePayloadData']['data'][alert_st]

    for city_idx, data in enumerate(r_data):

        city_name = data['city']
        city_status = data['status']

        if city_name in alert_cities and city_status == 'Available':
            msg = send_email(alert_st, city_name, city_status)
            print(msg, '\n')

def send_email(alert_st, city_name, city_status, config=eml_config):

    msg_body = 'State: ' + alert_st
    msg_body += '\n'
    msg_body += 'City: ' + city_name
    msg_body += '\n'
    msg_body += 'Status: ' + city_status

    msg = EmailMessage()
    msg.set_content(msg_body)

    msg['Subject'] = 'CVS Update: ' + city_name + ', ' + alert_st + ' - ' + city_status
    msg['From'] = config['sender']
    msg['To'] = config['recipient']

    with smtplib.SMTP_SSL(config['smtp_server'], config['ssl_port'], context=config['context']) as server:

        server.login(config['sender'], config['password'])
        server.send_message(msg)
        server.quit()

    return msg_body

if __name__ == "__main__":
    run_alerts()



