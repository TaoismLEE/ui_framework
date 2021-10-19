# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from bs4 import BeautifulSoup
from conf.global_var import *
from lib.common.log import logger


class SendMail(object):
    def __init__(self, report_file, email_type, send_mail_always=True):
        """
        Constructor
        :param report_file: absolute path of html report file
        :param send_mail_always: if False, send mail only when test case fail; if True, send mail always
        """
        self.report_file = report_file
        self.send_mail_always = send_mail_always
        self.email_type = email_type

    def send_email(self):
        """
        parse report file, then send mail
        :return: N/A
        """
        ret_code = self.parse_report_html()
        if self.send_mail_always or ret_code != 0:
            if self.email_type == "TE":
                self.set_tencent_enterprise_email(ret_code)
            elif self.email_type == "QQ":
                self.set_qq_email(ret_code)
            elif self.email_type == "163":
                self.set_163_email(ret_code)
            elif self.email_type == "outlook":
                self.set_outlook_email(ret_code)

    def set_tencent_enterprise_email(self, ret_code):
        """
        set email service, attachment, etc
        :param ret_code: return code from parse_report_html
        :return: N/A
        """
        try:
            # third party SMTP service
            mail_host = MAIL_HOST
            mail_port = MAIL_PORT
            mail_user = MAIL_USER
            mail_pwd = MAIL_PWD
            sender = MAIL_SENDER
            receivers = MAIL_RECEIVERS

            # email attachment
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = ";".join(receivers)
            if ret_code == 0:
                subject = '全部成功√√√{}'.format(MAIL_SUBJECT)
            elif ret_code == 10010:
                subject = '解析报告失败！！！{}'.format(MAIL_SUBJECT)
            else:
                subject = '失败用例数：{}！！！{}'.format(ret_code, MAIL_SUBJECT)
            message['Subject'] = Header(subject, 'utf-8')

            # email body
            message.attach(MIMEText('附件为{}，请查收!'.format(MAIL_SUBJECT), 'plain', 'utf-8'))

            # email attachment
            att1 = MIMEText(open(self.report_file, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="automation_test_report.html"'
            message.attach(att1)

            obj_smtp = smtplib.SMTP()
            obj_smtp.connect(mail_host, mail_port)
            obj_smtp.login(mail_user, mail_pwd)
            obj_smtp.sendmail(sender, receivers, message.as_string())
            logger.info("Pass to send email!")

        except Exception as e:
            logger.error(e)

        finally:
            obj_smtp.quit()

    def set_qq_email(self, ret_code):
        """
        set email service, attachment, etc
        :param ret_code: return code from parse_report_html
        :return: N/A
        """
        try:
            # third party SMTP service
            mail_host = MAIL_HOST
            mail_port = MAIL_PORT
            mail_user = MAIL_USER
            mail_pwd = MAIL_PWD
            sender = MAIL_SENDER
            receivers = MAIL_RECEIVERS

            # email attachment
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = ";".join(receivers)
            if ret_code == 0:
                subject = '全部成功√√√{}'.format(MAIL_SUBJECT)
            elif ret_code == 10010:
                subject = '解析报告失败！！！{}'.format(MAIL_SUBJECT)
            else:
                subject = '失败用例数：{}！！！{}'.format(ret_code, MAIL_SUBJECT)
            message['Subject'] = Header(subject, 'utf-8')

            # email body
            message.attach(MIMEText('附件为{}，请查收!'.format(MAIL_SUBJECT), 'plain', 'utf-8'))

            # email attachment
            att1 = MIMEText(open(self.report_file, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="automation_test_report.html"'
            message.attach(att1)

            obj_smtp = smtplib.SMTP_SSL(mail_host, mail_port)
            obj_smtp.login(mail_user, mail_pwd)
            obj_smtp.sendmail(sender, receivers, message.as_string())
            logger.info("Pass to send email!")

        except Exception as e:
            logger.error(e)

        finally:
            obj_smtp.quit()

    def set_163_email(self, ret_code):
        """
        set email service, attachment, etc
        :param ret_code: return code from parse_report_html
        :return: N/A
        """
        try:
            # third party SMTP service
            mail_host = MAIL_HOST
            mail_port = MAIL_PORT
            mail_user = MAIL_USER
            mail_pwd = MAIL_PWD
            sender = MAIL_SENDER
            receivers = MAIL_RECEIVERS

            # email attachment
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = ";".join(receivers)
            if ret_code == 0:
                subject = '全部成功√√√{}'.format(MAIL_SUBJECT)
            elif ret_code == 10010:
                subject = '解析报告失败！！！{}'.format(MAIL_SUBJECT)
            else:
                subject = '失败用例数：{}！！！{}'.format(ret_code, MAIL_SUBJECT)
            message['Subject'] = Header(subject, 'utf-8')

            # email body
            message.attach(MIMEText('附件为{}，请查收!'.format(MAIL_SUBJECT), 'plain', 'utf-8'))

            # email attachment
            att1 = MIMEText(open(self.report_file, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="automation_test_report.html"'
            message.attach(att1)

            obj_smtp = smtplib.SMTP_SSL(mail_host, mail_port)
            obj_smtp.login(mail_user, mail_pwd)
            obj_smtp.sendmail(sender, receivers, message.as_string())
            logger.info("Pass to send email!")

        except Exception as e:
            logger.error(e)

        finally:
            obj_smtp.quit()

    def set_outlook_email(self, ret_code):
        """
        set email service, attachment, etc
        :param ret_code: return code from parse_report_html
        :return: N/A
        """
        try:
            # third party SMTP service
            mail_host = MAIL_HOST
            mail_port = MAIL_PORT
            # mail_user = MAIL_USER
            # mail_pwd = MAIL_PWD
            sender = MAIL_SENDER
            receivers = MAIL_RECEIVERS

            # email attachment
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = ";".join(receivers)
            if ret_code == 0:
                subject = '全部成功√√√{}'.format(MAIL_SUBJECT)
            elif ret_code == 10010:
                subject = '解析报告失败！！！{}'.format(MAIL_SUBJECT)
            else:
                subject = '失败用例数：{}！！！{}'.format(ret_code, MAIL_SUBJECT)
            message['Subject'] = Header(subject, 'utf-8')

            # email body
            message.attach(MIMEText('附件为{}，请查收!'.format(MAIL_SUBJECT), 'plain', 'utf-8'))

            # email attachment
            att1 = MIMEText(open(self.report_file, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="UI_automation_test_report.html"'
            message.attach(att1)

            obj_smtp = smtplib.SMTP(mail_host, mail_port)
            obj_smtp.starttls()
            # obj_smtp.login(mail_user, mail_pwd)
            obj_smtp.sendmail(sender, receivers, message.as_string())
            logger.info("Pass to send email!")

        except Exception as e:
            logger.error(e)

        finally:
            obj_smtp.quit()

    def parse_report_html(self):
        """
        judging whether all test cases PASS
        :return: return code, num_fail_cases or 10010 - parsing html file fail
        """
        try:

            with open(self.report_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                ret = soup.select('tr#total_row td')
                # number of cases marked as fail or error
                num_fail_case = int(ret[3].text.strip()) + int(ret[4].text.strip())
                return num_fail_case

        except Exception as e:
            logger.error(e)
            return 10010


if __name__ == '__main__':
    obj_mail = SendMail(PROJECT_PATH + '/report/automation_test_report.html')
    obj_mail.send_email()
