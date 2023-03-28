import openai
from utils import config_reader

API_key = config_reader('gpt', 'api_key')
openai.api_key = API_key

user_history = {}

def gpt_responce(user_id, message):
    global user_history
    if user_id not in user_history:
        user_history[user_id] = ""
    user_history[user_id] += " " + message

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistent. Answer any questions the user may have"},
                {"role": "user", "content": user_history[user_id]}])
    user_history[user_id] += " " + response["choices"][0]["message"]["content"]
    return response["choices"][0]["message"]["content"]