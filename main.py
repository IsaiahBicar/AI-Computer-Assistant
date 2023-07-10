from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
#Might inllcude abbility to use wolfram alpha

# Speech engine initialisiation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 = male , 1 = female
activationWord = 'computer' # Single word

#choose your browser
#set the path to chrome Windows version 
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
#Alert user to an exception via speech()

def speak(text,rate = 120):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()


# Listening for commands

def parseCommand():
    listener = sr.Recognizer()
    # Parses voices into text 
    print('Listening for a command')
    
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)
        
    try:
        print('Recongizing Speech...')
        #Converts speech into text
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query

#Method to search for wikipedia
def search_wiki(query = ''):
    searchResults = wikipedia.search(query)
    if not searchResults: # not in array of resutls
        print('No results could be found')
        return 'No result received'
    try:
        wikipage = wikipedia.page(searchResults[0])
    except wikipage.Disambiguationerror as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSum = str(wikiPage.summary)
    return wikiSum

# Main Loop
if __name__ == '__main__':
    speak('All systems nominal.')
    
    while True:
        # Parse Command as a list
        query = parseCommand().lower().split()
        
        #checks activation word is first word 
        if query[0] == activationWord:
            query.pop(0)
            
            # List Commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greeting, all.')
                else:
                    query.pop(0) # Remove Say
                    speech = ' '.join(query)
                    speak(speech)
                    
            # Navigate to a website
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)
                
            #Using wikipedia
            if query[0] == 'Wikipedia':
                query = ' '.join(query[1:])
                speak('Checking the database.' )