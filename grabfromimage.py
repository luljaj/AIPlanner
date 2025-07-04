from openai import OpenAI
import dotenv
from instructions import vision_ins, image_url
import os
import json
import re

api_key = dotenv.get_key(dotenv_path='.env',key_to_get='OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def image_to_json(image_url):
    init_vision = client.responses.create(
        model="gpt-4o",
        instructions=vision_ins,
        input=[
            {   
                "role": "user",
                "content": [
                {
                    "type":"input_image",
                    "image_url":image_url
                            }]}]
    )
    result_str = init_vision.output[0].content[0].text
    print(result_str)
    try:
        cleaned = re.sub(r"```(?:json)?\n|```$", "", result_str)
        result_dict = json.loads(cleaned)
        print(result_dict)
        with open("json/class.json","w") as f:
            json.dump(result_dict,f,indent = 4)
    except Exception as e:
        print('Could not save')
    return result_str
