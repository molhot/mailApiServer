import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print("=== New Mail ===")
        print("From:", mailfrom)
        print("To:", rcpttos)
        print("Data:", data.decode("utf-8", errors="replace"))
        print("================")
        return

server = CustomSMTPServer(('0.0.0.0', 1025), None)
print("Python SMTP server listening on 1025...")
asyncore.loop()
