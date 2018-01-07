# -*- coding: utf-8 -*
'''
- JIRA逾期汇总
'''
from jira import JIRA
from ConfigData.Userphonelist import userlists

def issue_search():
    jira = JIRA('http://192.168.0.21:8080',basic_auth=('yanbin','yanbin.net'))
    issues = jira.search_issues('status in (\
                                                                                        新建问题, 处理中, Reopened, 待办, \
                                                                                        重新打开, 延迟解决, 新建, 压力测试, 预发布环境测试, 开发, 部署, 开发环境测试, 产品部署, 验) \
                                            AND due <= -1d ORDER BY assignee ASC',
                                            fields='summary,assignee,description,comment'
                                         )
    return issues

def get_issue():
    issue_list = []
    for issue in issue_search():
        summarys = issue.fields.summary
        users = issue.fields.assignee
        issue = str(issue) + ","+ str(summarys)+";"+"经办人:"+format(users)
        issue_list.append(issue)
    s = '\n'.join(issue_list)
    return s

def get_users():
    phonelist = []
    userlist = []
    base_users = userlists
    for issue in issue_search():
        users = format(issue.fields.assignee)
        for i,v in base_users.items():
            if users == i:
                phonelist.append(v)
    l1 = phonelist
    phonelist1 = list(set(l1))
    return phonelist1

