import os
import openpyxl
import time
from pathlib import Path
from datetime import datetime
from utils import create_pdf_from_template, sendemail, create_pdf_from_сv
from utils.bookworks import insertpass

current_time = datetime.now()
# Convert the datetime object to a string
current_time_str = current_time.strftime("%Y-%m-%d")
template_path_resume = 'pdf/cv.docx'
output_pdf_path = ""
output_pdf_path_resume = ""


def send_one_email(html,
                   name: str,
                   company: str,
                   sx: int,
                   receiver: str,
                   email_company: str = "None done",
                   website: str = "None done",
                   phone_company: str = "None done",
                   surname: str = "None done",
                   phone_person: str = "None done",):
    """
    принимает еmail и возвращает None предназначена для отправки емайла одному получателю

    Параметры:
    - a (int): Первое число.
    - b (int): Второе число.

    Возвращает:

    """
    try:
        sex = "Monsieur" if sx == 1 else ("Madame" if sx == 0 else "Madame, Monsieur")

        # Замены в формате {'имя': 'новое_слово'}
        current_time = datetime.now()
        # Convert the datetime object to a string
        current_time_str = current_time.strftime("%Y-%m-%d")

        html_content = html.replace('{sex}', f"{sex.capitalize()}  {name}")
        html_content = html_content.replace("{current_time_str}", str(current_time_str))
        replacements = {'nom': name, "ent": company, "sex": sex, "about": ""}
        #     # Создаем PDF из шаблона Word с заменами
        template_path = 'pdf/letterpresent.docx'

        output_pdf_path = f"pdf/LettrePrésentationKamarali{current_time_str}.pdf"

        try:
            create_pdf_from_template(template_path, output_pdf_path, replacements)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        # if not create_pdf_from_template(template_path, output_pdf_path, replacements):
        #     print(f"break {output_pdf_path}")

        # Путь к вашему документу Word с
        output_pdf_path_resume = f"pdf/CVKamaraliSansPhoto{current_time_str}.pdf"
        if not create_pdf_from_сv(template_path_resume, output_pdf_path_resume):
            print("break")
        # Путь к сохраненному документу PD
        path_cv = Path(r"pdf/CVKamaraliSansPhoto.pdf")
        if not os.path.exists(path_cv):
            time.sleep(6)

        #     sendemail("marc.delbreil@laposte.net", "resume", body, 'capt.jpg')

        """
           1 name_company         (str): Первый аргумент.
           2 phone_number_company (str): Второй аргумент.
           3 email_company        (str): email company
           4 website              (str): Вебсайт компании 
           5 name_persons         (str): Имя персоны
           6 surname_person       (str): Фимилия персоны
           7 phone_person         (str): Телефон персоны
           8 email_person         (str): Емайл персоны
        """
        # insertpass("company", "phone_number_company", "email_company", "website", "name_person", "surname_person",
        #            "phone_person", "email_person")
        if insertpass(company, phone_company, email_company,
                      website, name, surname, phone_person, receiver):
            print("send email and read")
            subject = "CV Kamarali Anatolii monteur solaire"
            sendemail(receiver, subject, html_content, 'capt.jpg', output_pdf_path, output_pdf_path_resume)
        else:
            print(" запись не выполенена")
    except Exception as exp:
        print(exp)


# send_one_email("", "Marc Delibreli".title(), "IFPD Foundation", 1, "webradsupport@gmail.com")