# coding: utf-8
from . import mail
from flask import render_template, current_app
from flask_mail import Message


def send_mail(recipients, subject, template, **kwargs):
    """
    Method for sending Email.
    """
    # check if recipient was input as a string, convert it to list
    if isinstance(recipients, str):
        recipients = [recipients]
    # check if recipients was either a string nor a list, raise error
    elif not isinstance(recipients, list):
        print 'Invalid Email'

    message = Message(
        recipients=recipients,
        subject=current_app.config['MAIL_SUBJECT_PREFIX'],
        sender=current_app.config['MAIL_SENDER']
    )
    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', *kwargs)
    mail.send(message)


def allowed_image_file(filename):
    """
    Return file extensions if file is valid for upload
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in \
        current_app.config['IMAGE_ALLOWED_EXTENSIONS']


def slugify(s):
    """
    Return a slugified string from a given string
    """
    return re.sub('[^\w]+', '-', s).lower()


def paginated_object_list(template_name, query, paginate_by=20, **context):
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    paginated_object_list = query.paginate(page, paginate_by)
    return render_template(template_name,
                           paginated_object_list=paginated_object_list,
                           **context)
