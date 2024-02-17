from utils.send_one_letter import send_one_email
from utils import read_html_content



def main():
    name_person = ""
    surname_person = ""
    reciver = "kamaralia@gmail.com"
    email_company = ""
    website = ""
    phone_company = ""
    phone_person = ""
    content = read_html_content()
    send_one_email(content, name_person, "Synergie AS", 1,
                   reciver, email_company, website, phone_company,
                   surname_person, phone_person)


if __name__ == "__main__":
    main()
