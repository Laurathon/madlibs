from flask import Flask, request, render_template
from stories import story1, story2, stories


app = Flask(__name__)


@app.route('/writeStory')
def write_story():
  """ Get request arguments from html prompt screen. Generate story with storyId that is passed through html page and write story """
  storyId = request.args["storyId"]
  story = stories[int(storyId)]
  text=story.generate(request.args)
  return render_template("story.html",text=text)

@app.route('/')
def choose_story():
  """Display two stories on page, let user pick a story """
  text=story1.generate(request.args)
  text2 = story2.generate(request.args)
  return render_template("choose_story.html", text =text, text2 =text2)

@app.route('/choose')
def select():  
  """ User chose a story, get the story id, generate the prompts from the story and display prompt screen. Pass the storyId along """
  storyId = request.args["custId"]
  story = stories[int(storyId)]
  prompts = story.prompts 
  return render_template("home.html", prompts = prompts, storyId=storyId) 

  


