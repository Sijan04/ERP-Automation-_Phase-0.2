# akaar-erp-unit-testing

This repository contains **automation test scripts** for the Akaar ERP system.  
The project is built with **Python, Selenium, and Faker** to perform automated testing of various ERP modules like login, HRM, employee creation, class management, and data deletion.

## 📌 Features
- **Automated Login** – Script for logging into the ERP application.
- **HRM Module Access** – Test navigation and accessibility of the HRM module.
- **Class Management**  
  - Add new classes with fake data.  
  - Delete existing classes from the list.
- **Employee Management**  
  - Create new employees using **Faker** (randomized names, emails, phone numbers, etc.).  
  - Validate employee entries in the system.
- **List Management** – Test deleting records from ERP lists.
- **Reusable Test Scripts** – Each module has an independent Python script for modular testing.

## 📂 Project Structure
1.Access_HRM.py # Test script for accessing HRM module
2.Add_Class.py # Add new classes using Faker data
3.Delete_From_List.py # Delete specific entry from a list
4.Delete_List.py # Delete full list data
5.Employee_Create.py # Employee creation with fake data
6.Login.py # Login automation
7.requirements.txt # Dependencies list
8.idea/ # Project settings (PyCharm/IDE configs)

🛠️ Tech Stack

#Python 3.x

#Selenium – Browser automation

#Faker – Random test data generation

#Pytest (optional) – Can be integrated for structured test execution

📌 Future Improvements

#Add Pytest test cases with reporting.

#Implement CI/CD integration (GitHub Actions).

#Add screenshot capture for failed tests.

#Create test data cleanup utilities.

This project is private and intended for internal testing of the Akaar ERP system.
Unauthorized distribution is prohibited.
