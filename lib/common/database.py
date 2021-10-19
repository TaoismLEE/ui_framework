# -*- coding:utf-8 -*-
import pymssql  # SQL Server module
import pymysql  # MySQL server module
from lib.common.log import logger
from lib.common.parse_file import ParseYaml

# default DB config of Project
config_obj = ParseYaml('project.yml')
project_config = config_obj.get_yaml_dict()
db_host = project_config['DB_HOST']
db_port = int(project_config['DB_PORT'])
db_user = project_config['DB_USER_NAME']
db_password = project_config['DB_USER_PASSWORD']
db_database_name = project_config['DB_DBNAME']


class SqlDriver(object):
    def __init__(self, host=db_host, port=db_port, user=db_user, password=db_password, database=db_database_name):
        """
        Constructor, default querying project database
        :param host: string, ip address
        :param port: int
        :param user: string
        :param password: string
        :param database: string
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    # Execute SQL Server Query
    def exec_mssql(self, sql):
        try:
            conn = pymssql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset="uft8")

            cur = conn.cursor()
            if cur:
                logger.info(u"Execute SQL Statement |%s|" % sql)
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) == 0:
                    logger.warning(u"No SQL Query Data Returned!")
                return rows
            else:
                logger.error(u"Failed to Connect SQL Server Database!")
        except Exception as e:
            logger.error(e)
        finally:
            conn.close()

    # Execute MySQL Query
    def exec_mysql(self, sql):
        try:

            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset='utf8')
            cur = conn.cursor()
            if cur:
                logger.info(u"Execute SQL Statement |%s|" % sql)
                cur.execute(sql)
                rows = cur.fetchall()
                if len(rows) == 0:
                    logger.warning(u"No SQL Query Data Returned!")
                return rows
            else:
                logger.error(u"Failed to Connect MySQL Database!")
        except Exception as e:
            logger.error(e)
        finally:
            conn.close()
