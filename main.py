# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import speech_recognition as sr
import openai

openai.api_key = "Your API KEY"

def generate_response(input_text: object) -> object:
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=input_text,
        max_tokens=50,
        temperature=0.7
    )
    print(response.choices[0].text.strip())


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)

        print("Please say something.....")

        audio = r.listen(source)

        try:
            while True:
                recognized_speech = r.recognize_google(audio)
                print("You have said : \n" + recognized_speech)
                generate_response(recognized_speech)
                print("Do you like the response answer Yes or No?")
                recognized_speech_Y_N = r.recognize_google(audio)
                if(recognized_speech_Y_N.lower() == "yes"):
                    print("Thank you")
                    break

        except Exception as e:
           print("Error : " + str(e))

if __name__ == "__main__":
    main()
