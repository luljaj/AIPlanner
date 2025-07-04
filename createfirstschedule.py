from openai import OpenAI
import dotenv
import json
from pydantic import BaseModel

from instructions import initialize_instruction, image_url
from grabfromimage import image_to_json
from models import ScheduleResponse

api_key = dotenv.get_key(dotenv_path='.env',key_to_get='OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def init_schedule(classes,goals,time):
    class_json = json.dumps(classes)

    user_prompt = (f'Goals {goals}, Classes {class_json}, Time {time}')
    form_sched = client.chat.completions.parse(
        model="o4-mini",
        messages=[
            {   
                "role":"system",
                "content":initialize_instruction},
            {
                "role": "user",
                "content": user_prompt}],
        response_format=ScheduleResponse,
        store = True
    )
    return form_sched.choices[0].message.parsed
