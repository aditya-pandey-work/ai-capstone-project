import pdfplumber

def extract_pdf(loc):

    path = f"/home/lap-49/Documents/ai-proj-capstone/doc/{loc}"
    pages = []

    with pdfplumber.open(path) as pdf: 
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            if text:
                pages.append({
                    "text": text, 
                    "metadata": {
                        "page": i+1, 
                        "access_role": "employee"
                    }
                })
    
    return pages