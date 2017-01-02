from flask import render_template
from flask_mail import Message
from threading import Thread
from config import MAIL_SUBJECT_PREFIX, MAIL_SENDER
from app import app, mail


def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(to, subject, template, user):
	print(to)
	msg = Message(MAIL_SUBJECT_PREFIX + subject, sender=MAIL_SENDER, recipients=[to])
	msg.body = render_template(template + '.txt', user=user)
	msg.html = render_template(template + '.html', user=user)
	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr