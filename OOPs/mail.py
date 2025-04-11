import smtplib
import os


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def snd_mail(work_flow_name , repo_name , work_flow_run_id , workflow_run_url): 
    sender_mail = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_mail = os.getenv('RECEIVER_EMAIL')

    subject = f"Workflow {work_flow_name} failed in {repo_name}"
    body = f"Workflow {work_flow_name} failed in {repo_name}. Please check the logs for more details.\n More details : \nrun_id: {wrk_flow_run_id} \nrepo_name: {repo_name} \nworkflow_name: {wrk_flow_name} \nworkflow_run_url: {workflow_run_url} "
    



    msg = MIMEMultipart()

    msg['From'] = sender_mail
    msg['To'] = receiver_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

snd_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'), os.getenv('WORKFLOW_RUN_URL'))