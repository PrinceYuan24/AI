#!/usr/bin/env python
# coding: utf-8

# In[6]:


from re import *   # Loads the regular expression module.
import random


# In[7]:


'''
A message assistant in constomer service,
created by Ziyuan Wang, A graduate student in UW.
This version of the program runs under Python 3.x.

Ziyuan Wang
'''
def introduce():
    intro="My name is Yuan, a service assistant.\n\
I was programmed by Ziyuan Wang (UWNetID: wangzi). \n\
If you don't like the way I deal, contact him at wangzi@uw.edu\n\
What kind of item you buy from our online market?\n\
Smartphone, Laptop or Headphone."
    return intro

def agentName():
    return "Yuan"
'''
RANDOM CHOICE
'''
def random_finalresponse():
    index=random.randint(0,2)
    response=["Thank you for choosing us.",
             "I am very happy to help you solve the problem.",
             "Ok, all set here."]
    return response[index]

'''
CIRCLE
'''
circle_index=0
def item_response_circle():
    circle=["Is there any other thing I can help on your ",
           "Do you have any problem about your ",
           "What else can I help you on your "]
    global circle_index
    circle_index += 1
    return circle[circle_index % 3]

circle_index2=0
def none_reponse_circle():
    circle=["Please say something.",
           "Are you there, sir.",
           "Do you have any questions?"]
    global circle_index2
    circle_index2 +=1
    return circle[circle_index2 % 3]
        

def item_response(item):
    change=" Or change another item."
    if item==0:
        res=item_response_circle()+"smartphone?" + change
        #print(res)
        return res
    elif item==1:
        res=item_response_circle()+"laptop?" + change
        #print(res)
        return res
    elif item==2:
        res=item_response_circle()+"headphone?" + change
        #print(res)
        return res

item=3
def Shrink():
    'Shrink is the top-level function, containing the main loop.'
    print(introduce())
    global item
    while True:
        the_input = input('TYPE HERE:>> ')
        if match('bye',the_input):
            print('Goodbye!')
            return
        print (respond(the_input))

'''
MEMORY
Using varible item to memory the first topic.
'''
def respond(the_input):
    global item
    if match('Smartphone', the_input):
        item=0
        #print("What is the problem about your Smartphone?")
        return ("What is the problem about your Smartphone?")
        #continue
    elif match('Laptop',the_input):
        item=1
        #print("What is the problem about your Laptop?")
        return ("What is the problem about your Laptop?")
        #continue
    elif match('Headphone',the_input):
        item=2
        #print("What is the problem about your Headphone?")
        return ("What is the problem about your Headphone?")
        #continue
    elif match('No',the_input):
        #print(random_finalresponse())
        #print("Please say bye to end the conversation.")
        return random_finalresponse() + "\n" +("Please say bye to end the conversation.")
        #continue
    elif match('Yes',the_input):
        #print("What's your other problem")
        return ("What's your other problem")
        #continue
    elif match('Change another item.', the_input):
        #print("Which kind of item you have problem on,")
        #print('Smartphone, Laptop, or Headphone?')
        #continue
        return ("Which kind of item you have problem on,")+"\n"+('Smartphone, Laptop, or Headphone?')
    wordlist = split(' ',remove_punctuation(the_input))
    # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()
    if (item==0):
        return smartphone_response(the_input, wordlist, mapped_wordlist,item)
    elif (item==1):
        return laptop_response(the_input, wordlist, mapped_wordlist,item)
    elif (item==2):
        return headphone_response(the_input, wordlist, mapped_wordlist,item)
    else:
        return("Please enter the right device name.")
        #print("Please enter the right device name.")
                
