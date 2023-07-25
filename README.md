# Voice-Activated Assistant

This is a Python script for a voice-activated assistant that performs various tasks such as speech recognition, web browsing, Wikipedia searching, and note-taking. The assistant uses the `speech_recognition`, `pyttsx3`, `webbrowser`, and `wikipedia` libraries.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `wikipedia`

You can install these libraries using `pip`:

```
pip install speech_recognition pyttsx3 webbrowser wikipedia
```

Also, ensure that you have Google Chrome installed on your system as the default browser.

## Usage

1. Run the script using Python:
   ```
   python voice_assistant.py
   ```
   
2. The assistant will start listening for a command. You need to say "computer" (the activation word) followed by your command.

3. Available commands:

   - **Say**: Speak a text phrase. For example:
     ```
     computer say hello
     ```
     The assistant will greet you by saying "Greeting, all."
     
     ```
     computer say How are you?
     ```
     The assistant will speak the provided text.
     
   - **Go to**: Open a website in Google Chrome. For example:
     ```
     computer go to example.com
     ```
     The assistant will open the website "example.com" in a new Chrome tab.
     
   - **Wikipedia**: Search for a query on Wikipedia. For example:
     ```
     computer Wikipedia Albert Einstein
     ```
     The assistant will search for "Albert Einstein" on Wikipedia and provide a summary of the page.
     
   - **Log**: Record a note in a text file. For example:
     ```
     computer log This is a sample note.
     ```
     The assistant will save the note in a text file with the current timestamp (e.g., `note_2023-07-10-12-34-56.txt`).
     
   - **Exit**: Terminate the assistant. For example:
     ```
     computer exit
     ```
     The assistant will say "Goodbye" and stop running.

Note: The assistant requires a working microphone to receive voice commands.

## Customization

You can customize the assistant by modifying the code:

- **Activation Word**: Change the activation word by modifying the `activationWord` variable. For example, you can set it to "assistant" instead of "computer":
  ```
  activationWord = 'assistant'
  ```

- **Voice Selection**: By default, the assistant uses a male voice. If you prefer a female voice, change the `voices[0].id` to `voices[1].id` in the following line:
  ```
  engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
  ```

- **Web Browser**: The script uses Google Chrome as the default browser. If you prefer a different browser, modify the `chrome_path` variable to the appropriate browser executable path.

## Troubleshooting

- If the assistant fails to recognize your command, ensure that your microphone is properly connected and working. You may also need to adjust the microphone volume or sensitivity settings.

- If the assistant is unable to find or open a website, make sure you have a stable internet connection and the website's URL is correct.

- If the Wikipedia search does not return any results, verify that the search query is valid and try different variations or keywords.

- If you encounter any issues or exceptions, make sure you have the required libraries installed and up to date. Check the documentation of each library for troubleshooting information.

## Limitations

- The assistant relies on an internet connection to perform web browsing and Wikipedia searches.

- The assistant's speech recognition accuracy depends on the quality of the audio input and the ambient noise. It may not always accurately recognize speech, especially in noisy environments.

- The assistant's functionality is limited to the provided commands. It does not have advanced natural language understanding capabilities like commercial voice assistants (e.g., Siri, Alexa).

## Future Implementations

-Add the ability for the voice assistant to do some math

-Integrate ChatGPT onto the system to allow smooth Talking.

## License

This project is licensed under the [MIT License](LICENSE).


