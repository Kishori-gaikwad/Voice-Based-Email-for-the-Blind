import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm="sanskruti.gogirwar@gmail.com"
pwd="tbsf hcuh siyd pytv"

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        speak(str)
        audio = r.listen(source)
        try:
            text=r.recognize_google(audio)
            return text
        except Exception as e:
            print(f"Recognition Error: {e}")
            str = "Sorry could not recognize what you said"
            speak(str)

def sendmail():
    rec = "s21_gogirwar_sanskruti@mgmcen.ac.in"

    str = "Please speak the body of your email"
    speak(str)
    msg = listen()

    str = "You have spoken the message"
    speak(str)
    speak(msg)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login("sanskruti.gogirwar@gmail.com", "tbsf hcuh siyd pytv")

    server.sendmail("sanskruti.gogirwar@gmail.com", "s21_gogirwar_sanskruti@mgmcen.ac.in", msg)
    server.quit()

    str = "The email has been Sent.."
    speak(str)


def readmail():
    server = e.connect("imap.gmail.com", "sanskruti.gogirwar@gmail.com", "tbsf hcuh siyd pytv")
    server.listids()

    str = "Please say the Serial Number of the email you wanna read starting from latest"
    speak(str)

    a = listen()

    if a is not None:
        if a.lower() == "two":
            a = "2"

        try:
            b = int(a) - 1
            email = server.mail(server.listids()[b])

            str = "The email is from: "
            speak(str)
            speak(email.from_addr)

            str = "The subject of the email is:"
            speak(str)
            speak(email.title)

            str = "The body of email is:"
            speak(str)
            speak(email.body)

        except ValueError:
            print(f"Invalid input: {a} is not a valid integer")
            str = "Invalid input. Please say a valid serial number."
            speak(str)
    else:
        print("Speech recognition failed. Please try again.")

def delete_email():
    server = e.connect("imap.gmail.com", "sanskruti.gogirwar@gmail.com", "tbsf hcuh siyd pytv")
    server.listids()

    str = "Please say the Serial Number of the email you want to delete starting from the latest"
    speak(str)

    a = listen()

    if a is not None:
        if a.lower() == "two":
            a = "2"

        try:
            b = int(a) - 1
            email_id = server.listids()[b]
            server.delete(email_id)

            str = "The email has been deleted."
            speak(str)

        except ValueError:
            print(f"Invalid input: {a} is not a valid integer")
            str = "Invalid input. Please say a valid serial number."
            speak(str)
        except Exception as e:
            print(f"Error deleting email: {e}")
            str = "Error deleting email. Please try again."
            speak(str)
    else:
        print("Speech recognition failed. Please try again.")


str = "Welcome to voice controlled email service"
speak(str)
str = "I am your email assistant"
speak(str)

while(1):

    str = "What do you want to do?"
    speak(str)

    str=" Speak compose to Send       Speak OPEN to Read Inbox       Speak DELETE EMAIL to delete       Speak EXIT TO Exit"
    speak(str)

    ch = listen()

    if (ch=='compose'):
        str = "You have chosen to send an email"
        speak(str)
        sendmail()

    elif (ch=='open'):
        str = "You have chosen to read email"
        speak(str)
        readmail()

    elif (ch=='delete email'):
        str = "You have chosen to delete an email"
        speak(str)
        delete_email()

    elif (ch=='exit'):
        str = "You have chosen to exit"
        speak(str)
        str = "Have a great day, Bye"
        speak(str)
        exit(1)

    else:
        str = "Invalid choice, you said:"
        speak(str)
        speak(ch)
