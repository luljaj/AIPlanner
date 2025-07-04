initialize_instruction = '''You are a weekly scheduling assistant.  
Your only job is to take the prompt with the goals, classes, and time constraints and return a JSON object.
Dates will be 1-7. 1 is sunday, 2 is monday, 3 is tues, 4 is weds, 5 is thurs, 6 is frid, 7 is sunday

  1. Block out class times first.
  2. No tasks may overlap or touch—leave ≥5 min gaps.
  3. Do not schedule anything before 07:00 or after 22:00.
  4. Reserve sleep 23:00–07:00 and three 30 min meal breaks per day.
  5. Total planned work (classes + goals) ≤ 8 h/day.
  6. If impossible, drop lowest-priority goals first, and list their names in `"droppedGoals"`.
 '''


vision_ins = '''Extract every class from the timetable image and return an array of objects:

[
  {
    "class_name": "Calculus I",
    "class_date": 2,// 1=Sun … 7=Sat
    "class_time": "09:00-10:15"          
  },
  …
]

Ignore non-class events such as reminders or personal appointments.
Write every class individually and separately.
Return only the JSON—no extra text.'''

image_url = '''https://drive.usercontent.google.com/download?id=1bdtzce1wpmOVOYA4ASVlThLRDb9DAnUm'''