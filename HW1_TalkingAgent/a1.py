import string

# three_x_cubed_plus_7(2) -> 31
def three_x_cubed_plus_7(x):
    return 3*x**3+7

# triple_up([2, 5, 1.5, 100, 3, 8, 7, 1, 1, 0, -2])  ->  [[2, 5, 1.5], [100, 3, 8], [7, 1, 1], [0, -2]]
def triple_up(list):
    length=len(list)
    ans=[]
    sub_ans=[]
    for i in range(length):
        if (i%3==0 and i!=0):
            x=[]
            for xx in sub_ans:
                x.append(xx)
            ans.append(x)
            sub_ans.clear()
        sub_ans.append(list[i])
        if (i==length-1):
            x=[]
            for xx in sub_ans:
                x.append(xx)
            ans.append(x)
    return ans

# mystery_code("abc Iz th1s Secure? n0, no, 9!") -> "NOP vM GU1F fRPHER? A0, AB, 9!"

alphabet_upper = []
for c in string.ascii_uppercase:
    alphabet_upper.append(c)

alphabet_lower = []
for c in string.ascii_lowercase:
    alphabet_lower.append(c)

mystery_alphabet_upper=[]
for c in alphabet_upper[13:26]:
    mystery_alphabet_upper.append(c)
for c in alphabet_upper[0:13]:
    mystery_alphabet_upper.append(c)

mystery_alphabet_lower=[]
for c in alphabet_lower[13:26]:
    mystery_alphabet_lower.append(c)
for c in alphabet_lower[0:13]:
    mystery_alphabet_lower.append(c)


def mystery_code(string):
    new_string = ''
    for i in string:
        if i in alphabet_lower:
            index = alphabet_lower.index(i)
            char = mystery_alphabet_upper[index]
        elif i in alphabet_upper:
            index = alphabet_upper.index(i)
            char = mystery_alphabet_lower[index]
        else:
            char = i;
        new_string = new_string + char
    return new_string

'''
future_tense(['Yesterday', 'I', 'ate', 'pasta', 'and', 'today', 'I', 'am', 'having', 'soup']) ->
 ['Tomorrow', 'I', 'will', 'eat', 'pasta', 'and', 'tomorrow', 'I', 'will', 'be', 'having', 'soup']

  future_tense(['Life', 'is', 'good', 'now']) ->
 ['Life', 'will', 'be', 'good', 'tomorrow']
Use the following rules for forming the future tense: Recognize past and present-tense forms of the verbs to be, 
to go, to eat, to have, and to do. Optionally handle some other verbs. Recognize the words today, yesterday, and now, 
and change them to tomorrow.
'''
tobe=['is','am','are','was','were','being']
togo=['go','went','going']
toeat=['eat','ate','eating']
tohave=['have','had','having']
todo=['do','did','doing']
time=['today','yesterday','now','Today','Yesterday','Now']

def tobe_change(tobe,output,s):
    index=output.index(s)
    tense=tobe.index(s)
    if tense<5:
        output.remove(s)
        output.insert(index,'be')
        output.insert(index,'will')
    else:
        ouput.insert(index,'will')
    return output

def change(tolist,output,s):
    index=output.index(s)
    tense=tolist.index(s)
    if tense<2:
        output.remove(s)
        output.insert(index,tolist[0])
        output.insert(index,'will')
    return output

def time_change(time,output,s):
    index=output.index(s)
    cap_index=time.index(s)
    output.remove(s)
    if cap_index<3:
        output.insert(index,'tomorrow')
    else:
        output.insert(index,'Tomorrow')
    return output

def future_tense(string_list):
    output=[]
    for i in string_list:
        output.append(i)
    for s in string_list:
        if s in tobe:
            output=tobe_change(tobe,output,s)
        elif s in togo:
            output=change(togo,output,s)
        elif s in toeat:
            output=change(toeat,output,s)
        elif s in tohave:
            output=change(tohave,output,s)
        elif s in todo:
            output=change(todo,output,s)
        elif s in time:
            output=time_change(time,output,s)
    return output

