import time

print(f"[{time.strftime('%H:%M:%S')}] script started")

from openai import OpenAI
import dotenv
from instructions import initialize_instruction, image_url
from grabfromimage import image_to_json
from createfirstschedule import init_schedule
import json

print(f"[{time.strftime('%H:%M:%S')}] imports done")

api_key = dotenv.get_key(dotenv_path='.env',key_to_get='OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

goals = '''I wanna get to the gym every other day for an hour and a half every session. I also want to study for my classes. Study for harder classes for longer. I wanna spend 30m-1h studying every day.'''
time = '''I don't wanna have anything scheduled before the earliest point in my schedule. Dont have me studying before my earliest class, just eating. I also wanna be done with everything before 6:00'''

try:
    with open("json/class.json", "r") as f:
        classes = json.load(f)
    print(classes)
except:
    print('Could not load classes. Grabbing again.')
    image_to_json(image_url)

try:
    with open("json/schedule.json", "r") as f:
        schedule = json.load(f)
except:
    print('Could not load.')
    schedule = init_schedule(classes,goals,time)
    print(schedule)
    with open("json/schedule.json", "r") as f:
        json.dump(schedule,f,indent=4)

