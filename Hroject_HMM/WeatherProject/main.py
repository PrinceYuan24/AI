import WeatherData as wd
import numpy as np
import matplotlib.pyplot as plt
import HMM as hmm
import argparse

'''
No data Test probability
'''
# Transition Probility
# S: Sunny; R: Rainy; C: Cloudy
A        = {'R|R': 0.5, 'C|R': 0.3, 'S|R': 0.2,\
            'R|C': 0.5, 'C|C': 0.3, 'S|C': 0.2,\
            'R|S': 0.5, 'C|S': 0.3, 'S|S': 0.2}
P_TRANSE = [[0.5, 0.3, 0.2],
            [0.5, 0.3, 0.2],
            [0.5, 0.3, 0.2]]


# Emission Probability
P_HUM   = {'1|R': 0.1, '1|C': 0.2, '1|S': 0.6,\
            '2|R': 0.3, '2|C': 0.3, '2|S': 0.3,\
            '3|R': 0.6, '3|C': 0.5, '3|S': 0.1}
P_HUM_M = [[0.1, 0.2, 0.6],
            [0.3, 0.3, 0.3],
            [0.6, 0.5, 0.1]]

P_TEMP  = {'1|R': 0.3, '1|C': 0.8, '1|S': 0.2,\
            '2|R': 0.6, '2|C': 0.2, '2|S': 0.3,\
            '3|R': 0.1, '3|C': 0.0, '3|S': 0.5}
P_TEMP_M = [[0.3, 0.8, 0.2],
            [0.6, 0.2, 0.3],
            [0.1, 0.0, 0.5]]

P_PRESS = {'1|R': 0.1, '1|C': 0.2, '1|S': 0.6,\
            '2|R': 0.3, '2|C': 0.3, '2|S': 0.3,\
            '3|R': 0.6, '3|C': 0.5, '3|S': 0.1}
P_PRESS_M = [[0.1, 0.2, 0.6],
                [0.3, 0.3, 0.3],
                [0.6, 0.5, 0.1]]

# Initial Prpbability distribution
PI = [0.0, 1.0, 0.0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Customized or Statistical Data')
    parser.add_argument('--customized', action='store_true')
    args = parser.parse_args()
    DATAPATH = 'data.xlsx'
    DATA = wd.WeatherData(DATAPATH)
    if not args.customized:
        print('---------------Statistical Data---------------')
        PI = DATA.PI.copy()
        P_TEMP_M = DATA.P_TEMP_M.copy()
        P_HUM_M = DATA.P_HUM_M.copy()
        P_PRESS_M = DATA.P_PRESS_M.copy()
        P_TRANSE = DATA.P_TRANSE.copy()
    else:
        print('---------------Customized Data---------------')

    '''
    Temperature
    '''
    print('----------Temperature----------')
    print('---Real Weather---')
    print(DATA.realWeather)
    PWeather_Forward = hmm.Forward(PI, P_TEMP_M, P_TRANSE, DATA.level_temp)
    print('---HMM Forward---')
    print(PWeather_Forward)
    PWeather_Viterbi, Predict_State_Code, Predict_State = hmm.Viterbi(PI, P_TEMP_M, P_TRANSE, DATA.level_temp)
    print('---HMM Viterbi---')
    print(PWeather_Viterbi)
    print('---Predicted weather---')
    print(Predict_State)
    # Plot Result
    timeDomain = DATA.time

    fig = plt.figure()
    plt.title('Temperature')
    plt.plot(timeDomain, Predict_State_Code, label='Predicted weather by Viterbi Algorithm')
    plt.plot(timeDomain, DATA.Code_realweather, label='Real Weather')
    plt.xlabel('Day')
    plt.ylabel('0: Rainy 1: Cloudy 2: Sunny')
    plt.legend()

    '''
    Humunity
    '''
    print('----------Humunity----------')
    print('---Real Weather---')
    print(DATA.realWeather)
    PWeather_Forward = hmm.Forward(PI, P_HUM_M, P_TRANSE, DATA.level_hum)
    print('---HMM Forward---')
    print(PWeather_Forward)
    PWeather_Viterbi, Predict_State_Code, Predict_State = hmm.Viterbi(PI, P_HUM_M, P_TRANSE, DATA.level_hum)
    print('---HMM Viterbi---')
    print(PWeather_Viterbi)
    print('---Predicted weather---')
    print(Predict_State)
    # Plot Result
    timeDomain = DATA.time

    fig = plt.figure()
    plt.title('Humunity')
    plt.plot(timeDomain, Predict_State_Code, label='Predicted weather by Viterbi Algorithm')
    plt.plot(timeDomain, DATA.Code_realweather, label='Real Weather')
    plt.xlabel('Day')
    plt.ylabel('0: Rainy 1: Cloudy 2: Sunny')
    plt.legend()

    '''
    Pressure
    '''
    print('----------Pressure----------')
    print('---Real Weather---')
    print(DATA.realWeather)
    PWeather_Forward = hmm.Forward(PI, P_PRESS_M, P_TRANSE, DATA.level_press)
    print('---HMM Forward---')
    print(PWeather_Forward)
    PWeather_Viterbi, Predict_State_Code, Predict_State = hmm.Viterbi(PI, P_PRESS_M, P_TRANSE, DATA.level_press)
    print('---HMM Viterbi---')
    print(PWeather_Viterbi)
    print('---Predicted weather---')
    print(Predict_State)
    # Plot Result
    timeDomain = DATA.time

    fig = plt.figure()
    plt.title('Pressure')
    plt.plot(timeDomain, Predict_State_Code, label='Predicted weather by Viterbi Algorithm')
    plt.plot(timeDomain, DATA.Code_realweather, label='Real Weather')
    plt.xlabel('Day')
    plt.ylabel('0: Rainy 1: Cloudy 2: Sunny')
    plt.legend()

    '''
    Show result
    '''
    plt.show()
