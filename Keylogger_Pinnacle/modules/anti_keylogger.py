import psutil
import os 
import hashlib

class AntiKeylogger:
    def __init__(self):
        self.suspicious_processes = []

    def scan_for_keyloggers(self):
        # List of known suspicious keywords
        keywords = ["keylogger", "hook", "spy", "capture", "intercept"]

        for process in psutil.process_iter(attrs=['pid', 'name']):
            process_name = process.info['name']
            if any(keyword in process_name.lower() for keyword in keywords):
                self.suspicious_processes.append(process.info)

        return self.suspicious_processes

    def display_suspicious_processes(self):
        if self.suspicious_processes:
            print("Suspicious processes detected:")
            for process in self.suspicious_processes:
                print(f"PID: {process['pid']} | Name: {process['name']}")
        else:
            print("No suspicious processes detected.")

    def monitor_network(self):
        suspicious_ips = ['192.168.0.10', '192.168.1.100']  # Example of known C2 server IPs
        connections = psutil.net_connections(kind='inet')

        for conn in connections:
            if conn.raddr and conn.raddr.ip in suspicious_ips:
                print(f"Suspicious connection detected: {conn.raddr.ip}")

    def check_file_integrity(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                file_data = f.read()
                checksum = hashlib.sha256(file_data).hexdigest()
                print(f"Checksum of {file_path}: {checksum}")