def smartphone_response(the_input, wordlist, mapped_wordlist,item):
    if wordlist[0]=='':
        #print("Please say something.")
        return none_reponse_circle()
    elif 'Iphone' in wordlist:
        #print("You can call Apple service for more information.")
        #item_response(item)
        ans = ("You can call Apple service for more information.") + "\n" + item_response(item)
        return ans
    elif 'Samsung' in wordlist:
        #print("I will transfer the call to the Samsung service,")
        #print("they will solve your problem")
        #item_response(item)
        ans = ("I will transfer the call to the Samsung service,")\
        +"\n"+("they will solve your problem") + "\n" + item_response(item)
        return ans
    elif 'screen' in wordlist:
        #print("We can change a new screen for you,")
        #print("and recommand you have a screen protector next time.")
        #item_response(item)
        ans = ("We can change a new screen for you,")\
        +"\n"+("and recommand you have a screen protector next time.")+"\n"\
        +item_response(item)
        return ans
    elif 'broken' in wordlist:
        #print("You can send it back and we will fix it.")
        #item_response(item)
        ans = ("You can send it back and we will fix it.") +"\n" + item_response(item)
        return ans
    else:
        print("Sorry, I cannot recognize this sentence.")
        print("Please change another way to express or contact our service agent.")
        ans = ("Sorry, I cannot recognize this sentence.") + "\n"\
        +("Please change another way to express or contact our service agent.")
        return ans
    
def laptop_response(the_input, wordlist, mapped_wordlist,item):
    if wordlist[0]=='':
        #print("Please say something.")
        return none_reponse_circle()
    elif 'Lenovo' in wordlist:
        #print("You can call Lenovo service to get some help")
        #item_response(item)
        ans=("You can call Lenovo service to get some help")+"\n"+item_response(item)
        return ans
    elif 'Dell' in wordlist:
        #print("I will transfer the call to the Dell service,")
        #print("they will solve your problem")
        #item_response(item)
        ans=("I will transfer the call to the Dell service,")+"\n"+("they will solve your problem")\
        +"\n"+item_response(item)
        return ans
    elif 'return' in wordlist:
        #print("I will create a new return requist, it will take serveral days to process")
        #item_response(item)
        ans = ("I will create a new return requist, it will take serveral days to process")+"\n"\
        +item_response(item)
        return ans
    elif 'system' in wordlist:
        #print("Win 10 is include in the price,")
        #print("I will send you a guidance to install it.")
        #item_response(item)
        ans = ("Win 10 is include in the price,") +"\n"+ ("I will send you a guidance to install it.")\
        +"\n"+item_response(item)
        return ans
    elif 'broken' in wordlist:
        #print("We will send a technical sevice agent to help you")
        #item_response(item)
        ans = ("We will send a technical sevice agent to help you")+"\n"+item_response(item)
        return ans
    else:
        #print("Sorry, I cannot recognize this sentence.")
        #print("Please change another way to express or contact our service agent.")
        ans = ("Sorry, I cannot recognize this sentence.")\
        + "\n" +("Please change another way to express or contact our service agent.")
        return ans

def headphone_response(the_input, wordlist, mapped_wordlist,item):
    if wordlist[0]=='':
        #print("Please say something")
        return none_reponse_circle()
    elif 'sound' in wordlist:
        #print("Please double check if the headphone connect to your device.")
        return ("Please double check if the headphone connect to your device.")
    elif 'still' in wordlist:
        #print("I can choose to change a new one or refund.")
        return ("I can choose to change a new one or refund.")
    elif 'change' in wordlist:
        #print("I will help you create a replacement process")
        #item_response(item)
        ans = ("I will help you create a replacement process") +"\n"+item_response(item)
        return ans
    elif 'refund' in wordlist:
        #print("I will help you create a refund process")
        #item_response(item)
        ans = ("I will help you create a refund process") + "\n"+item_response(item)
        return ans
    else:
        #print("Sorry, I cannot recognize this sentence.")
        #print("Please change another way to express or contact our service agent.")    
        ans = ("Sorry, I cannot recognize this sentence.")\
        +"\n"+("Please change another way to express or contact our service agent.") 
        return ans

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:") 
def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}


# In[ ]:


Shrink()


# In[ ]:




