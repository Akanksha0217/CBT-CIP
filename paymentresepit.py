from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_receipt(customer_name, items, receipt_no):
    # PDF filename
    receipt_filename = f"Receipt_{receipt_no}.pdf"
    
    # Create a PDF document
    pdf = SimpleDocTemplate(receipt_filename, pagesize=letter)
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']
    
    # Title
    title = Paragraph("Payment Receipt", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Customer Info
    customer_info = f"Receipt No: {receipt_no}<br/>Customer Name: {customer_name}"
    customer_paragraph = Paragraph(customer_info, normal_style)
    elements.append(customer_paragraph)
    elements.append(Spacer(1, 12))
    
    # Table of items
    item_data = [["Item", "Quantity", "Price", "Total"]]
    total_amount = 0  # Initialize total amount
    
    for item in items:
        item_total = item['quantity'] * item['price']  # Calculate total for each item
        total_amount += item_total  # Add to total amount
        item_data.append([item['name'], item['quantity'], f"${item['price']:.2f}", f"${item_total:.2f}"])
    
    # Add a spacer row
    item_data.append(["", "", "", ""])
    
    # Grand Total row
    grand_total = [["", "", "", f"${total_amount:.2f}"]]
    
    # Combine items and grand total for the table
    item_data.extend(grand_total)
    
    # Table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    
    # Create the table
    item_table = Table(item_data)
    item_table.setStyle(table_style)
    elements.append(item_table)
    
    # Total Amount Paid
    total_paid = f"<br/><br/>Total Amount Paid: ${total_amount:.2f}"
    total_paid_paragraph = Paragraph(total_paid, normal_style)
    elements.append(total_paid_paragraph)
    
    # Build PDF
    pdf.build(elements)
    print(f"Receipt {receipt_no} generated successfully as {receipt_filename}.")

# Example usage
items = [
    {"name": "Laptop", "quantity": 1, "price": 999.99},
    {"name": "Mouse", "quantity": 2, "price": 25.50},
]

create_receipt("John", items, 1001)
