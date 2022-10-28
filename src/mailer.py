import smtplib
import ssl
import json

def bulk_mail_sender(configfile, addressfile, messagefile):
    #with open("config.json", "r") as json_file:
    with open(configfile, 'r') as json_file:
        config = json.load(json_file)
    #server = "smtp.mail.yahoo.com" 
    server = config['server']
    #print(server)
    #port = 587  
    port = config['port']
    #print(port)
    #sender_email = "sender@yahoo.com"
    sender_email = config['sender_email']
    #print(sender_email)
    
    #password = "password here"
    password = config['password']
    #print(password)
    #addresses = open('addresses.txt', 'r').readlines()
    addresses = open(addressfile,'r').readlines()
    #print(addresses)
    msg = open(messagefile, 'r').read()
    context = ssl.create_default_context()
   
    with smtplib.SMTP(server, port) as mailer:
        # Setting debug level in order to get detailed information for debuging
        mailer.set_debuglevel(1)
        mailer.starttls(context=context)
        
        # Authentication
        mailer.login(sender_email, password)

        # Sending the email
        for line in addresses:
            first_name, last_name, address = line.split('\t')
            #toaddr = address
            receiver_email = address #"receiver@yahoo.com"

            subject = "Subject: Message Subject\n"
            greeting = "Dear " + first_name + " " + last_name + ",\n"
            
            #message_body = open('test_message_body.txt', 'r').read() #"\nTest email from Python."
            message_body = msg
            signature = "\nBest Regards,\nSender Signature"

            message = subject + "\n" + greeting + "\n" + message_body + "\n" + signature
            
            mailer.sendmail(sender_email, receiver_email, message)