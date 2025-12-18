from datetime import datetime

def generate_report(findings):
    report_file = "../output/security_test_report.txt"

    with open(report_file, "w") as file:
        file.write("Authentication & IDOR Security Test Report\n")
        file.write(f"Generated on: {datetime.now()}\n\n")

        for finding in findings:
            file.write(f"- {finding}\n")

    print(f"[+] Report saved to {report_file}")
