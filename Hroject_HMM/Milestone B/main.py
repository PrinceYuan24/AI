import WeatherData as wd
import matplotlib.pyplot as plt

DATAPATH = ''
HIDDENSTATE_CODE = {'Sunny': 0, 'Raining': 1, 'Snowing': 2}
CODE_HIDDENSTATE = {0: 'Sunny', 1: 'Raining', 2: 'Snowing'}

WeatherData1 = wd.WeatherData(DATAPATH)
state = [0, 1, 2]
PWeather_Forward = Forward(WeatherData1.observe, state)
PWeather_Viterbi = Viterbi(WeatherData1.observe, state)

# Plot Result
timeDomain = WeatherData1.time
plt.plot(timeDomain, PWeather_Forward, 'Predicted weather by Forward Algorithm')
plt.plot(timeDomain, PWeather_Viterbi, 'Predicted weather by Viterbi Algorithm')
plt.show()


def Forward(O, Q):
    # O: Observation Q: Hidden state
    '''
    function FORWARD(observations of len T, state-graph of len N) returns forward-prob
    create a probability matrix forward[N,T]
    for each state s from 1 to N do ; initialization step
        forward[s,1]←πs ∗ bs(o1)
    for each time step t from 2 to T do ; recursion step
        for each state s from 1 to N do
            forward[s,t]←sum(forward[s',t-1]*a(s',s)*b(s)(o_t))
    forwardprob←sum(forward[s,T])
    return forwardprob
    '''
    PWeather_Forward = []
    return PWeather_Forward

def Viterbi(O, Q):
    # O: Observation Q: Hidden state
    '''
    function VITERBI(observations of len T,state-graph of len N) returns best-path, path-prob
    create a path probability matrix viterbi[N,T]
    for each state s from 1 to N do ; initialization step
    viterbi[s,1]←πs ∗ bs(o1)
    backpointer[s,1]←0
    for each time step t from 2 to T do ; recursion step
        for each state s from 1 to N do
            viterbi[s,t]←max(viterbi[s',t-1]*a(s',s)*b(s)(o_t))
            backpointer[s,t]←argmax(viterbi[s',t-1]*a(s',s)*b(s)(o_t))
    bestpathprob←max(viterbi[s,T])
    bestpathpointer←argmax(viterbi[s,T])
    bestpath←the path starting at state bestpathpointer, that follows backpointer[] to states back in time
    return bestpath, bestpathprob

    '''   
    PWeather_Viterbi = []
    return PWeather_Viterbi