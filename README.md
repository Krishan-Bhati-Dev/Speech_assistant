#  Voice Assistant in Python  

A simple **Voice Assistant** built with Python that can listen to your voice commands and perform useful tasks such as telling the time, opening YouTube, searching Google, fetching Wikipedia summaries, and more.  

---

##  Features  
-  **Tells the Time** — Ask "What's the time?"  
-  **Tells the Date** — Ask "What's today's date?"  
-  **Google Search** — Say "Search" and provide a query  
-  **Open Recycle Bin** — Opens Windows Recycle Bin (safe mode, no deletion)  
-  **Play YouTube Videos** — Say "Open YouTube" or "Play" and provide a topic  
-  **Wikipedia Summary** — Get short summaries from Wikipedia  
-  **Open ChatGPT** — Opens ChatGPT in your browser  
-  **Exit** — Close the assistant with "Exit" or "Quit"  

---

##  Requirements  

Make sure you have **Python 3.7+** installed. Install the dependencies using pip:  

```bash
pip install speechrecognition pyttsx3 playsound pywhatkit wikipedia pyautogui
```

⚠️ **Note:**  
- On Windows, you may also need to install [PyAudio](https://pypi.org/project/PyAudio/):  
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```

---

##  How to Run  

1. Clone this repository or copy the code into a `.py` file (e.g., `voice_assistant.py`).  
2. Open a terminal in the project folder.  
3. Run the assistant:  

   ```bash
   python voice_assistant.py
   ```

4. Speak your command after the assistant says:  
   ```
   How can I help you?
   ```

---

##  Project Structure  

```
voice-assistant/
│-- voice_assistant.py   # Main script
│-- README.md            # Project documentation
```

---

##  Example Commands  

- "What time is it?"  
- "What's today's date?"  
- "Search Python programming"  
- "Play Imagine Dragons on YouTube"  
- "Wikipedia Artificial Intelligence"  
- "Open ChatGPT"  
- "Exit"  

---

##  Notes  
- This project uses **Google Speech Recognition API**, so it requires an **internet connection**.  
- Background noise may affect accuracy — try speaking clearly.  
- The `pyttsx3` text-to-speech engine works offline.  

---

##  License  
This project is open-source and free to use for educational and personal purposes.  
