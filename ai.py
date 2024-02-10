# We are grabbing some magic tools (libraries) to help us build our Little Assistant!
import os  # A magic tool to help us with computer stuff like finding files
import speech_recognition as sr  # A wizard's ear that can listen and understand what we say
from gtts import gTTS  # A spell to turn text into speech, like giving words a voice
import pygame  # A magic box for playing sounds and music
import openai  # A key to the library of a super smart wizard named GPT


# We need a special key (API key) to talk to the super smart wizard, GPT!
openai.api_key ="Please youse your own OPEN AI SECRET KEY"  # Remember, this key is a secret!


# Let's teach our Little Assistant how to talk!
def speak(text):
    tts = gTTS(text, lang='en')  # This spell turns text into spoken words
    filename = "response.mp3"  # We'll save the spoken words in a magic file
    tts.save(filename)  # Saving the spell into the file
    pygame.mixer.init()  # Preparing our magic sound box
    pygame.mixer.music.load(filename)  # Putting our magic file into the sound box
    pygame.mixer.music.play()  # The sound box speaks the words!
    # We wait here until the sound box is done talking
    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()  # Clearing the sound box for next time
    os.remove(filename)  # We clean up and make the file disappear

# Now let's give our Little Assistant an ear to hear us!
def listen():
    recognizer = sr.Recognizer()  # It's like a magic ear!
    with sr.Microphone() as source:  # We use a microphone to catch our words
        print("Listening for your question...")  # Little Assistant tells us it's ready to listen
        audio = recognizer.listen(source)  # It's listening...
    try:
        text = recognizer.recognize_google(audio)  # Turning our words into text
        print("You said:", text)  # Little Assistant repeats what we said
        return text
    except sr.UnknownValueError:  # Sometimes it might not understand us...
        return "Sorry, I didn't understand that."
    except sr.RequestError:  # Or there might be a hiccup in its magic.
        return "There was an error with the speech recognition service."

# Let's ask the super smart wizard GPT to help answer questions!
def ask_openai(question):
    try:
        # We send the question to GPT and wait for an answer
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=question,
            max_tokens=100  # We tell GPT to keep the answer short
        )
        return response.choices[0].text.strip()  # Here comes the answer!
    except Exception as e:  # If GPT is confused or busy, it tells us here
        return f"An error occurred with OpenAI: {str(e)}"

# The heart of our Little Assistant - where the magic happens!
def main():
    # First, Little Assistant greets us!
    initial_prompt = "Hello! I'm an AI assistant. How can I help you today?"
    print("AI:", initial_prompt)  # It shows the greeting on screen
    speak(initial_prompt)  # And says it out loud
    while True:  # This magic loop keeps our conversation going
        user_question = listen()  # It listens for our questions
        if 'goodbye' in user_question.lower():
            print("AI: Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")  # It says goodbye when we're done
            break
        ai_response = ask_openai(user_question)  # It thinks about our question
        print("AI:", ai_response)  # Shows us the answer
        speak(ai_response)  # And tells us the answer too

# This spell starts everything when we say the magic words!
if __name__ == "__main__":
    main()
