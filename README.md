# Overview - Weather Bot

[Rasa](https://rasa.com/docs/rasa/) is an open source machine learning framework for building conversational AI, consisting of Rasa NLU and Rasa Core. 

I built a simple chatbot that allows you ask for the weather of a particular city or country. 

If you're bored, or need to laugh, ask the bot for a joke or something funny ("e.g. can you tell me a joke?"). Hopefully it will brighten your day. :)

## How to use

1. Clone Repository 

2. Set up virtual environment in terminal

```virtualenv -p python3 [name_of_virtual_env]``` or ```python3 -m venv /path/to/new/virtual/environment ```

3. Activate virtual environment 
``` source path_to_virtual_env/bin/activate ```

4. Install necessary packages 

```pip install -r requirements.txt```

5. Get Open Weather Map API Key 

You can get a free API key by signing in [here](https://openweathermap.org/price). Once you received the API key, set it as an environment variable. 

In Windows, _Varible_ can be set to WEATHER_API_KEY. _Value_ is the api_key.  

In linux, run this command in terminal.

``` export WEATHER_API_KEY="api_key"```

6. Run Rasa

``` rasa run actions ```. 

This runs the actions server, which runs custom actions (e.g. finding the weather through API call. More details [here](https://rasa.com/docs/rasa/2.x/custom-actions).) 

``` rasa train ```. 

This will train the model to be used in conversation. This may take some time! 

Once the model training is complete, you can run - 


``` rasa shell ```. 

A simple shell to interact with the trained model. 

## Example Dialog Flow 

**User**: "Hello" 

**Weather_bot**: "Hey, how are you?" 

**User**: "I'm doing good."

**Weather_bot**: "How can I help you?"

**User**: "What is the weather in Paris?" 

**Weather_bot**: "In Paris, it is 25C and sunny. The humidity level is..."

## Weather API 

For finding the weather, I used the [Open Weather Map API](https://openweathermap.org/api). 

## Resources 

- [Rasa Installation](https://rasa.com/docs/rasa/installation/)
- [Rasa Commands](https://rasa.com/docs/rasa/command-line-interface) 