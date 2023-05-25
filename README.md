# SMTP Mailer+Spoofer

Author: [Jeret Christopher@M0du5 + AI](https://github.com/jeretc)

Welcome to the SMTP Mailer+Spoofer! This program allows you to send or spoof emails using an SMTP server.


## Usage

To use the program, simply run the `smtpms.py` script and follow the prompts. You will be asked to enter the sender's email address, the receiver's email address, the email subject and body, and the SMTP server hostname and port number. You will also be asked to enter the sender's email password, which will be masked and won't be displayed as you type it.

   
### Spoofing the sender's email address

The program also includes an option to spoof the sender's email address. This means that you can enter a different email address that will appear as the sender of the email to the recipient.

To use this feature, simply enter a spoofed sender's email address when prompted. Please note that this feature may not work with all SMTP servers and email providers. Some SMTP servers and email providers have strict authentication and validation mechanisms in place to prevent email spoofing.

If spoofing fails, it could be due to several reasons. For example, the SMTP server or email provider might require proper authentication methods (such as SPF, DKIM, and DMARC) to be set up correctly for the domain used in the spoofed sender's email address. The reputation of the domain and IP address used in the spoofed sender's email address can also affect whether spoofing is successful.
   

## License
This project is licensed under the [MIT License](LICENSE).

