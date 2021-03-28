class Service:
    def __init__(self, protocol, port_number, is_SSL):
        self.protocol = protocol #TCP or UDP
        self.port_number = port_number
        self.is_SSL = is_SSL

class Target:
    def __init__(self, ip, fqdn=""):
        self.ip = ip
        self.fqdn = fqdn
        self.services = []
        self.active_tasks = []
        self.complete = False
        self.ports_probed = dict.fromkeys([i for i in range(1,65353)], False)

    @property
    def fqdn(self):
       return self.fqdn

    @fqdn.setter
    def fqdn(self, new_fqdn):
        self.fqdn = new_fqdn
    
    def add_service(self, service)
        self.services += service
    
    def set_port_probed(self, port_num):
        self.ports_probed[port_num] = True
    