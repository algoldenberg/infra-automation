from src.logger import logger

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }

    def log_creation(self):
        message = f"Provisioning machine: {self.name} | OS: {self.os} | CPU: {self.cpu} | RAM: {self.ram}"
        logger.info(message)
        print(f"[INFO] {message}")