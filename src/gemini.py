from dotenv import load_dotenv
import os

import google.generativeai as genai

PROMPT1 = '''Generate a hard crossword puzzle in the style of "'''
PROMPT2 ='''" trivia.
 Generate 10 WORD/CLUE pairs in total.
 Format each WORD/CLUE pair like "WORD CLUE" with different pairs separated by newlines. Add no other characters to the formatting.
 Each WORD should be a single word.
 Each CLUE should be a phrase or a sentence'''

class Gemini:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-pro', generation_config={"temperature": 1.0})

    def generate_words_clues(self, topic):
        prompt = PROMPT1 + topic + PROMPT2
        response = self.model.generate_content(prompt)
        return response.text
        