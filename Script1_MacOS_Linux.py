import psutil
import smtplib
from getpass import getpass


def get_disk_usage(mount_point):
    """
    This function gets disk usage information for a specified mount point.

    Args:
        mount_point: String, the path to the mount point.

    Returns:
        A tuple containing:
            - Total disk space in GB (float)
            - Used disk space in GB (float)
            - Percentage of disk space used (float)
    """
    disk_usage = psutil.disk_usage(mount_point)
    total_gb = round(disk_usage.total / (1024 ** 3), 2)
    used_gb = round(disk_usage.used / (1024 ** 3), 2)
    percentage_used = round(disk_usage.used / disk_usage.total * 100, 2)
    return total_gb, used_gb, percentage_used


def send_email_notification(usage, recipient, subject):
    """
    This function sends an email notification with disk usage details.

    Args:
        usage: Tuple containing total, used space, and percentage used.
        recipient: String, the email address to send the notification to.
        subject: String, the subject line of the email.
    """
    # Configure sender email and password securely (not shown here)
    sender = input("Enter the email that will SEND the update email: ")
    password = getpass("Enter the password for the sender email: ")

    message = f"""Disk usage on {mount_point}:
    Total Space: {usage[0]} GB
    Used Space: {usage[1]} GB
    Percentage Used: {usage[2]}%

    This script detected usage exceeding {threshold_percent}% and triggered this notification."""

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, f"Subject: {subject}\n\n{message}")


# Get user input for mount point, threshold, and recipient email
mount_point = input("Enter the mount point to monitor (e.g., /): ")
threshold_percent = int(input("Enter the percentage threshold (e.g., 85): "))
recipient_email = input("Enter the recipient email address: ")

# Get disk usage information
total_gb, used_gb, percentage_used = get_disk_usage(mount_point)

# Check if threshold is exceeded
if percentage_used > threshold_percent:
    subject = f"Disk Usage Alert on {mount_point}"
    send_email_notification((total_gb, used_gb, percentage_used), recipient_email, subject)
    print(f"Disk usage on {mount_point} exceeded threshold. Email sent to {recipient_email}")
else:
    print(f"Disk usage on {mount_point} is within normal limits.")
