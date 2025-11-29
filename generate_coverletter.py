"""
PDF Cover Letter Generator
Creates a professional-looking cover letter PDF from text input.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from datetime import datetime
import json


def create_cover_letter_pdf(data, output_filename="cover_letter.pdf"):
    """
    Generate a professional cover letter PDF.
    
    Args:
        data (dict): Dictionary containing cover letter information
        output_filename (str): Name of the output PDF file
    """
    # Create the PDF document
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Style for sender information (your information)
    sender_style = ParagraphStyle(
        'SenderStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#333333',
        alignment=TA_LEFT,
        spaceAfter=6
    )
    
    # Style for recipient information
    recipient_style = ParagraphStyle(
        'RecipientStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#333333',
        alignment=TA_LEFT,
        spaceAfter=6
    )
    
    # Style for date
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#333333',
        alignment=TA_LEFT,
        spaceAfter=12
    )
    
    # Style for subject line
    subject_style = ParagraphStyle(
        'SubjectStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor='#000000',
        alignment=TA_LEFT,
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )
    
    # Style for body paragraphs
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor='#333333',
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=16
    )
    
    # Style for salutation and closing
    salutation_style = ParagraphStyle(
        'SalutationStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor='#333333',
        alignment=TA_LEFT,
        spaceAfter=12
    )
    
    # Add sender information (your contact details)
    story.append(Paragraph(f"<b>{data['sender_name']}</b>", sender_style))
    story.append(Paragraph(data['sender_address'], sender_style))
    story.append(Paragraph(data['sender_city'], sender_style))
    if 'sender_phone' in data and data['sender_phone']:
        story.append(Paragraph(f"Phone: {data['sender_phone']}", sender_style))
    if 'sender_email' in data and data['sender_email']:
        story.append(Paragraph(f"Email: {data['sender_email']}", sender_style))
    
    # Add space
    story.append(Spacer(1, 0.3*inch))
    
    # Add date
    date_str = data.get('date', datetime.now().strftime("%B %d, %Y"))
    story.append(Paragraph(date_str, date_style))
    
    # Add recipient information
    story.append(Paragraph(f"<b>{data['recipient_name']}</b>", recipient_style))
    if 'recipient_title' in data and data['recipient_title']:
        story.append(Paragraph(data['recipient_title'], recipient_style))
    story.append(Paragraph(data['company_name'], recipient_style))
    if 'company_address' in data and data['company_address']:
        story.append(Paragraph(data['company_address'], recipient_style))
    if 'company_city' in data and data['company_city']:
        story.append(Paragraph(data['company_city'], recipient_style))
    
    # Add space
    story.append(Spacer(1, 0.2*inch))
    
    # Add subject line (optional)
    if 'subject' in data and data['subject']:
        story.append(Paragraph(f"<b>Re: {data['subject']}</b>", subject_style))
    
    # Add salutation
    salutation = data.get('salutation', f"Dear {data['recipient_name']},")
    story.append(Paragraph(salutation, salutation_style))
    
    # Add body paragraphs
    body_paragraphs = data.get('body', [])
    if isinstance(body_paragraphs, str):
        # If body is a single string, split by double newlines
        body_paragraphs = body_paragraphs.split('\n\n')
    
    for paragraph in body_paragraphs:
        if paragraph.strip():  # Only add non-empty paragraphs
            story.append(Paragraph(paragraph.strip(), body_style))
    
    # Add closing
    closing = data.get('closing', 'Sincerely,')
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(closing, salutation_style))
    
    # Add space for signature
    story.append(Spacer(1, 0.5*inch))
    
    # Add sender name again for signature
    story.append(Paragraph(f"<b>{data['sender_name']}</b>", sender_style))
    
    # Build the PDF
    doc.build(story)
    print(f"Cover letter PDF created successfully: {output_filename}")


def load_from_json(json_file):
    """Load cover letter data from a JSON file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)


# Example usage
if __name__ == "__main__":
    # Example data structure
    example_data = {
        "sender_name": "John Doe",
        "sender_address": "123 Main Street",
        "sender_city": "New York, NY 10001",
        "sender_phone": "+1 (555) 123-4567",
        "sender_email": "john.doe@email.com",
        
        "date": datetime.now().strftime("%B %d, %Y"),
        
        "recipient_name": "Jane Smith",
        "recipient_title": "Hiring Manager",
        "company_name": "Tech Solutions Inc.",
        "company_address": "456 Business Avenue",
        "company_city": "San Francisco, CA 94102",
        
        "subject": "Application for Senior Software Engineer Position",
        
        "salutation": "Dear Ms. Smith,",
        
        "body": [
            "I am writing to express my strong interest in the Senior Software Engineer position at Tech Solutions Inc. With over 8 years of experience in software development and a proven track record of delivering high-quality solutions, I am confident that I would be a valuable addition to your team.",
            
            "In my current role at Innovation Labs, I have led the development of multiple enterprise-level applications, working with technologies such as Python, Java, and cloud platforms. I have successfully managed cross-functional teams and consistently delivered projects on time and within budget. My experience aligns perfectly with the requirements outlined in your job posting, particularly in areas of system architecture, API development, and agile methodologies.",
            
            "What particularly attracts me to Tech Solutions Inc. is your commitment to innovation and your reputation for fostering a collaborative work environment. I am excited about the opportunity to contribute to your mission of delivering cutting-edge solutions to your clients. I believe my technical expertise, combined with my strong communication skills and passion for continuous learning, would enable me to make meaningful contributions to your team.",
            
            "I would welcome the opportunity to discuss how my background, skills, and enthusiasm align with the needs of your team. Thank you for considering my application. I look forward to hearing from you soon."
        ],
        
        "closing": "Sincerely,"
    }
    
    # Generate the PDF
    create_cover_letter_pdf(example_data, "cover_letter_example.pdf")
    print("\nExample cover letter generated successfully!")
    print("You can customize the content by modifying the data dictionary or loading from a JSON file.")
