import fitz  # PyMuPDF
import re

class BillExtractor:
    """
    Extracts units (kWh, Liters) from electricity and water bills.
    """
    
    @staticmethod
    def extract_text(pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    @staticmethod
    def parse_electricity(text):
        """
        Parses kWh from electricity bills using regex patterns.
        """
        # Look for patterns like "Units Consumed: 123", "Usage: 123 kWh", etc.
        patterns = [
            r'(\d+(?:\.\d+)?)\s*kWh',
            r'Units\s*Consumed[:\s]*(\d+(?:\.\d+)?)',
            r'Total\s*Consumption[:\s]*(\d+(?:\.\d+)?)',
            r'Current\s*Reading.*?(\d+(?:\.\d+)?)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return float(match.group(1))
        return None

    @staticmethod
    def parse_water(text):
        """
        Parses liters or cubic meters from water bills.
        """
        # Look for "Liters", "L", "kl", "m3"
        patterns = [
            r'(\d+(?:\.\d+)?)\s*Liters',
            r'(\d+(?:\.\d+)?)\s*L\b',
            r'Consumption[:\s]*(\d+(?:\.\d+)?)\s*kL',
            r'Usage[:\s]*(\d+(?:\.\d+)?)\s*m3'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                val = float(match.group(1))
                # Convert kL or m3 to Liters
                if 'kL' in match.group(0) or 'm3' in match.group(0):
                    val *= 1000
                return val
        return None
        
    @classmethod
    def process_bill(cls, pdf_file, bill_type='electricity'):
        # Save temp file
        with open("temp_bill.pdf", "wb") as f:
            f.write(pdf_file.read())
            
        text = cls.extract_text("temp_bill.pdf")
        
        if bill_type == 'electricity':
            val = cls.parse_electricity(text)
        else:
            val = cls.parse_water(text)
            
        return val, text
