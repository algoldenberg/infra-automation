from src.machine import Machine
from src.input_handler import get_user_input, save_to_file
import subprocess

def run_setup_script():
    try:

        # On Linux server use:
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)

        # On Windows/Git Bash use
        # subprocess.run(["sh", "scripts/setup_nginx.sh"], check=True)
        print("[INFO] Nginx installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to run setup script: {e}")

def main():
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
    run_setup_script()
    print("\n=== Provisioning Complete ===")

if __name__ == "__main__":
    main()