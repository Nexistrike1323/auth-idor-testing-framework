from auth_test import test_login_bypass
from idor_test import test_idor_access
from report import generate_report

findings = []

print("[*] Starting security tests")

test_login_bypass()
findings.append("Authentication test executed")

test_idor_access()
findings.append("IDOR test executed")

generate_report(findings)
