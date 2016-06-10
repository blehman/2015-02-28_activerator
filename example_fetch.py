#!/usr/bin/env python
import pprint
import requests
import ConfigParser
import mysql.connector
from datetime import datetime
from time import gmtime, strftime
import json

config = ConfigParser.RawConfigParser()
config.read('config.cfg')
client_id = config.get('creds','client_id')
client_secret = config.get('creds','client_secret')
access_token = config.get('creds','access_token')
header = {
    'Authorization': 'Bearer {}'.format(access_token)
}
rds_db = config.get('rds','DB_instance')
rds_usr = config.get('rds','user_name')
rds_pswd = config.get('rds','pasword')


def make_request(p,access_token,endpoint):
    return requests.get(
            config.get('creds','url')+endpoint
            , params=p
            , headers = header
        ).json()

#current_date = datetime.strftime(datetime.utcnow(), '%Y-%m-%d')+ 'T00:00:00Z'
current_date = '2016-03-03'
endpoint = 'segments/636162/all_efforts'
parameters = {
    'per_page': 10
    , 'start_date_local': current_date
    , 'end_date_local':current_date + 'T23:59:59Z'
}


data = make_request(parameters, access_token, endpoint)
with open('data/initial_segment636162_data.json','wb') as result:
    result.write(json.dumps(data))

for item in data:
    pprint.pprint(item)

conn = mysql.connector.connect(
user = 'awsuser_erator'
, password = 'cp9naTY5nrv0nq77p8h3'
, database = 'activerator'
, host = 'activerator-rds.cq5marzdsdnc.us-west-2.rds.amazonaws.com'
)

cur = conn.cursor('dict')

cur.execute(r"""USE activerator;""")
cur.execute(r"""SHOW TABLES;""")
for item in cur:
    print item
cur.execute(r"""DESCRIBE Test;""")
for item in cur:
    print item
conn.close()
conn = mysql.connector.connect(
user = 'awsuser_erator'
, password = 'cp9naTY5nrv0nq77p8h3'
, database = 'activerator'
, host = 'activerator-rds.cq5marzdsdnc.us-west-2.rds.amazonaws.com'
)

cur = conn.cursor('dict')

for item in data:
    AthleteID = item['athlete']['id']
    Distance = item['distance']
    SegmentName = item['segment']['name']
    StartDate = datetime.strptime(item['start_date'],'%Y-%m-%dT%H:%M:%SZ')
    print StartDate
    #StartDate = datetime.strftime(datetime(item['start_date']), '%Y-%m-%dT%H:%M:%SZ')
    MovingTime = item['moving_time']
    ElapsedTime = item['elapsed_time']
    cur.execute("INSERT INTO Test VALUES ({}, {}, 'Flag', now(), {}, {});".format(AthleteID, Distance, MovingTime, ElapsedTime))
    conn.commit()

cur.execute(r"""SELECT * FROM Test;""")
for item in cur:
    print item
