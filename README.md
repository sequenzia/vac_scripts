# COVID-19 Vaccine Availability

These scripts check the availability of vaccines at pharmacies and sends email alerts.

Currently I only have the CVS scripts working.

## CVS Info:

These scripts check this URL : https://www.cvs.com/immunizations/covid-19-vaccine

[list_cities](cvs/list_cities.py) : This is a basic script that just checks all the cities in your state and prints the results.

[run_alerts](cvs/run_alerts.py) : This script checks for updates to the availability and sends an email with a link. Hopefully, you should be able to sign-up for an appointment.

Just change the relevant information in the settings section.

The required settings:

    eml_config = {'sender': '',
                  'password': '',
                  'recipient': '',
                  'smtp_server': '',
                  'ssl_port': 465}

    alert_st = 'FL'
    alert_cities = ['ORLANDO', 'WINTER PARK', 'JACKSONVILLE']
    alert_secs = 60

** It will only send an email if a city in the *alert_cities* list has availability.

** The *alert_secs* variable changes the frequency of how often the site will be checked. I wouldn't go too low on that.

** If you use gmail, you need to make sure "less secure apps" is turned on for the sending account: (https://myaccount.google.com/lesssecureapps)

You can ping me if you have any questions: steve@sequenzia.com
