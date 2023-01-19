import appgamekit as agk
import json

class Network:
    def __init__(self, name, ip, port):
        self.target_ip = ip
        self.port = port
        self.last_msg_id = 0
        self.name = name
        self.state = 0
        self.type = 0
        self.network_id = 0

    def host(self):
        network_id = agk.host_network("AGK Test Game", self.name, 45000)
        self.type = 0
        self.state = 1
        return network_id

    def client(self):
        network_id = agk.join_network_ip(self.target_ip, 45000, self.name)
        self.type = 0
        self.state = 1
        return network_id

    def retreive_message(self, network_id):
        cmessage = agk.get_network_message(network_id)
        while cmessage != 0:
            player_data = None
            player_data = agk.get_network_message_string(cmessage)
            player_obj = json.loads(player_data)
            agk.delete_network_message(cmessage)
            cmessage = agk.get_network_message(network_id)
            print(player_data)
            return player_data

    def send_message(self, network_id, message):
        cmessage = agk.create_network_message()
        agk.add_network_message_string(cmessage, json.dumps(message))
        print("Outgoing - " + str(message))
        agk.send_network_message(network_id, 0, cmessage)

    def update(self):
        pass
