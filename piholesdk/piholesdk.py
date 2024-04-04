import paramiko
import time

class PiHoleClient:

    def __init__(self, ssh_ip_address, ssh_username, ssh_password):

        self.ssh_ip_address = ssh_ip_address
        self.ssh_username = ssh_username
        self.ssh_password = ssh_password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ssh_ip_address, username=self.ssh_username, password=self.ssh_password)

    @classmethod
    def create_dns_record(cls, hostname:str, ip_address:str, domain:str):
        dns_record = f"{ip_address} {hostname}.{domain}"
        return dns_record

    def push_dns_record(self, dns_record):
        try:
            command = f"echo '{dns_record}' | sudo tee -a /etc/pihole/custom.list"
            stdin, stdout, stderr = self.client.exec_command(command)
            time.sleep(1)
            command = "pihole restartdns"
            stdin, stdout, stderr = self.client.exec_command(command)
            return {"status": True, "message": "A record added successfully."}
        except Exception as e:
            return {"status": False, "error": str(e)}

    def delete_dns_record(self, dns_record):
        try:
            command = f"sudo sed -i '/{dns_record}/d' /etc/pihole/custom.list"
            stdin, stdout, stderr = self.client.exec_command(command)
            restart_command = "pihole restartdns"
            stdin, stdout, stderr = self.client.exec_command(restart_command)
            return {"status": True, "message": "A Record deleted successfully."}
        except Exception as e:
            return {"status": False, "error": str(e)}

    def read_custom_list(self):
        try:
            file_path = "/etc/pihole/custom.list"
            stdin, stdout, stderr = self.client.exec_command(f"cat {file_path}")
            lines = stdout.readlines()
            dns_records = {}
            for line in lines:
                ip_address, hostname = line.strip().split()
                dns_records[hostname] = ip_address
            return {"status": True, "message": "Retrieved A record list.", "data": dns_records}
        except Exception as e:
            return {"status": False, "error": str(e)}

    def close_connection(self):
        self.client.close()
