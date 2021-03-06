#import requests
import json
import mariadb
import os
import logging
from dotenv import load_dotenv

class event(object):

    def __init__(self):
        load_dotenv()
        self.logger = logging.getLogger('prometo.event.events')
        self.logger.debug('creating an instance of event')

    def insert_event(self, data):

        try:
            conn = mariadb.connect(
                user = os.getenv("MARIADB_USERNAME"),
                password = os.getenv("MARIADB_PASSWORD"),
                host = os.getenv("MARIADB_HOST"),
                database = "prometeo",
                port = 3306)

            cursor = conn.cursor()

            cursor.callproc('sp_create_event', (data))

            data = cursor.fetchall()

            if len(data[0][0]) is 0:
                con.commit()
                return True
            else:
                return False

        except Exception as e:
            return None

        finally:
            cursor.close()
            conn.close()


    def update_event(self, data):
        try:
            conn = mariadb.connect(
                user = os.getenv("MARIADB_USERNAME"),
                password = os.getenv("MARIADB_PASSWORD"),
                host = os.getenv("MARIADB_HOST"),
                database = "prometeo",
                port = 3306)

            cursor = conn.cursor()
            cursor.callproc('sp_update_event', (data))

            data = cursor.fetchall()

            if len(data[0][0]) is 0:
                con.commit()
                return True
            else:
                return False

        except Exception as e:
            return None

        finally:
            cursor.close()
            conn.close()

    def get_event(self, eventid):
        try:
            conn = mariadb.connect(
                user = os.getenv("MARIADB_USERNAME"),
                password = os.getenv("MARIADB_PASSWORD"),
                host = os.getenv("MARIADB_HOST"),
                database = "prometeo",
                port = 3306)

            cursor = conn.cursor()
            print("get_event")
            print(eventid)

            cursor.callproc('sp_select_event', (eventid,))

            print("get_event - he abierto el cursor")

            data = cursor.fetchall()


            if len(data) > 0:
                return(data[0])
            else:
                return None

        except Exception as e:
            print("get_event - estoy en la excepcion")
            return None

        finally:
            cursor.close()
            conn.close()

    def get_allevents(self):
        print("get_allevents - entro en la funcion")

        try:
            conn = mariadb.connect(
                user = os.getenv("MARIADB_USERNAME"),
                password = os.getenv("MARIADB_PASSWORD"),
                host = os.getenv("MARIADB_HOST"),
                database = "prometeo",
                port = 3306)

            cursor = conn.cursor()

            print("get_allevents - llamada a sql")
            cursor.callproc('sp_select_all_events')
            data = cursor.fetchall()
            if len(data) > 0:
                print("get_allevents - Hay informacion")
                for i in data:
                    print(i)
                return(data)
            else:
                print("get_allevents - NO HAY INFORMACION")
                return None
        except Exception as e:
            print("get_allevents - Estoy en la excepcion")
            return None

        finally:
            cursor.close()
            conn.close()

    def get_event_firefighters_devices(self, eventid):
        try:
            conn = mariadb.connect(
                user=os.getenv("MARIADB_USERNAME"),
                password=os.getenv("MARIADB_PASSWORD"),
                host=os.getenv("MARIADB_HOST"),
                database="prometeo",
                port=3306)

            cursor = conn.cursor()
            print("get_event")
            print(eventid)

            cursor.callproc('sp_select_event_firefighters_devices', (eventid,))

            print("get_event_firefighters_devices - he abierto el cursor")

            data = cursor.fetchall()


            if len(data) > 0:
                print("get_event_firefighters_devices - hay datos")
                for i in data:
                    print(i)
                return(data)
            else:
                print("get_event_firefighters_devices - no hay datos")
                return None

        except Exception as e:
            print("get_event_firefighters_devices - estoy en la excepcion")
            return None

        finally:
            cursor.close()
            conn.close()
