import requests
import configuration
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
#response = get_docs()
#print(response.status_code)
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count": 20})
#response = get_logs()
#print(response.status_code)
#print(response.headers)
def get_user_table():
    return requests.post(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_user_table()
print(response.status_code)
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,json=body,headers=data.headers)
#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.json())