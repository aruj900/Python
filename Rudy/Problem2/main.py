from flask.app import Flask
import requests
import json
from flask import flask

app = Flask(__name__)
@app.route('/'):
def index:
    return 'hello'

API_Key = 't6HFCz87q5uu'

Project_Token= 'to4zNSe8Gmqo'

Run_Token= 'tdT4PPQyh40s'

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{Project_Token}/last_ready_run/data', params={"api_key": API_Key})
data = json.loads(response.text)

#print(data['country'])

  
  
    
class Data:
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
			"api_key": self.api_key
		}
		self.data = self.get_data()

	def get_data(self):
		response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		data = json.loads(response.text)
		return data

	def get_country_data(self, country):
		data = self.data["country"]

		for content in data:
			if content['name'].lower() == country.lower():
				return content

		return "0"

data = Data(API_Key,Project_Token)
print(data.get_country_data("India"))
    