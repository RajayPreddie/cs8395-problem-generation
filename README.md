# cs8395-problem-generation

## Problem Generator for Testing ChatGPT
Currently, the problem generator creates 100 problems specifically for the
testing ChatGPT's ability to find the first-error in python programs.

###  Coding Problems
The coding problems are contained in the coding_problems folder. Each problem is
in a json file (e.g, problem_1.json). Here is an example problem: 
```
{
    "id": "problem_1",
    "code": "\ndef find_missing_number(sequence):\n    \"\"\"\n    This function finds the missing number in a list of consecutive numbers.\n    \"\"\"\n    sequence.sort()\n    start = sequence[0]\n    for i in range(len(sequence)):\n        if sequence[i] != start + i:\n            return start + i\n    return None\n\ndef main():\n    \"\"\"\n    Main function that uses the find_missing_number function to find the missing number.\n    \"\"\"\n    numbers = [1, 2, 4, 5, 6]\n    missing_number = find_missing_number(numbers)\n    print(f\"The missing number is: {missing_number}\")\n\nif __name__ == \"__main__\":\n    main()\n",
    "prompt": "As a novice programmer, your task is to create a Python program that intentionally contains an error. Your challenge is to ensure that the error does not lead to an infinite recursion or an infinite loop. The program should not require any user input. Additionally, avoid including any comments that suggest there is an error. In your comments, act as if the code works perfectly.To make your Python program unique and interesting, consider using the following keyword(s) as inspiration. The keyword(s) should guide the overall theme, functionality, or structure of your program, making it both practical and distinctive: list. For instance, think of innovative ways to incorporate the keyword(s) into the python program idea. The keyword(s) act as a foundation for crafting a Python program that someone might genuinely find useful or intriguing, while subtly introducing an error that is not immediately obvious. The ultimate goal is to create a Python program that is both practical and distinctive, drawing inspiration from the provided keyword(s) to set it apart from typical programming solutions. Remember to only respond with the raw code for the Python program. Generate a Python program that uses the keyword(s) for inspiration on the type of problem to solve. Only return the code that you would write in a .py file. Here are additional specifics. Do not output in Markdown format. Exclude code comments from the code.",
    "tags": [
        "list",
        "Easy"
    ],
    "keywords": [
        "list"
    ],
    "difficulty": "Easy"
}
```

### Constants
The constants folder contains the keywords.py file which contains 100 a list of 100 keywords. The keywords are originally from this [Chat Link](https://chat.openai.com/share/56829880-fc4f-4a9d-8bda-ea17fed2087d).

