import numpy as np

HIDDENSTATE_CODE = {'Rainy': 0, 'Cloudy': 1, 'Sunny': 2}
CODE_HIDDENSTATE = {0: 'Rainy', 1: 'Cloudy', 2: 'Sunny'}

def Forward(PI, Ob, A, Test):
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
    PWeather_Forward = np.array(PI)
    A = np.array(A)
    index = 0
    for t in Test:
        em = np.array([Ob[t-1][0], Ob[t-1][1], Ob[t-1][2]])
        #print('PF',PWeather_Forward)
        #print('em', em)
        PWeather_Forward = PWeather_Forward * em
        #print('dot', PWeather_Forward)
        if (index == 0): 
            # Initialization Step
            index += 1
            continue
        else:
            # Recursion Step
            PWeather_Forward = np.dot(PWeather_Forward, A)
            #print('result', PWeather_Forward)
        index += 1

    return PWeather_Forward

def Viterbi(PI, Ob, A, Test):
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
    Predict_State_Code = []
    PWeather_Viterbi = np.array(PI)
    A = np.array(A)
    index = 0
    for t in Test:
        em = np.array([Ob[t-1][0], Ob[t-1][1], Ob[t-1][2]])
        # print('PF',PWeather_Viterbi)
        # print('em', em)
        PWeather_Viterbi = PWeather_Viterbi * em
        # print('dot', PWeather_Viterbi)
        if (index == 0): 
            # Initialization Step
            index += 1
            predict = np.argmax(PWeather_Viterbi)
            Predict_State_Code.append(predict)
            continue
        else:
            # Recursion Step
            PWeather_Viterbi = np.dot(PWeather_Viterbi, A)
            # print('result', PWeather_Viterbi)
            predict = np.argmax(PWeather_Viterbi)
            Predict_State_Code.append(predict)
        index += 1
        Predict_State = Code2State(Predict_State_Code)
    return PWeather_Viterbi, Predict_State_Code, Predict_State

def Code2State(Predict_State_Code):
    Predict_State = [CODE_HIDDENSTATE[code] for code in Predict_State_Code]
    return Predict_State