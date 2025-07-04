from openai import OpenAI
import dotenv
from instructions import initialize_instruction, image_url
from grabfromimage import image_to_json
import json

api_key = dotenv.get_key(dotenv_path='.env',key_to_get='OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def init_schedule(classes,goals,time):
    class_json = json.dumps(classes)
    form_sched = client.responses.create(
        model="o4-mini",
        instructions=initialize_instruction,
        input=[
            {   
                "role": "user",
                "content": [

                {"type":"input_text",
                    "text": goals},
                {"type":"input_text",
                    "text": time},
                {
                    "type":"input_text",
                    "text": class_json
                }]}]
    )
    return form_sched.output[0].content[0].text

