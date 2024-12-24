# Django Secure Messaging App

## Table of Contents
- [Introduction](#introduction)
- [Project Objectives](#project-objectives)
- [System Overview](#system-overview)
- [Key Features](#key-features)
- [Technical Stack and Tools](#technical-stack-and-tools)
- [Installation and Setup](#installation-and-setup)
- [Middleware Functionality](#middleware-functionality)
- [System Development Roadmap](#system-development-roadmap)
- [Team Members](#team-members)

## Introduction
This project demonstrates the development of two secure Django REST Framework applications, emphasizing secure real-time communication through encrypted and hashed messages. It includes user authentication, secure APIs, and a functional dashboard, adhering to Django best practices.

## Project Objectives
- **Develop Secure Applications:** Build two robust Django REST Framework applications with secure data handling features.
- **Implement Encryption Middleware:** Ensure data confidentiality via middleware for encrypting outgoing and decrypting incoming messages.
- **Enable Secure Communication:** Establish APIs for secure message exchange using encryption and hashing techniques.
- **Build a Functional Dashboard:** Design an intuitive dashboard for managing users and viewing messages securely.
- **Promote Collaboration:** Utilize a GitHub repository for version control and team collaboration.

## System Overview
**Project Title:** D-Message  
**Description:** A secure real-time chat system consisting of two interconnected applications, enabling seamless and encrypted communication. Built with Django REST Framework and leveraging Redis for real-time messaging.

## Key Features
1. **Real-Time Communication:** Utilizes WebSockets for instant, bi-directional message exchange.
2. **Dynamic Room Creation:** Allows private or group conversations in unique chat rooms.
3. **Secure Communication:** Middleware encrypts and decrypts messages during transmission.
4. **User Authentication:** Robust system with token-based session management.
5. **Two-Way System Communication:** Interoperable systems enable cross-platform messaging.
6. **Scalable Room Management:** High-performance architecture supports multiple participants.
7. **User-Friendly Interface:** Responsive and intuitive design with Tailwind CSS.

## Technical Stack and Tools
**Backend:**  
- Django 5.0+  
- Django Channels  
- PostgreSQL  
- Redis  
- Daphne

**Frontend:**  
- HTML, CSS, JavaScript  
- Tailwind CSS

**Security:**  
- Django’s built-in auth middleware  
- Custom encryption middleware

**Development Tools:**  
- Git/GitHub  
- VS Code

## Installation and Setup
### Prerequisites
1. Install Python.
2. Install Redis for WebSocket functionality.
3. Clone the repository:
   ```bash
   git clone https://github.com/kurtchinta/FINAL-PROJECT-120
   ```

### Setup Instructions
1. Navigate to the project directory:
   ```bash
   cd FINAL-PROJECT-120/DjangoProject
   ```
2. Update database configurations in `First_System/settings.py` and `Second_System/settings.py` to match your local setup.
3. Ensure Redis is installed and running.
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start both systems:
   ```bash
   python manage.py runserver 8000
   python manage.py runserver 8001
   ```

## Middleware Functionality
### Encryption
- Encrypts message payloads before sending.
- Uses Fernet encryption to ensure secure transmission.

### Decryption
- Decrypts messages upon receipt.
- Ensures only authorized users can view the content.

## System Development Roadmap
1. Set up Django project and apps.
2. Configure database and sessions.
3. Develop frontend UI.
4. Implement WebSockets and integrate Redis.
5. Define models for users and messages.
6. Store messages securely in PostgreSQL.
7. Implement and integrate encryption middleware.
8. Develop an admin dashboard for user management.
9. Implement APIs for message history with decryption.
10. Refine UI/UX using Tailwind CSS.
11. Duplicate and configure the system for additional use cases.

## Team Members
- **Kurt Reserva** (Group Leader)
- **Drandreb Reyes**
- **Jan Carlo Dela Cerna**
- **John Dave Lausa**

## Section
**Course:** IT 120 – Integrative Programming Technologies II
**Section:** AE1
**Term:** Final – 2024–2025, 1st Semester  
**Instructor:** Dexter A. Romaguera

