
from time import gmtime, strftime

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

current_date = datetime.date.now().date()
endpoint = 'segments/636162/all_efforts'
parameters = {
    'per_page': 10
    , 'start_date_local': datetime.datetime.now().date() + 'T00:00:00Z'
    , 'end_date_local':datetime.date + 'T23:59:59Z'
}
#print pp.dumps(make_request(parameters, access_token, endpoint),indent=4)
data = make_request(parameters, access_token, endpoint)
with open('data/initial_segment636162_data.json','wb') as result:
    result.write(json.dumps(data))
