from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.utils.safestring import mark_safe
from smtplib import SMTPException

from .forms import EmailForm


def sendEmail(request, item=None):

    messageSent = False

    if request.method == "POST":

        form = EmailForm(request.POST)

        if form.is_valid():
            try:
                cleaned_data = form.cleaned_data
                send_to = settings.DEFAULT_FROM_EMAIL
                message = cleaned_data["message"]
                subject = render_to_string(
                    "mailer/contact_email/contact_email_subject.txt",
                    {
                        "user": cleaned_data["name"],
                        "item": item,
                    },
                )

                body = render_to_string(
                    "mailer/contact_email/contact_email_body.txt",
                    {
                        "data": cleaned_data,
                        "contact_email": settings.DEFAULT_FROM_EMAIL,
                        "message": message,
                        "item": item,
                    },
                )

                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [send_to])

                messageSent = True

                messages.success(
                    request,
                    "Message Sent! -Thank You",
                )
                return redirect(reverse("home"))
            except SMTPException as e:
                messages.error(
                    request,
                    mark_safe(
                        "ERROR: failed to send message.<br/>If the issue confinues, call us on 02938 726739"
                    ),
                )
                print("message sending error:", e)

    else:
        form = EmailForm()

    template = "mailer/mailer.html"
    context = {
        "form": form,
        "messageSent": messageSent,
    }

    return render(request, template, context)
