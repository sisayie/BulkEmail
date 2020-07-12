import smtplib
import ssl

server = "smtp.mail.yahoo.com" 
port = 587  

sender_email = "sender@yahoo.com"
password = "password here"

addresses = open('addresses.txt', 'r').readlines()

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
        
        message_body = open('test_message_body.txt', 'r').read() #"\nTest email from Python."
        
        signature = "\nBest Regards,\nSender Signature"

        message = subject + "\n" + greeting + "\n" + message_body + "\n" + signature
        
        mailer.sendmail(sender_email, receiver_email, message)