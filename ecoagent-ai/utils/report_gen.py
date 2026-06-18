from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import datetime

class ReportGenerator:
    """
    Generates a professional sustainability report in PDF format.
    """
    
    @staticmethod
    def generate_pdf(data, advice, filepath):
        doc = SimpleDocTemplate(filepath, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        # Title
        elements.append(Paragraph("<b>EcoAgent AI: Personal Sustainability Report</b>", styles['Title']))
        elements.append(Paragraph(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
        elements.append(Spacer(1, 20))

        # Executive Summary
        elements.append(Paragraph("<b>1. Executive Summary</b>", styles['Heading2']))
        score = data['score']
        elements.append(Paragraph(f"Sustainability Score: {score['score']}/100 (Grade: {score['grade']})", styles['Normal']))
        elements.append(Paragraph(f"Total Monthly CO2e: {data['footprint']['total']} kg", styles['Normal']))
        elements.append(Spacer(1, 12))

        # Data Table
        elements.append(Paragraph("<b>2. Consumption Breakdown</b>", styles['Heading2']))
        table_data = [
            ['Category', 'Input Value', 'CO2e Impact (kg)'],
            ['Electricity', f"{data['inputs']['elec_kwh']} kWh", f"{data['footprint']['breakdown']['Electricity']}"],
            ['Water', f"{data['inputs']['water_liters']} L", f"{data['footprint']['breakdown']['Water']}"],
            ['Travel', f"{data['inputs']['travel_km']} km ({data['inputs']['transport_mode']})", f"{data['footprint']['breakdown']['Travel']}"]
        ]
        t = Table(table_data, colWidths=[150, 150, 150])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.green),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(t)
        elements.append(Spacer(1, 20))

        # AI Recommendations
        elements.append(Paragraph("<b>3. Personalized Recommendations</b>", styles['Heading2']))
        # Split advice into paragraphs
        res_lines = advice.split('\n')
        for line in res_lines:
            if line.strip():
                elements.append(Paragraph(line, styles['Normal']))
        
        elements.append(Spacer(1, 20))
        elements.append(Paragraph("<i>Aligned with SDG 7, 12, and 13.</i>", styles['Normal']))

        # Build PDF
        doc.build(elements)
        return filepath
        
