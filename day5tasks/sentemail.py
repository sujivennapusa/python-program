import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("sujivennapusa2000@gmail.com","suji1806")
message="hello all"
connection.sendmail("sujivennapusa2000@gmail.com","vennapusasuji463@gmail.com",message)
print("email sent successfully")
connection.quit()