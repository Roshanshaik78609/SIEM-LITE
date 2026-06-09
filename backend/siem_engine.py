import time

from threat_detector import detect_brute_force
from file_access_detector import detect_file_access
from password_spray_detector import detect_password_spray
from unauthorized_access import detect_unauthorized_access
from privilege_escalation import detect_privilege_escalation


print("=" * 50)
print("        SIEM-Lite Engine Started")
print("=" * 50)

while True:

    print("\nScanning new logs...\n")

    detect_brute_force()
    detect_file_access()
    detect_password_spray()
    detect_unauthorized_access()
    detect_privilege_escalation()

    print("\nScan completed.")
    print("Waiting 5 seconds...\n")

    time.sleep(5)