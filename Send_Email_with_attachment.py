import smtplib
import sys
sys.path.insert(1, '/scripts')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# email = sys.argv[1]
# print(email)

# Function to send an email with body content and attachment
def send_email(sender_email, receiver_email, cc_email, subject, body, attachment_path):
    # Create a MIMEMultipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_email)
    msg['Cc'] = ', '.join(cc_email)
    msg['Subject'] = subject

    # Attach the body of the email as plain text
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="RTBS_SNOW_AWC_INC_Report.csv")
        part['Content-Disposition'] = f'attachment; filename="RTBS_SNOW_AWC_INC_Report.csv"'
        msg.attach(part)

    # Connect to the SMTP server and send the email
    try:
        smtp_server = 'smtpau.corp.riotinto.org'
        smtp_port = 25
        
        s = smtplib.SMTP(smtp_server, smtp_port)
        
       

        # Send the email
        s.sendmail(sender_email, receiver_email + cc_email, msg.as_string())
        
        # Quit the SMTP server
        s.quit()
        
        print('Mail Sent')
    except Exception as e:
        print(f"An error occurred: {e}")

Success_Mail_Send_Body_Message = '''
Hi All,

Good Day!

Sending RTBS Awaiting Customer Incidents Report. Please find attached the report.

Regards
Automation
'''

if __name__ == "__main__":
    sender_mail = 'accenture.splunk@riotinto.com'
    # receiver_mail = ['anshul.agarwal@riotinto.com', 'rati.shukul@riotinto.com']
    receiver_mail_Prod = ['Pinkey.Sahay@riotinto.com']
    # lst_email = ['anshul.agarwal@riotinto.com', 'rati.shukul@riotinto.com']
    lst_email = ['Swati.Sharma@riotinto.com', 'Arun.Chaudhary@riotinto.com', 'Dushyant.Jain@riotinto.com', 'Avik.Saha@riotinto.com', 'Goldy.Gupta@riotinto.com', 'AbhinayKumar.Kundu@riotinto.com', 'rati.shukul@riotinto.com', 'Ravissan.Markenday@riotinto.com', 'Arsheen.BanuA@riotinto.com', 'Sakitha.Maddini@riotinto.com', 'ankesh.kumar@riotinto.com', 'Shalabh.Saxena@riotinto.com', 'anshul.agarwal@riotinto.com']
    # lst_email = []
    cc_mail = lst_email 
    if len(lst_email) > 0:
        subj = "RTBS Awaiting Customer Incident Tickets Report"
        mail_message = Success_Mail_Send_Body_Message
        attachment_path = "/scripts/RTBS_SNOW_AWC_Incident_REPORT/RTBS_SNOW_AWC_INC_Report.csv"
        
        send_email(sender_mail, receiver_mail, cc_mail, subj, mail_message, attachment_path)
    else:
        subj = "RTBS Awaiting Customer Incident Tickets Report"
        mail_message = "list of usernames is empty"  
        attachment_path = "/scripts/RTBS_SNOW_AWC_Incident_REPORT/RTBS_SNOW_AWC_INC_Report.csv"
        
        send_email(sender_mail, receiver_mail, cc_mail, subj, mail_message, attachment_path)
        
    
    
    
