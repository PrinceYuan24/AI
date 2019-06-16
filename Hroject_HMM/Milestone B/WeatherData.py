import pandas as pd
import FunctionLib as fl

class WeatherData():
    def __init__(self, Datapath):
        INPUT = pd.read_excel (Datapath)
        self.OrginalInput = fl.Data2List(INPUT)
        self.temp = self.OrginalInput[:][0]          # Temperature
        self.hum = self.OrginalInput[:][1]           # Humidity
        self.press = self.OrginalInput[:][2]         # Pressure 
        self.observe = self.OrginalInput[:][0:3]     # Observable data
        self.realWeather = self.OrginalInput[:][3]   # Real weather
        self.time = range(len(self.OrginalInput))    # Time domain
