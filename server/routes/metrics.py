import json
import mariadb

class metrics(object):

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
            for result in cursor.stored_results():
                data = result.fetchall()
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
            con.close()
