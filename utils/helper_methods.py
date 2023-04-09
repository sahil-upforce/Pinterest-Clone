import os.path

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from cyclone.celery_task import app


def update_user_profile_picture_name(instance, filename):
    upload_path = 'profile_pictures'
    file_ext = filename.split('.')[-1]
    file_name = str(instance.user.username) + '_profile_picture_' + str(instance.user.id) + '.' + file_ext
    return os.path.join(upload_path, file_name)


def update_user_cover_picture_name(instance, filename):
    upload_path = 'cover_pictures'
    file_ext = filename.split('.')[-1]
    file_name = str(instance.user.username) + '_cover_picture_' + str(instance.user.id) + '.' + file_ext
    return os.path.join(upload_path, file_name)


@app.task
def send_mail(subject='Test Mail', to='', body='', html_template=None, context={}):
    html_page = render_to_string(template_name=html_template, context=context)
    email = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.EMAIL_HOST_USER,
        to=to,
        body=body
    )
    email.attach_alternative(content=html_page, mimetype='text/html')
    email.send()
