import smtplib
from email.message import EmailMessage
import mimetypes
import os
import base64

class Email:
	def __init__(self, sender_email: str, password: str = None, recipient: str = None, oauth_token: str = None):
		self.sender_email = sender_email
		self.password = password
		self.recipient = recipient
		self.oauth_token = oauth_token
		self.msg = EmailMessage()
		self.attachments = []
		self.smtp_server, self.port = self._detectSmtpServer(sender_email)

	def _detectSmtpServer(self, email: str):
		domain = email.split('@')[-1].lower()
		if 'gmail.com' in domain:
			return "smtp.gmail.com", 587
		elif any(x in domain for x in ['outlook.com', 'hotmail.com', 'live.com', 'office365.com']):
			return "smtp.office365.com", 587
		elif any(x in domain for x in ['icloud.com', 'me.com', 'mac.com']):
			return "smtp.mail.me.com", 587
		elif 'yahoo.com' in domain:
			return "smtp.mail.yahoo.com", 465
		else:
			return f"smtp.{domain}", 465

	def setRecipient(self, recipient_email: str):
		self.recipient = recipient_email
		self.msg["To"] = self.recipient

	def setSubject(self, subject: str):
		self.msg["Subject"] = subject

	def setContent(self, content: str):
		self.msg.set_content(content)

	def addAttachment(self, file_path: str):
		if not os.path.exists(file_path):
			print(f"⚠️ Attachment not found: {file_path}")
			return
		mime_type, _ = mimetypes.guess_type(file_path)
		if mime_type is None:
			mime_type = "application/octet-stream"
		main_type, sub_type = mime_type.split("/", 1)
		with open(file_path, "rb") as f:
			file_data = f.read()
			file_name = os.path.basename(file_path)
			self.msg.add_attachment(file_data, maintype=main_type, subtype=sub_type, filename=file_name)
			self.attachments.append(file_name)

	def _authWithOAuth2(self, server):
		"""Authenticate using OAuth2 token (Gmail / Outlook)."""
		auth_string = f"user={self.sender_email}\1auth=Bearer {self.oauth_token}\1\1"
		auth_string = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
		server.docmd('AUTH', 'XOAUTH2 ' + auth_string)

	def send(self):
		if not self.recipient:
			raise ValueError("Recipient not set. Use setRecipient().")

		use_ssl = self.port == 465
		if use_ssl:
			server = smtplib.SMTP_SSL(self.smtp_server, self.port)
		else:
			server = smtplib.SMTP(self.smtp_server, self.port)
			server.starttls()

		if self.oauth_token:
			self._authWithOAuth2(server)
		else:
			server.login(self.sender_email, self.password)

		server.send_message(self.msg)
		server.quit()

		print(f"✅ Email sent successfully to {self.recipient}")	

	def preview(self):
		attach_list = ', '.join(self.attachments) if self.attachments else 'None'
		return f"""\
From: {self.sender_email}
To: {self.recipient}
Subject: {self.msg['Subject']}
Attachments: {attach_list}
"""