from database import escape_string, Database
from utility import fetch_api


def log_map():
    network_query = fetch_api("https://clwo.eu/jailbreak/api/v2/networkquery.php")
    for server in network_query['data']:
        print("Parsing server " + server['ShortName'] + " with SID " + server['ServerID'] + ".")
        sid = escape_string(server['ServerID'])
        player_count = escape_string(server['ClientCount'])
        map_name = escape_string(server['MapName'])
        query = "INSERT INTO log_map (sid, map, player_count) VALUES ('" + \
                sid + "', '" + \
                map_name + "', '" + \
                player_count + "')"
        Database.db.execute(query)
