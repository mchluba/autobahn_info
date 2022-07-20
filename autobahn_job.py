from autobahnbot import AutobahnParser, SQLConnector, TelegramBot
import topsecret

sql_connection = SQLConnector(topsecret.mysql_host, topsecret.mysql_user, topsecret.mysql_password, topsecret.mysql_database)
telegram_bot = TelegramBot(topsecret.telegram_token, topsecret.telegram_chatid)


## DATEN ABFRAGEN UND GGF EINTRAGEN

autobahn_data = AutobahnParser().get_warnings("A3", "Würzburg", "Nürnberg")
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