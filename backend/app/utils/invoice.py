from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), '..', 'templates')

def render_invoice_html(invoice, booking, customer):
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    tpl = env.get_template('invoice.html')
    return tpl.render(invoice=invoice, booking=booking, customer=customer)

def html_to_pdf_bytes(html_str):
    return HTML(string=html_str).write_pdf()
