import os
import time
from docxtpl import DocxTemplate
from docx2pdf import convert





def get_sheet_list(workbook: object, sheet_name: str):
    """
    Returns the sheet with the given name from the workbook.
    If the sheet does not exist, creates a new sheet with the given name.

    Args:
    workbook: Workbook object
    sheet_name: Name of the sheet to retrieve or create

    Returns:
    sheet: The sheet with the given name
    """
    if sheet_name not in workbook.sheetnames:
        workbook.create_sheet(sheet_name)
    return workbook[sheet_name]


def create_pdf_from_сv(template_path_resume, output_pdf_path):
    print(template_path_resume, output_pdf_path)
    doc = DocxTemplate(template_path_resume)

    temp_docx_path = "temp.docx"
    doc.save(temp_docx_path)

    # Конвертируем временный файл в PDF
    convert(temp_docx_path, output_pdf_path)

    # Удаляем временный файл .docx
    os.remove(temp_docx_path)

    return True

def create_pdf_from_template(template_path, output_pdf_path, replacements):
    """
    Creates a PDF from a given template using the provided replacements and saves it to the specified output path.

    Args:
        template_path (str): The file path of the template.
        путь к шаблону который будет использоваться для создния временого файла
        output_pdf_path (str): The file path to save the output PDF.
        путь  к временному файлу который булет создан в результате работы функции
        replacements (dict): A dictionary containing the replacements for the template.

    Returns:
        bool: True if the PDF is successfully created, False otherwise.
    """

    # получаем путь к шаблону
    doc = DocxTemplate(template_path)
    print(template_path)
    context = {key: value for key, value in replacements.items()}
    doc.render(context)
    # путь для верменного файла
    temp_docx_path = "pdf/temp.docx"
    try:
        doc.save(temp_docx_path)
        print(doc.is_saved)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    # Give all permissions (read, write, execute) to the owner, group, and others
    try:
        os.chmod(temp_docx_path, 0o777)
        print(f"Successfully changed the permissions of {temp_docx_path}")
    except FileNotFoundError:
        print(f"The file or directory {temp_docx_path} does not exist.")
        return False
    except PermissionError:
        print(f"You do not have the permissions to change the file or directory {temp_docx_path}.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    # Конвертируем временный файл в PDF
    # ресультат конвертации в PDF будет сохранен в output_pdf_path LettrePrésentationKamarali.pdf
    convert(temp_docx_path, output_pdf_path)

    # Удаляем временный файл .docx
    os.remove(temp_docx_path)
    time.sleep(6)
    return True


# Read HTML content from the file
def read_html_content():
    # Read HTML content from the file
    with open('email/html/index.html', 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    return html_content


