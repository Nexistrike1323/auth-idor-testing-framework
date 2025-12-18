# Authentication & IDOR Vulnerability Testing Framework

## 📌 Overview
This project is a security testing framework designed to identify common web
application vulnerabilities related to **authentication flaws** and
**Insecure Direct Object Reference (IDOR)** issues.

The framework automates basic security checks and generates a clear report,
simulating real-world application security and SOC workflows.

---

## 🎯 Problem Statement
Many web applications fail to properly enforce authentication and authorization
controls, leading to vulnerabilities such as:
- Authentication bypass
- Unauthorized access to user resources (IDOR)

Manual testing can be repetitive and time-consuming. This project demonstrates
how such checks can be automated responsibly.

---

## 🧠 Solution
The framework:
- Tests authentication logic for weak validation
- Checks for IDOR-style access control flaws
- Executes tests against an intentionally vulnerable application
- Generates a structured security report for review

All testing is performed **locally** using OWASP Juice Shop to ensure legality
and ethical compliance.

---

## 🔄 Workflow
1. Launch a vulnerable test application (OWASP Juice Shop)
2. Execute authentication security checks
3. Perform IDOR access control tests
4. Capture findings during execution
5. Generate a consolidated security report

---

## 🛠️ Tools & Technologies
- **Operating System:** Ubuntu Linux
- **Programming Language:** Python
- **Libraries:** requests, BeautifulSoup
- **Test Application:** OWASP Juice Shop (Docker)

---

## ⚠️ Legal & Ethical Notice
This framework is intended strictly for **educational and authorized testing**.
All tests are conducted on a locally hosted, intentionally vulnerable application.
Unauthorized testing of real-world systems is not performed or encouraged.

---

## 📊 Output
- Console-based vulnerability findings
- Security assessment report generated at:


---

## 🚀 How to Run
1. Start OWASP Juice Shop locally using Docker
2. Navigate to the source directory:
```bash
python src/main.py

👨‍💻 Author

Venkata Neeraj Meka
Cybersecurity Enthusiast | Application Security & Automation
GitHub: https://github.com/Nexistrike1323





