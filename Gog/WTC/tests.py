from django.test import TestCase
import jenkins
import json
def jenkins_api(req):
    jenkins_server_url = "http://127.0.0.1:8080"
    user_id = 'root'
    api_token = '9fb01ce9aa060d9e4702cdc601d05e9f'
    server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    info = server.get_job_info(req)
    data = json.dumps(info)
    print(data)
    # job = server.build_job()
jenkins_api('test')
# Create your tests here.
