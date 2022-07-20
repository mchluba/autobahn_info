import mysql.connector
class SQLConnector():

    def __init__(self, sql_host, sql_user, sql_password, sql_database):
        self.sql_connection = mysql.connector.connect(
            host = sql_host,
            username = sql_user,
            password = sql_password,
            database = sql_database
        )

    def put_entry(self, external_id, highway, location_lat, location_long, timestamp, isblocked, description, routea, routeb):
        dbhandler = self.sql_connection.cursor()
        sql_query = "INSERT INTO highway_messages (external_id, highway, location_lat, location_long, timestamp, isblocked, description, routea, routeb, sent) VALUES ('" + external_id + "', '" + highway + "', '" + location_lat + "', '" + location_long + "', '" + timestamp + "', '" + isblocked + "', '" + description + "', '" + routea + "', '" + routeb + "', 'F')"
        dbhandler.execute(sql_query)
        self.sql_connection.commit()

    def get_unsent_entries(self):
        unsent_entries = []
        dbhandler = self.sql_connection.cursor()
        sql_query = "SELECT * FROM highway_messages WHERE sent = 'F'"
        dbhandler.execute(sql_query)
        for item in dbhandler:
            unsent_entries.append(item)
        return unsent_entries

    def set_sent(self, id):
        dbhandler = self.sql_connection.cursor()
        sql_query = "UPDATE highway_messages SET sent = 'T' WHERE id=" + str(id)
        dbhandler.execute(sql_query)
        self.sql_connection.commit()

    def get_all_externalids(self):
        all_external_ids = []
        dbhandler = self.sql_connection.cursor()
        sql_query = "SELECT external_id FROM highway_messages"
        dbhandler.execute(sql_query)
        for item in dbhandler:
            all_external_ids.append(item[0])
        return all_external_ids
