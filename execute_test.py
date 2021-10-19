# -*- coding:utf-8 -*-

import unittest
import sys
import time
# to fix embedded version of python bug
# sys.path.append("C:\\Users\yuliy\\edms-automation")

from HTMLTestRunner import HTMLTestRunner

from conf.global_var import PROJECT_PATH
from lib.common.send_email import SendMail
from scripts.YCJ_login import YcjLogin
from scripts.YCJ_create_project import YcjCreateProject


if __name__ == "__main__":
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    report_file = PROJECT_PATH + "/report/" + current_time + "_automation_test_report.html"
    report = open(report_file, "wb")

    total_suite = unittest.TestSuite()
    total_suite.addTest(YcjLogin("testYcjLogin"))
    # total_suite.addTest(YcjCreateProject("testYcjCreateProject"))

    '''trigger to run scripts'''
    runner = HTMLTestRunner(stream=report, title="Automation Test Report", description="Project description")
    result = runner.run(total_suite)
    report.close()

    # currently support sending email to TencentEnterprise mailbox, TencentQQ mailbox and NetEase 163 mailbox
    # TencentEnterprise mailbox: TE
    # TencentQQ mailbox: QQ
    # NetEase 163 mailbox: 163
    # OutLook mailbox: outlook
    obj_email = SendMail(report_file, "outlook")
    obj_email.send_email()
