from flask import Flask
import youtube_play as yp
app = Flask(__name__)

@app.route('/<query>')
def get_link(query):
    return yp.link_from_input_query(query)

if __name__ == '__main__':
   app.run()