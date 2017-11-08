import jenkins
import json
import time
def jenkins_api(req):
    req = str(req)
    jenkins_server_url = "http://192.168.1.38:8080"
    user_id = 'admin'
    api_token = '24e78c29c3a6c0ee886413403d4a2fa2'
    server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    try:
        last_build_num = server.get_job_info(req)['lastBuild']['number'] #最后一次job构建序号
        new_build_num = int(last_build_num) + 1 #新准备构建序号
        server.build_job(req) #构建job
    except jenkins.NotFoundException as e:
        warn_info = str(e) + '\n'+ "请查看项目与jenkins job_name是否正确"
        warn_info = str(warn_info)
        return warn_info

# print(jenkins_api('www'))


