import jenkins
import json
import time
def jenkins_update(req):
    datetime = time.strftime('%Y%m%d', time.localtime(time.time()))
    req = str(req)
    jenkins_server_url = "http://115.236.182.186:18080/"
    user_id = 'admin'
    api_token = '24e78c29c3a6c0ee886413403d4a2fa2'
    server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    try:
        last_build_num = server.get_job_info(req)['lastBuild']['number'] #最后一次job构建序号
        new_build_num = int(last_build_num) + 1 #新准备构建序号
        server.build_job(req,  parameters={'datetime':datetime}) #构建job
    except jenkins.NotFoundException as e:
        warn_info = str(e) + '\n'+ "请查看项目与jenkins job_name是否正确"
        warn_info = str(warn_info)
        return warn_info

def jenkins_rollback(jobname, datetime):
    job_name = str(jobname)
    datetime = str(datetime)
    jenkins_server_url = "http://115.236.182.186:18080/"
    user_id = 'admin'
    api_token = '24e78c29c3a6c0ee886413403d4a2fa2'
    server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    try:
        last_build_num = server.get_job_info(job_name)['lastBuild']['number'] #最后一次job构建序号
        new_build_num = int(last_build_num) + 1 #新准备构建序号
        server.build_job(job_name,  parameters={'datetime':datetime}) #构建job
    except jenkins.NotFoundException as e:
        warn_info = str(e) + '\n'+ "请查看项目与jenkins job_name是否正确"
        warn_info = str(warn_info)
        return warn_info







