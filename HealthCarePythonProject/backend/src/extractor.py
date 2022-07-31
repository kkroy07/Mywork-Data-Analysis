from pdf2image import convert_from_path
import pytesseract
import util
import prescription_parser
import parser_patient_details
POPPLER_PATH=r'C:\poppler-21.11.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path,file_format):
    #extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)#convert from pdf to image
    document_text=''
    for page in pages:
        processed_image=util.preprocess_image(page)#convert RGB image to greyscale
        text = pytesseract.image_to_string(processed_image,lang='eng')
        document_text='\n'+text
    return document_text
    # if file_format=='prescription':
    #     pass # extract details from prescription
    # elif file_format == 'patient_details':
    #     pass #extract data from patient details
if __name__=='__main__':
    data=extract('../resources/prescription/pre_2.pdf','prescription')

    pp = prescription_parser.PrescriptionParser(data)
    print(pp.parse())
