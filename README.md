# 🎓 Student Subject Enrollment System (CLI + GUI)

This project is a **Python-based student subject enrollment system** that allows students to sign up, log in, and manage their subject enrollments.  
It supports both **CLI** (Command-Line Interface) and **GUI** (Graphical User Interface) modes.  
The system enforces rules such as **maximum subject limits** and **no duplicate 3-digit subject IDs per student**.

---

## 📘 Project Overview

The system simulates a university subject enrollment process.  
It provides modules for:
- **Student registration and login** (`student.py`, `controller.py`)
- **Subject creation and management** (`subject.py`)
- **Enrollment control and validation** (`controller.py`)
- **Data persistence** using an in-memory or file-based structure (`database.py`)
- **Menu-based navigation** via both CLI and GUI (`cli_main.py`, `gui_main.py`, `menu.py`)

Each subject is assigned a random 3-digit ID (`001`–`999`) during creation.  
A student cannot enroll in two subjects sharing the same numeric ID (e.g., `CSC101` and `MKT101`).

---

## ⚙️ System Requirements

| Component | Version / Recommendation |
|------------|--------------------------|
| **Python** | 3.0 |
| **Libraries** | Standard Library |
| **OS** | macOS, Windows, or Linux |
| **Optional GUI** | Tkinter (bundled with Python) |

---

## 🧩 Installation and Setup

1. **Clone or copy** the project folder to your computer.

   ```bash
   git clone https://github.com/yourusername/student-enrollment-system.git
   cd student-enrollment-system
2. **Running instructions** for CLI
   ```bash
   python cli_main.py
   ```
3. **Running instructions** for GUI
   ```bash
   python gui_main.py
   ```
