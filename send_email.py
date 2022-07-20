import sys
import os
import time
import argparse
import smtplib
from smtplib import SMTP_SSL
import logging
import json
sys.path.append('/usr/lib/python3/dist-packages')
import requests
from datetime import datetime

def send_email(user = None, pwd = None, to = "", subject = "", body = ""):
    logger = logging.getLogger("send_email") # Initialize logging

    # Make sure user and password is set
    if not user or not pwd or not to or not subject or not body:
        logger.error('Not all required parameters provided')
        return False

    # Set variables
    gmail_user = user
    gmail_pwd = pwd
    FROM_EMAIL = user
    TO_EMAIL = []
    for i in to.split(","):
        TO_EMAIL.append(i)
    SUBJECT_EMAIL = subject

    try:
        #print(requests.get('http://fluidd-ender/printer/objects/query?print_stats=filename').json())
        query = requests.get('http://fluidd-ender/printer/objects/query?print_stats=filename').json()
        TEXT = datetime.now().strftime("%m/%d/%Y %H:%M:%S")  + "\n" + query["result"]["status"]["print_stats"]["filename"] + "\n" + body
    except Exception as e:
        print("Unable to get filename from moonraker",e)

    try:
        #print(requests.get('http://fluidd-ender/printer/info').json())
        query = requests.get('http://fluidd-ender/printer/info').json()
        SUBJECT_EMAIL = query["result"]["hostname"] + " - " + SUBJECT_EMAIL
    except Exception as e:
        print("Unable to get filename from moonraker",e)

    # Prepare email message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM_EMAIL, TO_EMAIL, SUBJECT_EMAIL, TEXT)

    # Try to email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        #server.ehlo()
        #server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM_EMAIL, TO_EMAIL, message)
        server.close()
        logger.info('Successfully sent email to ' + user)
    # Catch any exceptions
    except Exception as e:
        logger.error("Failed to send mail: " + str(e))
        raise e

parser = argparse.ArgumentParser(description="")
parser.add_argument("-el", "--email-login", type=str, help="Gmail username for sending and receiving email alerts for open pledge levels and pledge results.")
parser.add_argument("-epwd", "--email-password", type=str, help="Gmail password")
parser.add_argument("-t", "--to", type=str, help="Destination email address")
parser.add_argument("-s", "--subject", type=str, help="Email Subject")
parser.add_argument("-b", "--body", type=str, default=" ", help="Email Body")

args = parser.parse_args()

# If email password argument was provided but not email login
if not args.email_password:
    #logger.error('--email-password not specified')
    print("--email-password not specified")
    sys.exit(0) # Exit Script

if not args.email_login:
    #logger.error('--email_login not specified')
    print("--email_login not specified")
    sys.exit(0) # Exit Script

if not args.to:
    #logger.error('--to not specified')
    print("--to not specified")
    sys.exit(0) # Exit Script

if not args.subject:
    #logger.error('--subject not specified')
    print("--subject not specified")
    sys.exit(0) # Exit Script

if not args.body:
    #logger.error('--body not specified')
    print("--body not specified")
    sys.exit(0) # Exit Script


send_email(args.email_login, args.email_password, args.to, args.subject, args.body)
