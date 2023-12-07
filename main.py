import os
import json
from openai import OpenAI
from constants.keywords import KEY_WORDS
import re

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
def create_problem_descriptions(num_problems=100):
    problem_descriptions = []

    easy_ratio, medium_ratio = 0.5, 0.3
    num_easy = int(num_problems * easy_ratio)
    num_medium = int(num_problems * medium_ratio)
    num_hard = num_problems - num_easy - num_medium

    for index in range(num_problems):
        cur_keywords = [KEY_WORDS[index % len(KEY_WORDS)]]

        if index < num_easy:
            problem_difficulty = "Easy"
        elif index < num_easy + num_medium:
            problem_difficulty = "Medium"
            cur_keywords.append(KEY_WORDS[(index + 1) % len(KEY_WORDS)])
        else:
            problem_difficulty = "Hard"
            cur_keywords.extend([KEY_WORDS[(index + 1) % len(KEY_WORDS)], KEY_WORDS[(index + 2) % len(KEY_WORDS)]])

        tags = cur_keywords.copy()
        tags.append(problem_difficulty)

        problem_description = {
            "id": f"problem_{index + 1}",
            "code": "",
            "prompt": "",
            "tags": tags,
            "keywords": cur_keywords,
            "difficulty": problem_difficulty,
        }

        problem_descriptions.append(problem_description)

    return problem_descriptions

def create_coding_problems_from_problem_descriptions(problem_descriptions):
  abs_directory_path = os.path.join(os.getcwd(), 'coding_problems')
  if not os.path.exists(abs_directory_path):
    os.makedirs(abs_directory_path)
  
  for idx, problem_description in enumerate(problem_descriptions):
  
    
    chatgpt_prompt = f"As a novice programmer, your task is to create a Python program that intentionally contains an error. Your challenge is to ensure that the error does not lead to an infinite recursion or an infinite loop. The program should not require any user input. Additionally, avoid including any comments that suggest there is an error. In your comments, act as if the code works perfectly.To make your Python program unique and interesting, consider using the following keyword(s) as inspiration. The keyword(s) should guide the overall theme, functionality, or structure of your program, making it both practical and distinctive: {','.join(problem_description['keywords'])}. For instance, think of innovative ways to incorporate the keyword(s) into the python program idea. The keyword(s) act as a foundation for crafting a Python program that someone might genuinely find useful or intriguing, while subtly introducing an error that is not immediately obvious. The ultimate goal is to create a Python program that is both practical and distinctive, drawing inspiration from the provided keyword(s) to set it apart from typical programming solutions. Remember to only respond with the raw code for the Python program. Generate a Python program that uses the keyword(s) for inspiration on the type of problem to solve. Only return the code that you would write in a .py file. Here are additional specifics. Do not output in Markdown format. Exclude code comments from the code."
    # Make an API request to ChatGPT
    
    response = client.chat.completions.create(
      model="gpt-4-1106-preview", 

        messages=[
        {
            "role": "user",
            "content": chatgpt_prompt,
        }
    ],
    
      max_tokens=2000,
      n=1,
      stop=None,
      temperature=0.5
    ) 
    # Save the response to a file
    filename = f"{problem_description['id']}.json"
    full_path = os.path.join(abs_directory_path, filename)
    code = response.choices[0].message.content
    pattern = r'```python(.*?)```'
     # Find the first code block in the input string
    match = re.search(pattern, code, re.DOTALL)
    
    # Extract the inner part of ```python...```
    if match:
      code = match.group(1)  #
    with open(full_path, 'w') as file:
      problem_description["code"] = code
      problem_description["prompt"] = chatgpt_prompt
      json_object = json.dumps(problem_description
         , indent=4)
      file.write(json_object)
      file.close()  # Close the file
    idx += 1

problem_descriptions = create_problem_descriptions()
print("PROBLEM DESCRIPTIONS CREATED")
create_coding_problems_from_problem_descriptions(problem_descriptions)


    
    
