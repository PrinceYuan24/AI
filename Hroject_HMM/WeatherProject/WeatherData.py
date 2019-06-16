import pandas as pd
import FunctionLib as fl
import numpy as np

# S: Sunny; R: Rainy; C: Cloudy

HIDDENSTATE_CODE = {'Rainy': 0, 'Cloudy': 1, 'Sunny': 2}
CODE_HIDDENSTATE = {0: 'Rainy', 1: 'Cloudy', 2: 'Sunny'}

class WeatherData():
    def __init__(self, Datapath):
        # Threshold
        self.TSH_TEMP = [50.0, 68.0]
        self.TSH_HUM = [39.0, 66.0]
        self.TSH_PRESS = [29.3, 29.9]

        INPUT = pd.read_excel (Datapath)
        self.OrginalInput = fl.Data2List(INPUT)
        self.dateTime = fl.column(self.OrginalInput, 0)[1:]      # Date Time

        self.temp = fl.column(self.OrginalInput, 1)[1:]          # Temperature
        self.level_temp = self.data2level(self.TSH_TEMP, self.temp)

        self.hum = fl.column(self.OrginalInput, 2)[1:]           # Humidity
        self.level_hum = self.data2level(self.TSH_HUM, self.hum)

        self.press = fl.column(self.OrginalInput, 3)[1:]         # Pressure
        self.level_press = self.data2level(self.TSH_PRESS, self.press)

        self.realWeather = fl.column(self.OrginalInput, 4)[1:]   # Real weather
        self.Code_realweather = [HIDDENSTATE_CODE[state] for state in self.realWeather] # using 0,1,2 to present the weather

        self.time = range(len(self.OrginalInput)-1)                # Time domain

        # Emission Probability
        self.P_TEMP_M = self.P_Emission(self.TSH_TEMP, self.temp, self.realWeather)
        self.P_HUM_M = self.P_Emission(self.TSH_HUM, self.hum, self.realWeather)
        self.P_PRESS_M = self.P_Emission(self.TSH_PRESS, self.press, self.realWeather)

        # Transition Probility
        self.P_TRANSE, self.PI = self.P_Transition(self.realWeather)
        # self.PI = [0.0, 0.0, 0.0]
        # InitiaState_code = HIDDENSTATE_CODE[self.realWeather[0]]
        # self.PI[InitiaState_code] = 1.0
        # print(self.PI)

    def P_Emission(self, Threshold, ob_data, realWeather):
        '''
        Input: 
            Threshold:   Threshold that define the level 1,2,3
            ob_date:     The processing data
            realweather: The realweather data
        Output:
            [['1|R', '1|C', '1|S'],
             ['2|R', '2|C', '2|S'],
             ['3|R', '3|C', '3|S']]
        '''
        R_num = C_num = S_num = 0
        length = len(ob_data)
        P =  [[0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0],
              [0.0, 0.0, 0.0]]
        for i in range(length):
            if realWeather[i] == 'Rainy':
                R_num += 1
                if ob_data[i] < Threshold[0]:
                    P[0][0] += 1
                elif ob_data[i] > Threshold[1]:
                    P[2][0] += 1
                else:
                    P[1][0] += 1
            elif realWeather[i] == 'Cloudy':
                C_num += 1
                if ob_data[i] < Threshold[0]:
                    P[0][1] += 1
                elif ob_data[i] > Threshold[1]:
                    P[2][1] += 1
                else:
                    P[1][1] += 1
            elif realWeather[i] == 'Sunny':
                S_num += 1
                if ob_data[i] < Threshold[0]:
                    P[0][2] += 1
                elif ob_data[i] > Threshold[1]:
                    P[2][2] += 1
                else:
                    P[1][2] += 1

        P[:] = [[x[0] / R_num, x[1] / C_num, x[2] / S_num] for x in P]
        return P

    def P_Transition(self, realweather):
        '''
        Input:
            realweather: The realweather data
        Outputt:
            P_TRANSE = [['R|R', 'C|R', 'S|R'],
                        ['R|C', 'C|C', 'S|C'],
                        ['R|S', 'C|S', 'S|S']]
        '''
        R_num = C_num = S_num = 0
        P_TRANSE = [[0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0]]
        length = len(realweather)
        for i in range(length - 1):
            if realweather[i] == 'Rainy':
                R_num +=1
                if realweather[i+1] == 'Rainy':
                    P_TRANSE[0][0] += 1
                elif realweather[i+1] == 'Cloudy':
                    P_TRANSE[0][1] += 1
                elif realweather[i+1] == 'Sunny':
                    P_TRANSE[0][2] += 1       
            elif realweather[i] == 'Cloudy':
                C_num +=1
                if realweather[i+1] == 'Rainy':
                    P_TRANSE[1][0] += 1
                elif realweather[i+1] == 'Cloudy':
                    P_TRANSE[1][1] += 1
                elif realweather[i+1] == 'Sunny':
                    P_TRANSE[1][2] += 1
            elif realweather[i] == 'Sunny':
                S_num +=1
                if realweather[i+1] == 'Rainy':
                    P_TRANSE[2][0] += 1
                elif realweather[i+1] == 'Cloudy':
                    P_TRANSE[2][1] += 1
                elif realweather[i+1] == 'Sunny':
                    P_TRANSE[2][2] += 1

        num_list = [R_num, C_num, S_num]
        P_TRANSE = [[P_TRANSE[i][0] / num_list[i], P_TRANSE[i][1] / num_list[i],\
                    P_TRANSE[i][2] / num_list[i] ] for i in range(len(num_list))]
        s = sum(num_list)
        PI = [R_num/s, C_num/s, S_num/s]

        return P_TRANSE, PI

    def data2level(self, Threshold, data):
        length = len(data)
        data_copy = data.copy()
        for i in range(length):
            if data_copy[i] < Threshold[0]:
                data_copy[i] = 1
            elif data_copy[i] > Threshold[1]:
                data_copy[i] = 3
            else:
                data_copy[i] = 2
        return data_copy            


