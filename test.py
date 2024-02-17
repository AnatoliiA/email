from utils import  send_one_email
from utils.bookworks import insertpass


# content = read_html_content()
# print(content)

def is_file_in_use(file_path):
    try:
        with open(file_path, 'a') as file:
            pass
    except IOError:
        return True
    return False

if is_file_in_use('pdf/temp.docx'):
    print("The file is in use.")
else:
    print("The file is not in use.")

# replacements = {'nom': "name", "ent" : "company", "sex": "sex", "about": ""}
# create_pdf_from_template('pdf/letterpresent.docx', 'pdf/LettrePrésentationKamarali.pdf', replacements)

# send_one_email("content", " Christian Bessard".title(), "Etablissements Techniques Fragnière SA", 1, "kamaralia@gmail.com")
insertpass("Etablissements Techniques Fragnière SA", "Etablissements Techniques Fragnière SA", "kamaralia@gmail.com", "kamaralia@gmail.com", "Kamarali", "Kamarali", "06.06.06.06.06", "kamaralia@gmail.com")