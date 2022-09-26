from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

def generate(filename, title, additional_info, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line, report_table])

def generateBarChart(filename,title,body,xaxis,yaxis):
    report = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(body, styles["BodyText"])
    report_bar_chart = Drawing()

    chart = VerticalBarChart()
    chart.data = [
        (yaxis[0], yaxis[2], yaxis[4], yaxis[6], yaxis[8]),
        (yaxis[1], yaxis[3], yaxis[5], yaxis[7], yaxis[9])
    ]

    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = 250
    chart.valueAxis._valueStep = 40
    chart.groupSpacing = 0
    chart.categoryAxis.categoryNames = xaxis

    report_bar_chart.add(chart)

    report.build([report_title,report_info,report_bar_chart])


