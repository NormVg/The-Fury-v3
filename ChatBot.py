import random
from speak import speak
from wikiInfo import infom
yes = ('yes' , 'ok' )

yes_reply = ("ok")

Hello = ('hello','hey','hii','hi',)

reply_Hello = ('Hello Sir',
            "Hey , What's Up ?",
            "Hey How Are You ?",
            "Hello Sir , Nice To Meet You Again .",
            "Of Course Sir , Hello .")

Bye = ('bye','exit','sleep','go')

reply_bye = ('Bye Sir.',
            "It's Okay .",
            "It Will Be Nice To Meet You .",
            "Bye.",
            "Thanks.",
            "Okay.")

How_Are_You = ('how are you','are you fine')

reply_how = ('I Am Fine.',
            "Excellent .",
            "Moj Ho rhi Hai .",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

nice = ('nice','good','thanks','well done')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.",'thankyou boss','its ok','its nice to hear')
wrong = ('are you stupid','you are wrong','are you mad or what','ye kya ker rehe ho','what the heck is this')

wrong_reply = ('i apologise sir','i am realy sorry sir','please give me another chance','sorry boss','i will improve',"its's bad of me")

love = ('i love you', 'love you','you are grate')

love_reply = ('me too', 'its good to hear from you', 'i am not that grate')

Functions = ['functions','abilities','what can you do','features']

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')

where = ('where are you','are you there','kaha ho','where are you gone')

info = ('who are you','what are you')

info_reply = ('i am a computerized artificial assistant program','i am fury',"i am vishnu gupta's assistant"
,'assistant program')

name = ('what is your name','name')

name_reply  = ('fury','my name is fury','fury is my name','you can call me fury by the way')

boss = ('who is vishnnu gupta','vishnu gupta')


boss_reply = ('vishnu gupta is my boss','vishnu gupta is a student of class 10','he is my boss')

can_do = ('what con you do','can you do')

can_do_reply = ('i can do some voice operated work you')

whoMadeYou = ('who made you','who programed you','made you','programed you')

whoMadeYou_reply = ('sir vishnu gupta','my boss, vishnu gupta','of corse vishnu gupta')

where_reply = ('on your server sir', "wating for your order",'wating for your command sir', 'always ready boss','always there for you boss')

sorry_reply = ("Sorry , That's Beyond My Abilities .",
               "i am not made for this",
                "i am realy sorry",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.")
#################################################################################################################################


def chatbot(chat):
    
    chat = str(chat)

    if chat in Hello:
        reply = random.choice(reply_Hello)
        print(reply)
        speak(reply)

    elif chat in yes:
        reply = random.choice(yes_reply)
        print(reply)
        speak(reply)

    elif chat in Bye:
        reply = random.choice(reply_bye)
        print(reply)
        speak(reply)

    elif chat in How_Are_You:
        reply = random.choice(reply_how)
        print(reply)
        speak(reply)

    elif chat in nice:
        reply = random.choice(reply_nice)
        print(reply)
        speak(reply)

    elif chat in wrong:
        reply = random.choice(wrong_reply)
        print(reply)
        speak(reply)

    elif chat in yes:
        reply = random.choice(yes_reply)
        print(reply)
        speak(reply)
     
    elif chat in love:
        reply = random.choice(love_reply)
        print(reply)
        speak(reply)

    elif chat in Functions:
        reply = random.choice(reply_Functions)
        print(reply)
        speak(reply)

    elif chat in where:
        reply = random.choice(where_reply)
        print(reply)
        speak(reply)
    
    elif chat in info:
        reply = random.choice(info_reply)
        speak(reply)

    elif chat in name:
        reply = random.choice(name_reply)
        speak(reply)        

    elif chat in boss:
        reply = random.choice(boss_reply)
        speak(reply)     

    elif chat in can_do:
        reply = random.choice(can_do_reply)
        speak(reply)     

    elif chat in whoMadeYou:
        reply = random.choice(whoMadeYou_reply)
        speak(reply)     

    elif '' == chat:
        pass

    else:
        try:
            para,title = infom(chat)
            speak("title is " + title)
            speak(para)
        except:
            reply = random.choice(sorry_reply)
            speak(reply) 




#####################################################################################################################################
