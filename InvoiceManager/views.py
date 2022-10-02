from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import response, HttpResponse
from django.contrib import messages
import pdfkit
from django.template.loader import get_template
import os
from django.http import FileResponse, Http404, HttpResponse

from . import settings
from .forms import ClientForm, InvoiceForm


# Health Check
def say_hello():
    return HttpResponse('Health Check Complete')


@login_required
def clientmanager(request):
    clientform = ClientForm(request.POST or None)
    print(request.POST)
    if clientform.is_valid():
        clientform.save()
        messages.success(request, "Invoice Data Saved")
        redirect("/")
    context = {'clientform': clientform}
    return render(request, 'client.html', context)


def invoicemanager(request):
    invoiceform = InvoiceForm(request.POST or None)
    print(request.POST)
    if invoiceform.is_valid():
        invoiceform.save()
        messages.success(request, "Invoice Data Saved")
        redirect("/")
    context = {'invoiceform': invoiceform}
    return render(request, 'Invoice.html', context)


def createPDF(request):
    # The name of your PDF file
    filename = 'filename.pdf'

    # HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('app/html-to-be-converted-to-pdf.html')

    # Add any context variables you need to be dynamically rendered in the HTML
    context = {}
    context['name'] = 'URIEL'
    context['surname'] = 'Technologies'

    # Render the HTML
    html = template.render(context)

    # Options - Very Important [Don't forget this]
    options = {
        'encoding': 'UTF-8',
        'javascript-delay': '1000',  # Optional
        'enable-local-file-access': None,  # To be able to access CSS
        'page-size': 'A4',
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
    }

    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    # IF you have CSS to add to template
    css1 = os.path.join(settings.STATIC_ROOT, 'css', 'app.css')
    css2 = os.path.join(settings.STATIC_ROOT, 'css', 'bootstrap.css')

    # Saving the File
    filepath = '/absolute/path/to/directory/where/you/want/to/save/file/'
    os.makedirs(filepath, exist_ok=True)
    pdf_save_path = filepath + filename
    # Save the PDF
    pdfkit.from_string(html, pdf_save_path, configuration=config, options=options)

    # Create the file
    file_content = pdfkit.from_string(html, False, configuration=config, options=options)

    # Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    # Return
    return response


def displaypdf(request, filename='Test.pdf'):
    file_path = settings.MEDIA_ROOT + '/upload_directory/' + filename
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')
