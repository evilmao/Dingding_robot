# -*- coding: utf-8 -*
'''
- 从JERA收集问题，获得问题
'''
import sys
from jira import JIRA
import pycha.pie

reload(sys)
sys.setdefaultencoding('utf8')

def issue_search():
    jira = JIRA('http://192.168.0.21:8080',basic_auth=('name','passwd'))
	#JQL 通过Jira筛选器获得，每次工作流修改需要更改此处！
    issues = jira.search_issues('status in (新建问题, 处理中, 待办, 重新打开, 延迟解决, 新建, 压力测试, "In Review", 开发, 部署, 测试, 验收) \
                                 AND due <= "0" ORDER BY assignee DESC',fields='summary,assignee,description,comment'
                                 )
    return issues

def get_issue():
    issue_list = []
    for issue in issue_search():
        summarys = issue.fields.summary.encode('utf-8')
        users = issue.fields.assignee
        issue =  str(issue) + ","+"@"+format(users) + ","
        issue_list.append(issue)
    s = '\t'.join(issue_list)
    return s

