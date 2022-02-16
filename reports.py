#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Spacer, Paragraph


def generate_report(filepath, title, info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filepath)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(info, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line])