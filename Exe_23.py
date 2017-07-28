# Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and
# routing e-mail between mail servers.
#
# Python provides smtplib module, which defines an SMTP client session object that
# can be used to send mail to any Internet machine with an SMTP or ESMTP listener
# daemon.
#
# Here is a simple syntax to create one SMTP object, which can later be used to send
# an e-mail:
#       import smtplib
#       smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
#
# Here is the detail of the parameters:
#    host: This is the host running your SMTP server. You can specify IP address of
#           the host or a domain name like tutorialspoint.com. This is optional argument.
#    port: If you are providing host argument, then you need to specify a port,
#           where SMTP server is listening. Usually this port would be 25.
#    local_hostname: If your SMTP server is running on your local machine, then
#           you can specify just localhost as of this option.
#
# An SMTP object has an instance method called sendmail, which is typically used to
# do the work of mailing a message. It takes three parameters:
#    The sender - A string with the address of the sender.
#    The receivers - A list of strings, one for each recipient.
#    The message - A message as a string formatted as specified in the various RFCs.
#

import smtplib
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
message = """
From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
