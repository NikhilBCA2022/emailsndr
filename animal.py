class server_info:
    def __init__(self, server_ip, server_version):        
        self.server_ip = server_ip
        self.server_version = server_version

    def status(self):
        if self.server_version == "1.0":
            print( "Server is up to date.")
        else:
            print (f"Server {self.server_ip} is outdated. Please update to the latest version.")

server = server_info("23.3.4.5", "1.0")
server.status()