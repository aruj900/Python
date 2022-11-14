from flask import Flask 
import urllib.request, json
app = Flask(__name__)

@app.route("/fetch_data/<search_term>")
def fetch_google(search_term):
    url = f"https://stackoverflow.com/questions/tagged/{search_term}"
    response = urllib.request.urlopen(url)
    data = response.read()
    return data

if __name__ == "__main__":
    app.run()
    
