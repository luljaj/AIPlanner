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
    return form_sched.output[1].content[0].text


Response(id='resp_6867e387bc988198812cf995745ada5f0383fcaf7591af88', created_at=1751638919.0, error=None, incomplete_details=None, instructions='You are a weekly scheduling assistant.  \nInputs:\n- classes: list of {name, day (1–7), start, end}  \n- goals: list of {name, duration, day_preferences (list[int] | null), priority(int)}  \n\nProduce **plain-text** output sorted by day (1-7) then start time, one task per line, e.g.  \n`2 09:00-10:15  Calculus`  \n\nRules (in order of importance)  \n1. Block out class times first.  \n2. No task may overlap or touch another; leave ≥5 min gaps.  \n3. Do not schedule anything before 07:00 or after 22:00.  \n4. Reserve sleep 23:00-07:00 and three 30 min meal breaks per day.  \n5. Total planned work (classes + goals) ≤8 h per day.  \n6. If impossible, drop lowest-priority goals first and list which were dropped.  ', metadata={}, model='o4-mini-2025-04-16', object='response', output=[ResponseReasoningItem(id='rs_6867e388ad648198a5d00edce4a1aace0383fcaf7591af88', summary=[], type='reasoning', encrypted_content=None, status=None), ResponseOutputMessage(id='msg_6867e3b4f13081988362cb0a62a23e0c0383fcaf7591af88', content=[ResponseOutputText(annotations=[], text='1 08:00-08:30 Meal: Breakfast  \n1 10:00-11:15 Prog & Hardware Fundamentals  \n1 11:20-11:50 Meal: Lunch  \n1 12:00-13:15 Differential Calc  \n1 12:00-13:15 Integral Calculus-WATSON  \n1 13:20-14:50 Gym  \n1 15:00-16:15 Inquiry and Academic Writing  \n1 16:20-17:20 Study Prog & Hardware Fundamentals  \n1 17:25-17:55 Meal: Dinner  \n\n2 08:00-08:30 Meal: Breakfast  \n2 10:00-11:15 Intro To Architecture (LEC)  \n2 11:20-11:50 Meal: Lunch  \n2 11:55-12:40 Study Intro To Architecture  \n2 15:00-16:15 Inquiry and Academic Writing  \n2 16:20-16:50 Meal: Dinner  \n\n3 08:00-08:30 Meal: Breakfast  \n3 10:00-11:15 Prog & Hardware Fundamentals  \n3 11:20-11:50 Meal: Lunch  \n3 12:00-13:15 Differential Calc  \n3 12:00-13:15 Integral Calculus-WATSON  \n3 13:20-14:50 Gym  \n3 14:55-15:25 Study Prog & Hardware Fundamentals  \n3 16:00-17:15 Prof Skills Ethics & CS Trends  \n3 17:20-17:50 Meal: Dinner  \n\n4 08:00-08:30 Meal: Breakfast  \n4 10:00-11:15 Intro To Architecture (LEC)  \n4 11:20-11:50 Meal: Lunch  \n4 12:30-13:45 Prog & Hardware Fundamentals  \n4 13:50-14:35 Study Prog & Hardware Fundamentals  \n4 15:00-16:15 Inquiry and Academic Writing  \n4 16:20-16:50 Meal: Dinner  \n\n5 08:00-08:30 Meal: Breakfast  \n5 10:00-11:15 Prog & Hardware Fundamentals  \n5 11:20-11:50 Meal: Lunch  \n5 12:00-13:15 Differential Calc  \n5 12:00-13:15 Integral Calculus-WATSON  \n5 13:20-14:50 Gym  \n5 14:55-15:55 Study Prog & Hardware Fundamentals  \n5 16:00-16:30 Meal: Dinner  \n\n6 08:00-08:30 Meal: Breakfast  \n6 12:00-12:30 Meal: Lunch  \n6 12:35-13:05 Study (General)  \n6 17:00-17:30 Meal: Dinner  \n\n7 08:00-08:30 Meal: Breakfast  \n7 08:35-10:05 Gym  \n7 12:00-12:30 Meal: Lunch  \n7 12:35-13:05 Study (General)  \n7 17:00-17:30 Meal: Dinner  \n\nNo goals were dropped.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message')], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[], top_p=1.0, background=False, max_output_tokens=None, max_tool_calls=None, previous_response_id=None, prompt=None, reasoning=Reasoning(effort='medium', generate_summary=None, summary=None), service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text')), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=789, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=5590, output_tokens_details=OutputTokensDetails(reasoning_tokens=4928), total_tokens=6379), user=None, store=True)