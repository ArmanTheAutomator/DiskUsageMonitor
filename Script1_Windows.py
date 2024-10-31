# Disk Usage Monitor - This script uses the wmic command-line tool to get disk usage statistics
# and will notify a chosen email address when the disk usage goes outside of the declared values.
# Upon running the script you will be prompted to input the Drive Letter that you want to monitor,
# (i.e. C), then the Percentage Threshold of the Drive Usage (i.e. 85), and the Free Space Threshold
# in GB, (i.e. 10.0). If the Percentage of the drive you've chosen goes above your chosen value, or
# if the remaining GB storage of the Drive drops below the value you've chosen, the email address
# that you declare will be notified. 

import wmi
import smtplib

def get_disk_usage(drive_letter):
  # Connect to WMI and get disk drive object
  c = wmi.WMI()
  drive = c.Win32_LogicalDisk(DriveLetter=drive_letter)[0]

  # Calculate usage percentage and free space
  usage_percent = int(drive.PercentFree)
  free_space_gb = round(int(drive.FreeSpace) / (1024**3), 2)
  return usage_percent, free_space_gb

def send_email_notification(usage, free_space, recipient, subject):
  # Configure sender email and password securely (not shown here)
  sender = "your_email@example.com"
  password = "your_password"
  message = f"""Disk usage on {drive_letter}:
  Percentage Used: {usage}%
  Free Space: {free_space_gb} GB

  This script detected usage exceeding {threshold_percent}% 
  and/or free space falling below {threshold_free_space} GB."""
  with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, f"Subject: {subject}", message.encode('utf-8'))

# Get user input for thresholds and recipient email
drive_letter = input("Enter the drive letter to monitor (e.g., C): ")
threshold_percent = int(input("Enter the percentage threshold (e.g., 85): "))
threshold_free_space = float(input("Enter the free space threshold in GB (e.g., 10.0): "))
recipient_email = input("Enter the recipient email address: ")

# Get disk usage information
usage_percent, free_space_gb = get_disk_usage(drive_letter)

# Check if thresholds are exceeded
if usage_percent > threshold_percent or free_space_gb < threshold_free_space:
  subject = f"Disk Usage Alert on {drive_letter}"
  send_email_notification(usage_percent, free_space_gb, recipient_email, subject)
  print(f"Disk usage on {drive_letter} exceeded thresholds. Email sent to {recipient_email}")
else:
  print(f"Disk usage on {drive_letter} is within normal limits.")
