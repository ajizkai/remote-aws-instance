import slackclient
from instance import Instance


class Slack(Instance):
    def __init__(self):
        super.__init__(self)
        pass

    def msgRaw(self):
        instanceList = []
        for i in self.listInstance:
            instanceList.append({"id" : i.get('InstanceId'), 
                                    "name": i.get('filter')})
        return instanceList

    def msgFormater(self):
        content = ""
        for i in self.msgRaw():
            content += "*" + i.get('name') + "*" + ": " + i.get('id') + "\n"
        
        block = {
	        "blocks": [
		        {
			        "type": "section",
			        "text": {
				            "type": "plain_text",
				            "text": content,
				            "emoji": true
		        	    }
		        }
	        ]
        }
        return block
    
    def msgSend(self):
        sc = slackclient.SlackClient("")
        sc.api_call("chat.postMessage", channel="#general", blocks=self.msgFormater())
        return True

    def msgStart(self, instanceId):
        self.startInstance(instanceId)
        self.msgSend()
        return True

    def msgStop(self, instanceId):
        self.stopInstance(instanceId)
        self.msgSend()
        return True