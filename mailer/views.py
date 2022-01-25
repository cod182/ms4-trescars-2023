from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.utils.safestring import mark_safe
from smtplib import SMTPException

from .forms import email_form


def handle_send_email(request, form, item):
    messageSent = False
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

        return messageSent

    except SMTPException as e:
        messages.error(
            request,
            mark_safe(
                "ERROR: failed to send message.<br/>If the issue confinues, call us on 02938 726739"
            ),
        )
        print("message sending error:", e)

        return messageSent


def send_email(request, item=None):
    messageSent = False

    if request.method == "POST":
        form = email_form(request.POST)

        if form.is_valid():
            messageSent = handle_send_email(request, form, item)
            if messageSent:
                return redirect(reverse("home"))
    else:
        form = email_form()

    template = "mailer/mailer.html"
    context = {
        "form": form,
        "messageSent": messageSent,
    }

    return render(request, template, context)
