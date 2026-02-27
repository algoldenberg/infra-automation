from src.machine import Machine
from src.input_handler import get_user_input, save_to_file
from src.logger import logger
import subprocess

def run_setup_script():
    try:
        # On Linux server use:
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)

        # On Windows/Git Bash use
        # subprocess.run(["sh", "scripts/setup_nginx.sh"], check=True)
        logger.info("Nginx installation completed.")
        print("[INFO] Nginx installation completed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to run setup script: {e}")
        print(f"[ERROR] Failed to run setup script: {e}")

def main():
    logger.info("=== Provisioning started ===")
    print("=== Infrastructure Provisioning Tool ===\n")
    
    machines_data = get_user_input()
    
    machines = []
    for data in machines_data:
        machine = Machine(
            name=data["name"],
            os=data["os"],
            cpu=data["cpu"],
            ram=data["ram"]
        )
        machine.log_creation()
        machines.append(machine.to_dict())
    
    save_to_file(machines)
    logger.info("Configurations saved to instances.json")
    run_setup_script()
    
    logger.info("=== Provisioning complete ===")
    print("\n=== Provisioning Complete ===")

if __name__ == "__main__":
    main()