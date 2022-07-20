from autobahnbot import AutobahnParser, SQLConnector, TelegramBot
import os

mysql_host = os.environ['MYSQL_HOST']
mysql_user = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_database = os.environ['MYSQL_DATABASE']
telegram_token = os.environ['TELEGRAM_TOKEN']
telegram_chatid = os.environ['TELEGRAM_CHATID']
env_highway = os.environ['ENV_HIGHWAY']
env_location1 = os.environ['ENV_LOCATION1']
env_location2 = os.environ['ENV_LOCATION2']


sql_connection = SQLConnector(mysql_host, mysql_user, mysql_password, mysql_database)
telegram_bot = TelegramBot(telegram_token, telegram_chatid)


## DATEN ABFRAGEN UND GGF EINTRAGEN

autobahn_data = AutobahnParser().get_warnings(env_highway, env_location1, env_location2)
database_data = sql_connection.get_all_externalids()

for element in autobahn_data:
    if element["external_id"] in database_data:
        continue
    sql_connection.put_entry(element["external_id"], element["highway"], element["location_lat"], element["location_long"], element["timestamp"], element["isblocked"], element["description"], element["routea"], element["routeb"])

## DATEN VERSENDEN

unsent_data = sql_connection.get_unsent_entries()

for element in unsent_data:
    telegram_bot.sendMessage(element)
    sql_connection.set_sent(element[0])