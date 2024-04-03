# AI-VIRTUAL-ASSISTANT
An AI virtual assistant that does various tasks based on users voice command 
Requirements:
 pyttsx3
 datetime
 speech_recognition 
 wikipedia
 smtplib
 webbrowser
 os
 pyautogui
 psutil
 pyjokes


Description:
The provided project defines a virtual assistant named "Enigma" that can perform various tasks based on voice commands. Here's a brief description of its functionality:

Initialization: It initializes the text-to-speech engine using pyttsx3 and sets the voice property.
Utility Functions:
speak(audio): This function takes an audio input and speaks it out using the initialized text-to-speech engine.
time(): It retrieves and speaks the current time.
date(): It retrieves and speaks the current date.
wishme(): Greets the user based on the current time and date.
takecommand(): Records user's voice input, converts it into text, and returns the text command.
sendemail(to, content): Sends an email to the specified recipient with the given content.
screenshot(): Takes a screenshot of the screen.
cpu(): Retrieves and speaks the current CPU usage and battery percentage.
jokes(): Tells a random joke.
Main Loop:
It continuously listens for user commands using takecommand() in a while loop.
Based on the recognized commands, it performs various tasks such as retrieving time and date, searching on Wikipedia, sending emails, searching in Chrome, performing system actions like logout, shutdown, and restart, playing songs, remembering user input, showing the remembered data, taking screenshots, displaying CPU usage, telling jokes, and going offline.
Overall, this code represents a basic virtual assistant implementation capable of performing several tasks based on voice commands provided by the user.





