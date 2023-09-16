#Importando blibioteca
from botcity.document_processing import *

def lerPDF(arquivo):
    reader = PDFReader()
    parser = reader.read_file(r"C:\Users\gomes\Documents\Code\lerPDF\docs\Contoso_INVOICE_TailSpin.pdf")
    
    _date = parser.get_first_entry("Date:")
    value = parser.read(_date, 1.214286, -1.5, 3.452381, 3.1)
    print(f"Date: {value}")
    
    _bill_to = parser.get_first_entry("Bill to:")
    value = parser.read(_bill_to, 1.314815, -2.2, 5.62963, 4.4)
    print(f"Bill to: {value}")
    
    _contact = parser.get_first_entry("Contact:")
    value = parser.read(_contact, 1.236842, -1, 4.802632, 2.8)
    print(f"Contact: {value}")
    
    _balance_due = parser.get_first_entry("Balance due:")
    value = parser.read(_balance_due, 1.126667, -1.666667, 1.76, 3.5)
    print(f"Balance due: {value}")
    
lerPDF()