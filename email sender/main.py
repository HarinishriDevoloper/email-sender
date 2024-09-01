import smtplib

MY_EMAIL = "samplepython@hotmail.com"
MY_PASSWORD = "r%u.%5*LpG8Y9,m"


with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='harini.shri13@gmail.com',
            msg=f"Subject:Happy Birthday!\n\n HI "
        )