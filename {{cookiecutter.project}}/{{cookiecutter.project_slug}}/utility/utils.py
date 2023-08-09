import os
import mimetypes
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv, set_key, find_dotenv

import pd
import re
load_dotenv()

from oauth2client.service_account import ServiceAccountCredentials
import gspread
from sqlalchemy import create_engine
import psycopg2

def send_alert(message='Message to send',subject='Alert',file_to_send=None,filename='alert_log.txt',mail_to='',mail_cc=''):
    """Send an email alert with an attachment if any

    Args:
        message (str): Message to be sent via email
        subject (str): Subject of the email. Defaults to Alert
        file_to_send (str, optional): Path to file to send via email attachment. Defaults to None.
        filename (str, optional): File name of the attachment. Defaults to 'alert_log.txt'.
        mail_to (str, optional): Comma separated mail list to send, Defaults to list defined in env file.
        mail_cc (str, optional): Comma separated mail cc list .
    """
    
    SMTP_HOST =os.getenv('SMTP_HOST',None)
    SMTP_TLS_PORT =os.getenv('SMTP_TLS_PORT',None)
    SMTP_SSL_PORT =os.getenv('SMTP_SSL_PORT',None)
    SMTP_MAIL_FROM =os.getenv('SMTP_MAIL_FROM',None)
    SMTP_MAIL_TO =os.getenv('SMTP_MAIL_TO',None)
    SMTP_PASSWORD =os.getenv('SMTP_PASSWORD',None)
    SMTP_USER =os.getenv('SMTP_USER',None)

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = SMTP_MAIL_FROM

    if mail_to:
        SMTP_MAIL_TO = mail_to
    if mail_cc:
        msg['Cc'] = mail_cc

    # msg['To'] requires SMTP_MAIL_TO to be a string
    msg['To'] = SMTP_MAIL_TO
    msg.attach(MIMEText(message,'html'))

    if file_to_send:
        ctype, encoding = mimetypes.guess_type(file_to_send)
        if ctype is None or encoding is not None:
            ctype = "text/*"

        maintype, subtype = ctype.split("/", 1)

        if not 'xlsx' in file_to_send:
            with open(file_to_send, encoding='utf-8') as fp:
                attachment = MIMEText(fp.read(), _subtype='subtype')
                # encoders.encode_base64(attachment)
                attachment.add_header("Content-Disposition","attachment", filename=filename)
                msg.attach(attachment)
        else:
            with open(file_to_send,'rb') as fp:
                # attachment = MIMEText(fp.read(), _subtype='xlsx')
                attachment = MIMEBase('application', "octet-stream")
                attachment.set_payload(open(file_to_send, "rb").read())
                encoders.encode_base64(attachment)
                attachment.add_header("Content-Disposition","attachment", filename=f'{filename}.xlsx')
                msg.attach(attachment)

    with smtplib.SMTP(SMTP_HOST,SMTP_TLS_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(SMTP_USER, SMTP_PASSWORD)

        # sendmail requires SMTP_MAIL_TO to be a list
        smtp.sendmail(SMTP_MAIL_FROM, SMTP_MAIL_TO.split(','), msg.as_string())


def read_gsheet(subsheet_id, subsheet_name):
    """Read google sheet using google cloud credentials

    Args:
        subsheet_id (str): Id of the subsheet to read, can be found in sheet url.
        subsheet_name (str): Name of the subsheet to read
    Returns:
        Dataframe(DF): Dataframe of respective sheet read
    """
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    sheet_id = subsheet_id
    subsheet_name = subsheet_name

    # access the json key 
    credentials = ServiceAccountCredentials.from_json_keyfile_name( 
        os.getenv('api_keys'), scopes)  
    
    # authenticate the JSON key with gspread
    auth_file = gspread.authorize(credentials)
    sheet = auth_file.open_by_key(sheet_id)
    gsheet_df = pd.DataFrame(sheet.worksheet(subsheet_name).get_all_records())

    return gsheet_df

def get_engine():   

    user =  os.getenv('user')
    password = os.getenv('password')
    host = os.getenv('host')
    port = os.getenv('port')
    db_name = os.getenv('db_name')
    use_db = os.getenv('use_db')

    # Define PostgreSQL connection
    engine = create_engine(f'{use_db}://{user}:{password}@{host}:{port}/{db_name}')
    # postgresql+psycopg2://super:set@111.11.0.1:5432/db_test
    # Connect to PostgreSQL
    conn = engine.connect()

    return conn

