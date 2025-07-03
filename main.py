from openai import OpenAI
import dotenv
from instructions import initialize_instruction, image_url
from grabfromimage import image_to_json
import os
import json

api_key = dotenv.get_key(dotenv_path='.env',key_to_get='OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

goals = '''I wanna get to the gym every other day for an hour and a half every session. I also want to study for my classes. Study for harder classes for longer. I wanna spend 30m-1h studying every day.'''
time = '''I don't wanna have anything scheduled before the earliest point in my schedule. Dont have me studying before my earliest class, just eating. I also wanna be done with everything before 6:00'''

def init_schedule(classes):
    form_sched = client.responses.create(
        model="o4-mini",
        instructions=initialize_instruction,
        input=[
            {   
                "role": "user",
                "content": [

                {"type":"input_text",
                    "text": goals},
                {
                    "type":"input_text",
                    "text": classes
                            }]}]
    )
    print(form_sched.output[0].content[0].text)


try:
    with open("class.json", "r") as f:
        classes = json.load(f)
except:
    print('Could not load.')

if not classes:
    image_to_json(image_url)

try:
    with open("schedule.json", "r") as f:
        schedule = json.load(f)
except:
    print('Could not load.')

if not schedule:
    print('No schedule found.')
    init_schedule(classes)
