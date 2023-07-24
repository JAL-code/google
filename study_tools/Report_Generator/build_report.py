from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Define your example text and references
example_text = [
    "Paragraph 1: DDR4 is a type of RAM commonly used in computers.",
    "Paragraph 2: DDR5 is the next-generation RAM technology, offering improved performance over DDR4.",
    "Paragraph 3: DDR4 operates at lower frequencies compared to DDR5.",
    "Paragraph 4: DDR5 provides higher bandwidth and faster data transfer rates than DDR4.",
    # Add more paragraphs as needed...
]

references = [
    "Reference 1: Smith, J. (2021). A Comparison of DDR4 and DDR5 RAM Technologies.",
    "Reference 2: Johnson, A. (2020). Understanding the Advantages of DDR5 RAM.",
    # Add more references as needed...
]

# Generate the PDF
def generate_pdf():
    doc = SimpleDocTemplate("comparison.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    story = []
    styles = getSampleStyleSheet()

    # Add paragraphs with numbered headings
    for i, text in enumerate(example_text, start=1):
        paragraph = Paragraph(f"<b>Paragraph {i}:</b> {text}", styles["Normal"])
        story.append(paragraph)
        story.append(Spacer(1, 12))  # Add spacing between paragraphs

    # Add references in the third column
    for reference in references:
        paragraph = Paragraph(reference, styles["Normal"])
        story.append(Spacer(1, 6))  # Add spacing between references
        story.append(paragraph)

    doc.build(story)

generate_pdf()
