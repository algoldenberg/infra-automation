# DevOps Infrastructure Provisioning & Configuration Automation Tool

> **Educational Project** - Developed as part of DevOps Engineer training course

A modular Python-based infrastructure provisioning and configuration automation tool built from scratch, designed with architecture patterns ready for future AWS and Terraform integration.

## 🎯 Project Overview

This tool demonstrates infrastructure-as-code principles through an interactive CLI that automates VM provisioning and service configuration. Built with production-ready patterns including modular architecture, comprehensive logging, and idempotent operations.

## 🛠️ Tech Stack

- **Languages**: Python 3.x, Bash
- **Key Libraries**: Pydantic V2, subprocess, logging
- **Tools**: Git, GitHub CLI, venv
- **Target Services**: Nginx (with extensibility for more)

## ✨ Features

### Core Functionality
- **Interactive CLI** - Dynamic VM definition with Pydantic V2 data validation
- **Modular OOP Architecture** - Separation of concerns: input layer, business logic, and orchestration
- **Service Automation** - Automated installation and configuration of services (Nginx) via Bash scripts
- **Idempotent Operations** - Scripts designed to be safely re-run without side effects

### Technical Highlights
- **Python-Bash Integration** - Seamless subprocess management with comprehensive error handling
- **Dual Logging System** - Coordinated logging across Python and Bash layers writing to `provisioning.log`
- **Configuration Persistence** - Machine configurations stored in JSON format
- **Isolated Environment** - Virtual environment setup with dependency management via `requirements.txt`
- **Version Control** - Organized Git repository structure with clean commit history

## 🏗️ Architecture
```
infra-automation/
├── infra_simulator.py   # Main entry point and orchestration
├── src/
│   ├── machine.py       # Machine class - business logic layer
│   ├── input_handler.py # User input and Pydantic validation
│   └── logger.py        # Logging configuration
├── scripts/
│   └── setup_nginx.sh   # Idempotent Bash script for Nginx
├── configs/
│   └── instances.json   # JSON configuration storage
├── logs/
│   └── provisioning.log # Provisioning activity logs
└── requirements.txt     # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Bash shell
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/algoldenberg/infra-automation.git
cd infra-automation

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate      # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Usage
```bash
python infra_simulator.py
```

## 📊 Expected Output
```
=== Infrastructure Provisioning Tool ===

Enter machine name (or 'done' to finish): web-server
Enter OS (Ubuntu/CentOS): Ubuntu
Enter CPU (e.g., 2vCPU): 2vCPU
Enter RAM (e.g., 4GB): 4GB
Enter machine name (or 'done' to finish): done

[INFO] Provisioning machine: web-server | OS: Ubuntu | CPU: 2vCPU | RAM: 4GB
Configurations saved to configs/instances.json
[INFO] Nginx installation completed.

=== Provisioning Complete ===
```

## 📝 Learning Outcomes

This project demonstrates:
- Infrastructure automation fundamentals
- Python OOP design patterns for DevOps tools
- Cross-language integration (Python + Bash)
- Configuration management principles
- Logging and error handling best practices
- Idempotent script design

## 🔮 Future Enhancements

Architecture is designed for extension to:
- AWS EC2 provisioning via boto3
- Terraform integration for multi-cloud support
- Additional service configurations (Docker, databases, etc.)
- Remote execution via SSH
- Configuration drift detection

## 📚 Course Context

Built as part of **John Bryce DevOps Engineer** training program to demonstrate:
- Infrastructure-as-Code principles
- Automation tool development
- Production-ready coding practices
- DevOps workflow fundamentals

## 📄 License

Educational project - MIT License

## 👤 Author

**Alex Goldenberg**
- GitHub: [@algoldenberg](https://github.com/algoldenberg)
- Portfolio: [sashagolden.xyz](https://sashagolden.xyz)

---

*Note: This is an educational project demonstrating DevOps automation concepts. For production use, consider established tools like Terraform, Ansible, or Pulumi.*