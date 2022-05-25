


class LoginPageConst:
    base_url = 'https://ivolunteer-app.herokuapp.com/'
    volunteer_button_login = "//button[contains(text(),'Go-Volunteer!')]"
    login_page_url = "https://ivolunteer-app.herokuapp.com/login"
    login_email_field_Xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    login_password_field_Xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]"
    user_details = {"email": "Morlove123@gmail.com", "password": '123456789'}
    login_send_button_Xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"
    slider_section_home_page = "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]"
    imgs = ["//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[1]",
            "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[2]",
            "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[3]",
            "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[4]",
            "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[5]",
            "//body/div[@id='root']/div[1]/div[1]/div[2]/section[1]/div[6]"]
    footer_div = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[4]"
    footer_nav_links = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/footer[1]/ul[1]"