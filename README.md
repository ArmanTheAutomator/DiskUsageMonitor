Disk Usage Monitoring and Email Notification Script
Developed by Arman "The Automator" Vakili
Los Angeles, CA 

**********
This Python script monitors disk usage on a specified mount point and sends an email notification if disk usage exceeds a specified threshold. 
It leverages the psutil library to check disk space and smtplib to send email alerts.

**********
Features
Monitors disk usage on a user-defined mount point
Checks if disk usage exceeds a user-defined threshold percentage
Sends an email alert if the disk usage surpasses the threshold

**********
Requirements
Python 3.x
psutil library (for retrieving disk usage information)
Install via: pip install psutil

**********
Usage
Clone or download this repository.

Install the required libraries.
pip install psutil

Run the script in a terminal.
python disk_usage_monitor.py

**********
Input the required details when prompted:
Mount Point: Path to the mount point to monitor (e.g., / for root).
Threshold Percentage: Disk usage percentage at which an alert is triggered (e.g., 85 for 85%).
Recipient Email Address: The email address to which alerts will be sent.
Sender Email Address: The email address from which alerts will be sent (must support SMTP, e.g., Gmail).
Sender Email Password: Password for the sender email account (hidden input using getpass).

**********
Email Configuration:
This script uses Gmail's SMTP server by default (smtp.gmail.com, port 587). 
Ensure the sender email has "Allow less secure app access" enabled or uses an app password for Gmail accounts with two-factor authentication.

**********
Code Details

Functions

get_disk_usage(mount_point): Retrieves disk usage information (total, used, and percentage used) for the specified mount point.
Args: mount_point (str) - Path to the mount point.
Returns: Tuple of total disk space in GB, used disk space in GB, and percentage of disk space used.

send_email_notification(usage, recipient, subject): Sends an email alert if the disk usage exceeds the threshold.
Args:
usage (tuple) - Contains total space, used space, and percentage used.
recipient (str) - Email address to send notifications.
subject (str) - Subject line of the email alert.

**********
Example Execution

python disk_usage_monitor.py
Enter the mount point to monitor (e.g., /): /
Enter the percentage threshold (e.g., 85): 85
Enter the recipient email address: recipient@example.com
Enter the email that will SEND the update email: sender@example.com
Enter the password for the sender email: (password hidden)

The script will check the specified mount point's disk usage and send an email if it exceeds the defined threshold.

**********
Example Email Notification

Subject: Disk Usage Alert on /
Body:

Disk usage on /:
Total Space: 100 GB
Used Space: 85 GB
Percentage Used: 85%

This script detected usage exceeding 85% and triggered this notification.

**********
Important Notes
This script currently supports Gmail’s SMTP server, but it can be modified for other email providers by updating the SMTP server and port.
Remember to safeguard your email password. This script uses getpass to keep it secure.
Troubleshooting
Authentication Error: If you receive an authentication error, ensure your email provider allows SMTP access and that the credentials are correct.
SMTP Connection Issues: Verify internet connection and email server details.

