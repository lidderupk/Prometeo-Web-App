import json
import os
import mariadb
from dotenv import load_dotenv
import logging

class metrics(object):
    
    def __init__(self):
        load_dotenv()
        self.logger = logging.getLogger('prometo.newmetric.new_metrics')
        self.logger.debug('creating an instance of metrics')

    def get_allmetrics(self, sensorid, event_date, max_mediciones):
        print("get_allmetrics - entro en la funcion")

        try:
            conn = mariadb.connect(
                user=os.getenv("MARIADB_USERNAME"),
                password=os.getenv("MARIADB_PASSWORD"),
                host=os.getenv("MARIADB_HOST"),
                database="prometeo",
                port=3306)

            cursor = conn.cursor()

            print("get_allmetrics - llamada a sql")
#            cursor.callproc('sp_select_metrics', (sensorid, event_date))
            cursor.callproc('sp_select_metrics', (sensorid, "10,02,2020", max_mediciones))
            print("get_allmetrics - sensorid")
            print(sensorid)
            data = cursor.fetchall()
            if len(data) > 0:
                print("get_allmetrics - Hay informacion")
                return(data)
            else:
                print("get_allmetrics - NO HAY INFORMACION")
                return None
        except Exception as e:
            print("get_allmetrics - Estoy en la excepcion")
            return None

        finally:
            cursor.close()
            conn.close()
