
import keys
import openai

openai.api_key = keys.openai_key

class ChatGpt: 

  def __init__(self):
    pass


  def prompt(self, print_response = True):
    text_prompt = str(input("Enter your prompt for Chat GPT: "))
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    if(print_response):
      print(response['choices'][0]['text'])
    return(response['choices'][0]['text'])







