from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('First Project - Weather App!')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x100")
root.configure(background='White')

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=25B51173-4EBA-4A25-BF99-5965EC9E2AB9")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."
    
myLabel = Label(root, text = city + " - Air Quality = "  + str(quality) + " , " + category, font=("Helvetica", 20), background="White")
myLabel.pack()

root.mainloop()
