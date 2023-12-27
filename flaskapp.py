import os
from flask import Flask, render_template, request

from src.selenium import Selenium
from src.gemini import Gemini

app = Flask(__name__)

gem = Gemini()
sel = Selenium()

# Set google creds for remote server
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "service_account.json"

DEBUG=False
TEST_STR = '''FIRM The law firm of main character Mitch McDeere
VESPER Client of Rudy Baylor who's paralyzed in the novel The Rainmaker
CALLMISTER Bruce Cable, the main villain from The Client
ROI A landowner who's murdered in The Testament
ROARKE Kristin Carlisle's son, and Michael Brock's adopted son, from The Appeal
BRUIN Katherine "Kay" Hall, a young attorney from The Firm
CANCELLATO A scientist and son of a Senator, Jimmy Black, from The Runaway Jury
KANE Judge from The Pelican Brief
RILEY A waitress who testifies against Steven Cord and is killed by hitmen in The Client
CHARLIE A boy who's taken in by the Ryans of Vicksburg in The Rainmaker'''

# Defining the home page of our site
@app.route("/", methods=['GET', 'POST'])  # this sets the route to this page
def index():
    if request.method == 'POST':
        topic = request.form['submission_text']
        if DEBUG:
            words_clues_str = TEST_STR
            pass
        else:
            words_clues_str = gem.generate_words_clues(topic)
            crossword_path = sel.get_xword(words_clues_str, topic)
        print(words_clues_str)
        return render_template('submitted.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
