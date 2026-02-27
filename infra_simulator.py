from src.machine import Machine
from src.input_handler import get_user_input, save_to_file

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
    print("\n=== Provisioning Complete ===")

if __name__ == "__main__":
    main()