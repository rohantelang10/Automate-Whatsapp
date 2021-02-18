import pywhatkit
print("Schedule your message to send")
number = input("Enter the sender's Mobile number(Use Country Code '+91xxxxxxxxxx')  - ")
message = input("Enter the message you want to send - ")
print("At what time you want to send? :")
hh = int(input("HH(24-hour Format) - "))
mm = int(input("MM - "))
pywhatkit.sendwhatmsg(number, message, hh, mm)