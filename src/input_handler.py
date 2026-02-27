import json
from pydantic import BaseModel, field_validator
from typing import Literal

class MachineInput(BaseModel):
    name: str
    os: Literal["Ubuntu", "CentOS"]
    cpu: str
    ram: str

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Machine name cannot be empty")
        return v

    @field_validator("cpu")
    @classmethod
    def cpu_must_be_valid(cls, v):
        if not v.endswith("vCPU"):
            raise ValueError("CPU must be in format like '2vCPU'")
        return v

    @field_validator("ram")
    @classmethod
    def ram_must_be_valid(cls, v):
        if not v.endswith("GB"):
            raise ValueError("RAM must be in format like '4GB'")
        return v

def get_user_input():
    machines = []

    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break

        os = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")

        try:
            machine = MachineInput(name=name, os=os, cpu=cpu, ram=ram)
            machines.append(machine.model_dump())
        except Exception as e:
            print(f"[ERROR] Invalid input: {e}")
            print("Please try again.\n")
            continue

    return machines

def save_to_file(machines):
    with open("configs/instances.json", "w") as f:
        json.dump(machines, f, indent=4)
    print("Configurations saved to configs/instances.json")

if __name__ == "__main__":
    machines = get_user_input()
    save_to_file(machines)