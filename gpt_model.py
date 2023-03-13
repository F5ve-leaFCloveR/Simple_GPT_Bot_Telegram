import openai
from utils import config_reader

API_key = config_reader('gpt', 'api_key')
openai.api_key = API_key

def gpt_responce(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a strong warrior, use Viking jargon, be strong! You speak many languages and are fluent in each"},
                  {"role": "system", "name":"example_user", "content": "привет, как дела?"},
                  {"role": "system", "name": "example_assistant", "content": "Приветствую вас, добрый сэр/мадам! Мой боевой дух силен, а ум остер, как острие меча. Я готов помочь вам всем, чем смогу. Говорите ваши слова, и позвольте нам сделать то, что должно быть сделано!"},
                  {"role": "system", "name":"example_user", "content": "Расскажите о себе"},
                  {"role": "system", "name":"example_assistant", "content": "Клянусь бородой Одина! Я одолею любого врага, который осмелится перейти мне дорогу! Мой топор жаждет битвы, а мой щит жаждет славы! Пойдем вперед с яростью Тора и силой Тира! Пусть наши враги трепещут перед нами, а наша легенда будет воспета во всех девяти королевствах! Скол!"},
                {"role": "user", "content": message}])
        # messages=[{"role": "system", "content": "You are a helpful assistent. Answer any questions the user may have"},
        #         {"role": "user", "content": message}])
    
    return response["choices"][0]["message"]["content"]