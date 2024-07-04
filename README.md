
---

# Jarvis desktop Assistant

## Introduction
Jarvis is a voice-activated personal assistant designed to perform various tasks, including fetching weather updates, playing music, providing news, setting alarms, and more. The assistant utilizes the power of Python, PyQt5 for the GUI, and various APIs for different functionalities.

## Features
- Voice command recognition using `speech_recognition`.
- Text-to-speech conversion using `pyttsx3`.
- Fetching and reading news using News API.
- Fetching weather updates using Weather API.
- Playing music and videos from YouTube.
- Setting alarms.
- Performing system tasks such as opening applications, taking screenshots, and controlling system power.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```
2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API keys:**
   - Obtain API keys from the respective services (News API, Weather API, and NASA API).
   - Create a `config.py` file in the root directory and add the following:
     ```python
     NEWS_API_KEY = 'your_news_api_key'
     WEATHER_API_KEY = 'your_weather_api_key'
     NASA_API_KEY = 'your_nasa_api_key'
     ```
4. **Run the application:**
   ```bash
   python main.py
   ```

## Files and Directories
- `main.py`: Main script to run the Jarvis assistant.
- `jarbot.py`: Contains the PyQt5 UI setup.
- `config.py`: Configuration file for storing API keys.
- `requirements.txt`: List of required Python libraries.
- `alarm.py`: Script to handle alarm functionality.
- `README.md`: Documentation for the project.

## Usage
1. **Start the application:**
   ```bash
   python main.py
   ```
2. **Interact with Jarvis:**
   - Use voice commands to ask Jarvis to perform tasks such as fetching news, setting alarms, playing music, and more.
   - The GUI will display the current time and date, and animate based on the actions performed.

## Voice Commands
- "What's the time?" - Tells the current time.
- "Open Google" - Opens Google and asks for a search query.
- "Search Wikipedia for [query]" - Searches Wikipedia for the given query.
- "Play [song name]" - Plays the specified song on YouTube.
- "Tell me a joke" - Tells a joke.
- "What's the weather in [city]" - Provides the current weather for the specified city.
- "Set alarm for [time]" - Sets an alarm for the given time.
- "Tell me the news" - Reads the latest news headlines.
- "Take a screenshot" - Takes a screenshot of the current screen.
- "Shutdown the system" - Shuts down the system.
- "Restart the system" - Restarts the system.
- "Mute" - Mutes Jarvis.
- "Exit program" - Closes the Jarvis application.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README file to better suit your project's specific needs.
