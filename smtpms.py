import smtplib
from email.mime.text import MIMEText
import re
from getpass import getpass

GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+$'
    return re.match(regex, email)

def is_valid_hostname(hostname):
    if hostname.startswith('-') or hostname.endswith('-'):
        return False
    if '.' not in hostname:
        return False
    regex = r'^[a-zA-Z0-9.-]+$'
    return re.match(regex, hostname)

def is_valid_port(port):
    try:
        port = int(port)
        return 0 < port < 65536
    except ValueError:
        return False

def colored_input(prompt, color, optional=False):
    while True:
        print(color + prompt + RESET, end='')
        try:
            user_input = input()
            if not user_input and not optional:
                print(RED + 'Error: Input cannot be empty' + RESET)
                continue
            if 'email address' in prompt and user_input and not is_valid_email(user_input):
                print(RED + 'Error: Invalid email address' + RESET)
                continue
            if 'SMTP server hostname' in prompt and user_input and not is_valid_hostname(user_input):
                print(RED + 'Error: Invalid hostname' + RESET)
                continue
            if 'SMTP server port number' in prompt and user_input and not is_valid_port(user_input):
                print(RED + 'Error: Invalid port number' + RESET)
                continue
            return user_input
        except (KeyboardInterrupt, EOFError):
            print(RED + '\nExiting program' + RESET)
            exit()

def send_email(sender, password, receiver, subject, body, smtp_server, smtp_port, spoofed_sender=None):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = spoofed_sender if spoofed_sender else sender
        msg['To'] = receiver
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print(GREEN + 'Email sent successfully!' + RESET)
    except smtplib.SMTPAuthenticationError:
        print(RED + 'Error: Authentication failed. Please check your email and password.' + RESET)
    except smtplib.SMTPConnectError:
        print(RED + 'Error: Could not connect to the SMTP server. Please check your SMTP server hostname and port number.' + RESET)
    except smtplib.SMTPRecipientsRefused:
        print(RED + 'Error: The recipient\'s email address was refused. Please check the recipient\'s email address.' + RESET)
    except smtplib.SMTPSenderRefused:
        print(RED + 'Error: The sender\'s email address was refused. Please check the sender\'s email address.' + RESET)
    except smtplib.SMTPDataError:
        print(RED + 'Error: The SMTP server refused to accept the message data.' + RESET)
    except Exception as e:
        print(RED + 'Error sending email: ' + str(e) + RESET)

print(GREEN + 'Welcome to the SMTP Email Sender-Spoofer!' + RESET)
print('This program allows you to send or spoof emails using an SMTP server.\n')

sender = colored_input('Enter the sender\'s email address: ', GREEN)
spoofed_sender = colored_input('Enter the spoofed sender\'s email address (optional): ', GREEN, optional=True)
receiver = colored_input('Enter the receiver\'s email address: ', GREEN)
subject = colored_input('Enter the email subject: ', GREEN)
body = colored_input('Enter the email body: ', GREEN)

smtp_server = colored_input('Enter the SMTP server hostname (e.g. smtp.gmail.com): ', GREEN)
smtp_port = int(colored_input('Enter the SMTP server port number (e.g. 587): ', GREEN))
password = getpass(GREEN + 'Enter the sender\'s email password: ' + RESET)

send_email(sender, password, receiver, subject, body, smtp_server, smtp_port, spoofed_sender=spoofed_sender)

