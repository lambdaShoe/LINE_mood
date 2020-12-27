from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

   #input
   # layer 1
    def is_going_to_mood(self, event):
        text = event.message.text
        return text.lower() == "mood"
	
    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_excited(self, event):
        text = event.message.text
        return text.lower() == "excited"

    def is_going_to_chill(self, event):
        text = event.message.text
        return text.lower() == "chill"
    
    def is_going_to_sad(self, event):
        text = event.message.text
        return text.lower() == "sad"
    #layer 2

    def is_going_to_little_excited(self, event):
        text = event.message.text
        return text.lower() == "little excited"

    def is_going_to_very_excited(self, event):
        text = event.message.text
        return text.lower() == "very excited"

    def is_going_to_wine(self, event):
        text = event.message.text
        return text.lower() == "wine"

    def is_going_to_travel(self, event):
        text = event.message.text
        return text.lower() == "travel"

    def is_going_to_little_sad(self, event):
        text = event.message.text
        return text.lower() == "little sad"

    def is_going_to_very_sad(self, event):
        text = event.message.text
        return text.lower() == "very sad"
    
    #layer 3

    def is_going_to_Pop(self, event):
        text = event.message.text
        return text.lower() == "Maroon 5"

    def is_going_to_HipHop(self, event):
        text = event.message.text
        return text.lower() == "Snoop Dog"
    
    def is_going_to_EDM(self, event):
        text = event.message.text
        return text.lower() == "Marshmallow"

    def is_going_to_Rock(self, event):
        text = event.message.text
        return text.lower() == "Coldplay"

    def is_going_to_Rap(self, event):
        text = event.message.text
        return text.lower() == "Eminem"

    def is_going_to_Metal(self, event):
        text = event.message.text
        return text.lower() == "Avenged Sevenfold"

    def is_going_to_Fusion(self, event):
        text = event.message.text
        return text.lower() == "Snarky Puppy"

    def is_going_to_Classic(self, event):
        text = event.message.text
        return text.lower() == "Beethoven"

    def is_going_to_Jazz(self, event):
        text = event.message.text
        return text.lower() == "Louis Armstrong"

    def is_going_to_Soul(self, event):
        text = event.message.text
        return text.lower() == "Daniel Caesar"



    #output
    #layer1
    def on_enter_mood(self, event):
	print("I'm entering mood")
	text = "Please choose your mood: [excited] or [chill] or [sad]"
		
        reply_token = event.reply_token
        send_text_message(reply_token, text)
        

    def on_enter_fsm(self, event):
	print("I'm entering fsm")
		
        reply_token = event.reply_token
        send_text_message(reply_token , "hello")


    def on_enter_excited(self, event):
	print("I'm entering excited")
	text = "Please choose your level of excitement: [little excited] or [very excited]"
		
        reply_token = event.reply_token
        send_text_message(reply_token, text)
        

    def on_enter_chill(self, event):
	print("I'm entering chill")
	text = "Please make a choice: [wine] or [travel]"
		 
        reply_token = event.reply_token
        send_text_message(reply_token, text)
        

    def on_enter_sad(self, event):
	print("I'm entering sad")
	text = "Please make a choice: [little sad] or [very sad]"
		 
        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    #layer2
    def on_enter_little_excited(self, event):
	print("I'm entering little_excited")
	text = "Please choose your favourite artist:[Maroon 5] or [Snoop Dog]"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
        

    def on_enter_very_excited(self, event):
	print("I'm entering very_excited")
	text = "Please choose your favourite artist: [Marshmallow] [Coldplay] [Eminem] [Avenged Sevenfold]"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_wine(self, event):
	print("I'm entering wine")
	text = "Please choose your favourite artist: [Snarky Puppy] [Beethoven] [Louis Armstrong] [Daniel Caesar]"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       
        

    def on_enter_travel(self, event):
	print("I'm entering travel")
	text = "I assume you like country songs a lot!Take me home~ Country Road~ To the place~ I BELONG~~"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_little_sad(self, event):
	print("I'm entering little_sad")
	text = "Cheer up! Listen to some happy songs.Life is Good."
     
        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_very_sad(self, event):
	print("I'm entering very_sad")
	text = "Cheer up! Listen to some happy songs.Life is Good."
        
        reply_token = event.reply_token
        send_text_message(reply_token, text)
        

    #layer3
    def on_enter_Pop(self, event):
	print("I'm entering Pop")
	text = "This is our recommendation for the genre of music for you to enjoy:Pop Music!"
         
        reply_token = event.reply_token
        send_text_message(reply_token, text)
      

    def on_enter_HipHop(self, event):
	print("I'm entering HipHop")
	text = "This is our recommendation for the genre of music for you to enjoy:Hip Hop Music!" 

        reply_token = event.reply_token
        send_text_message(reply_token, text)
        

    def on_enter_EDM(self, event):
	print("I'm entering EDM")
	text = "This is our recommendation for the genre of music for you to enjoy:EDM Music!" 

        reply_token = event.reply_token
        send_text_message(reply_token, text)
      

    def on_enter_Rock(self, event):
	print("I'm entering Rock")
	text = "This is our recommendation for the genre of music for you to enjoy:Rock Music!" 

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_Rap(self, event):
	print("I'm entering Rap")
	text = "This is our recommendation for the genre of music for you to enjoy:Rap Music!"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_Metal(self, event):
	print("I'm entering Metal")
	text = "This is our recommendation for the genre of music for you to enjoy:Metal Music!"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_Fusion(self, event):
	print("I'm entering Fusion")
	text = "This is our recommendation for the genre of music for you to enjoy:Fusion Music!"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_Classic(self, event):
	print("I'm entering Classic")
	text = "This is our recommendation for the genre of music for you to enjoy:Classical Music!" 

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

    def on_enter_Jazz(self, event):
	print("I'm entering Jazz")
	text = "This is our recommendation for the genre of music for you to enjoy:Jazz Music!" 

        reply_token = event.reply_token
        send_text_message(reply_token, text)
        

    def on_enter_Soul(self, event):
	print("I'm entering Soul")
	text = "This is our recommendation for the genre of music for you to enjoy:Neo-soul!"

        reply_token = event.reply_token
        send_text_message(reply_token, text)
       

