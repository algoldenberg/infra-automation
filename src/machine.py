from src.logger import logger

class Machine:
    """Represents a virtual machine with its configuration details."""

    def __init__(self, name, os, cpu, ram):
        # Store machine configuration
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    def to_dict(self):
        """Return machine details as a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }

    def log_creation(self):
        """Log machine creation to both console and provisioning.log."""
        message = f"Provisioning machine: {self.name} | OS: {self.os} | CPU: {self.cpu} | RAM: {self.ram}"
        logger.info(message)
        print(f"[INFO] {message}")