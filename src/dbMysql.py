
import json
from types import SimpleNamespace
from pathlib import Path
import diff_data
import logging
from datetime import datetime
from pprint import pprint
import pymysql

import app_logger

logger = app_logger.get_logger(__name__)


class workDb:
    def __init__(self, rc, c_count=None):

        self.mydb = pymysql.connect(host=rc._sections.artix.server_ip,
                                    database=rc._sections.artix.database,
                                    user=rc._sections.artix.user,
                                    passwd=rc._sections.artix.passwd)
        self._mycursor = self.mydb.cursor()  # cursor created

    def get_last_workshift(self):

        l_date = self.load_last_date()
        logger.info('Date of the last closed cash shift - ' + str(l_date))
        try:
            self._mycursor.execute(diff_data.qrSelect_workshift, [l_date])
        except Exception as e:
            logger.info('Get date from DB - ' + str(l_date))
            logger.exception(e, exc_info=True)

        logger.info('Getting data on the last closed cash shifts')
        l_workshift = self._mycursor.fetchall()
        # self._mycursor.close()
        with open('data.json', 'w', encoding='utf-8') as f:
            logging.info('Writing a new date for closed shifts to a file')
            json.dump(l_workshift, f, ensure_ascii=False,
                    indent=4,  default=str)
        # self.mydb.close()

        logging.info('sent workshift for 1C')
        logging.info('workshift - ' + str(l_workshift))

        return l_workshift

    def get_last_workshift_open(self):
        l_date = self.load_last_date_open()
#        logging.info('workshift - ' + str(l_workshift))
        self._mycursor.execute(diff_data.qrSelect_workshift_open, [l_date])
        l_workshift = self._mycursor.fetchall()
        # self._mycursor.close()
        with open('data_open.json', 'w', encoding='utf-8') as f:
            # json_string = json.dumps(l_workshift)
            # pprint(json_string)
            # f.write(json.dumps(l_workshift, ensure_ascii=False, indent=4))
            json.dump(l_workshift, f, ensure_ascii=False,
                    indent=4,  default=str)
        # self.mydb.close()

        logging.info('sent workshift_open for 1C')
        logging.info('workshift_open - ' + str(l_workshift))

        return l_workshift

    def save_last_date(self, t_date):
        filename = '/home/administrator/Workshift_load/src/last_date.txt'
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write(str(t_date))

    def save_last_date_open(self, t_date):
        filename = '/home/administrator/Workshift_load/src/last_date_open.txt'
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write(str(t_date))

    def load_last_date(self):
        logging.info(
            'Reading the file with the date of the last closed cash shift')
        filename = '/home/administrator/Workshift_load/src/last_date.txt'
        with open(filename, 'r', encoding='utf-8') as outfile:
            return (outfile.readline())

    def load_last_date_open(self):
        logging.info(
            'Reading the file with the date of the last openeded cash shift')

        filename = '/home/administrator/Workshift_load/src/last_date_open.txt'
        with open(filename, 'r', encoding='utf-8') as outfile:
            return (outfile.readline())

    def get_last_date(self):

        self._mycursor.execute(diff_data.qrSelect_last_workshift_date)
        l_date = self._mycursor.fetchone()
        logging.info(
            'Getting the date of the last closed cash shift from the database - ' + str(l_date))
        # self.mydb.close()

        return l_date[0]

    def save_new_date(self):
        tl_date = self.get_last_date()
        self.save_last_date(tl_date)

    def save_new_date_open(self):
        tl_date = self.get_last_date_open()
        self.save_last_date_open(tl_date)

    def get_last_date_open(self):

        self._mycursor.execute(diff_data.qrSelect_last_workshift_date_open)
        l_date = self._mycursor.fetchone()
        # self._mycursor.close()
        logging.info(
            'Getting the date of the last opened cash shift from the database - ' + str(l_date))
        # logging.info(
        #      'Cursor closed')

        return l_date[0]

    def close_db_connection(self):
        self._mycursor.close()
        self.mydb.close()
        logging.info('DB is closed!!!')
