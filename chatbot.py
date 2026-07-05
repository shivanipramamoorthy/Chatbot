import tkinter as tk #here we re importing the tkinter library as tk
def send(): #this is where we define our send button, and how the chatbot responds back. This occurs within lines 2-5
    send="you->"+input1.get()
    txt.insert(tk.END,"\n"+send)
    user=input1.get().lower()
    if(user=="hello"): #HERE, we start to train our bot by giving it specifics responses. One example is "hello"(occurs within lines 6-94) these lines have a common line of code, which is "txt.insert(tk.END,"\n"+"")" this is for when the chatbot receives a response, it will respons back accordingly. But to get the exact response, the user must word it such like "(level of activity(beginner,moderate,hard)) activities for (your age group(adults, kids,teenagers))"
        txt.insert(tk.END,"\n"+"bot->Hi there! How can I help you?")
    elif(user=="beginner activities for adults"):#we also use efif and if functions to determine the exact response the bot responds with after the user enters their response.(lines 6-94)
        txt.insert(tk.END, "\n"+'''bot->Here is a simple, universally accessible list of beginner-friendly hobbies and activities for adults that you can do practically anywhere:                
• Geocaching: Turn your daily walk into a real-life treasure hunt using free apps like  Geocaching . It’s a great way to explore local parks. 
• Journaling: Start a low-pressure writing habit. You can use free platforms like  Day One  to track daily gratitude or just clear your head. 
• Reading: Join virtual reading challenges or connect with local readers through the  Goodreads  community to find book recommendations. 
• Sketching: Grab a simple pencil and paper to practice drawing. You can find free step-by-step tutorials for beginners on  YouTube . 
• Bird Watching: Download bird identification apps like  Merlin Bird ID by Cornell Lab  to discover and track the species in your backyard or neighborhood. 
• Bodyweight Fitness: Build a simple, at-home routine (like squats and push-ups). Apps like Nike Training Club offer free beginner guided workouts. 
• Meditation: Learn the basics of mindfulness using guided sessions on free apps like  Insight Timer . 
''')
    elif(user=="beginner activities for teenagers"):
        txt.insert(tk.END, "\n"+'''bot->Here is a simple, go-to list of beginner-friendly, universally accessible activities teenagers can do anywhere: 

• Creative Arts: Try origami with basic paper  Origami Guide , or learn digital sketching using free mobile apps like IbisPaint X. 
• Fitness & Wellness: Follow along with free, beginner-friendly yoga or bodyweight workouts on  YouTube . 
• Language Learning: Build a new skill using free gamified apps like  Duolingo . 
• Creative Writing: Start a journal, draft a short story, or write lyrics for a song. 
• Organization & Hobbies: Customize a vision board using free platforms like  Canva  to map out goals and interests. [1, 2, 3, 4, 5]  
''')
    elif(user=="beginner activities for kids"):
        txt.insert(tk.END,"\n"+"bot->Here is a simple list of zero-prep, beginner-friendly activities you can do with kids anywhere:"
        "Dance Freeze: Play music and have the kids dance until you pause it, then tell them to freeze."
        "Pillow Fort: Throw blankets and pillows over the couch for an instant hideaway."
        "Floor is Lava: Lay down couch cushions or towels and challenge them to get across the room without touching the floor."
        "Sock Toss: Roll up a few pairs of clean socks and try to throw them into a laundry basket."
        "Simon Says: Take turns giving movement commands.")
    elif(user=="moderate activities for adults"):
        txt.insert(tk.END,"\n"+'''bot->Here is a simple, go-anywhere list of moderate activities perfect for adults:
        "Brisk Walking: The ultimate anywhere activity. A steady, moderate pace gets your heart pumping without intense strain.
        "Recreational Swimming: Gentle on the joints while offering a superb full-body workout.
        "Casual Cycling: Great for low-impact cardio; perfect for exploring your local neighborhood or parks.
        "Yoga and Pilates: Excellent for building core strength, flexibility, and balance using only your body weight.
        Bodyweight Calisthenics: Simple strength moves like modified push-ups, squats, and lunges can be done in any living room.
        Yard Work or Gardening: Raking leaves, mowing the lawn, or planting flowers easily counts as moderate physical activity''')
    elif(user=="moderate activities for teenagers"):
        txt.insert(tk.END,"\n"+'''bot->A simple list of moderate, universally accessible activities for teenagers: 
• Fitness/Outdoors: Go for a walk or bike ride in a local park, or play a casual game of basketball at a neighborhood court. 
• Creative: Learn to bake a new recipe, upcycle old clothes, or do an at-home spa day. 
• Social: Host an impromptu karaoke night using a Bluetooth speaker, or have a movie marathon. [1, 3, 4, 5, 6''')
    elif(user=="moderate activities for kids"):
        txt.insert(tk.END,"\n"+'''bot->These simple, moderate activities require minimal setup and no special equipment, making them perfect for kids of any age, anywhere. 

• Balloon Volleyball: Blow up a balloon and hit it back and forth to see how long you can keep it in the air. 
• Dance Party: Play upbeat music and dance, then pause it suddenly to freeze like statues. 
• Floor is Lava: Arrange pillows or cushions on the floor, allowing kids to jump from one "safe" spot to another without touching the floor. 
• Sock Toss: Roll clean socks into balls and practice tossing them into laundry baskets placed at various distances. 
• Animal Walks: Challenge kids to race or crawl across the room moving like different animals (e.g., bear crawls, frog jumps, or crab walks). 
• Mirror Game: Stand face-to-face and have kids mimic your stretches, silly faces, and movements, then switch places. [8, 9]  
''')
    elif(user=="hard activities for adults"):
        txt.insert(tk.END,"\n"+'''bot->Choosing to do "hard" activities is an excellent way for adults to build mental resilience and physical endurance. Here is a simple, universally accessible list of challenging activities that require no special equipment and can be done right in your local community. [1]  
🧠 Hard Mental Activities 

• The 30-Day Memory Challenge: Pick a complex poem, a challenging text, or a new foreign language phrase, and make it your goal to memorize or speak it daily. 
• Blindfold Tasking: Fold laundry or navigate a familiar room with your eyes closed to force your brain to map out your surroundings using only spatial awareness. 
• Math in Your Head: Ditch the calculator for a week. Try calculating restaurant tips, groceries, or time-tables completely in your head, double-checking with a calculator only afterward. 
• Progressive Muscle Relaxation: Lie completely still and tense individual muscle groups one by one from head to toe, holding for 15 seconds. It requires intense mental focus and extreme physical patience. 
• Creative Journaling: Pick a random, complex prompt (e.g., "describe what freedom tastes like") and write continuously for 15 minutes without editing yourself. [7, 8]  

🏃‍♂️ Hard Physical Activities 

• Walking Lunges: Pick a target distance in your living room or at a nearby park (e.g., 200 meters) and lunge the entire way. 
• Isometric Holds: Assume a plank or wall-sit position, and hold it until failure. Then, try to hold it for 15 seconds longer. 
• Adult Dance Classes: Learning completely new motor patterns—such as stepping combinations and routines—is notoriously difficult for adult brains and provides an intense full-body workout. 
• Outdoor Scavenger Hunts: Go for a walk and challenge yourself to find 10 specific, highly specific items (e.g., a heart-shaped leaf, something made of rusted iron, or a specific bird). 
• Bodyweight Circuits: Perform a combination of air squats, push-ups, and burpees with minimal rest between sets to challenge your cardiovascular endurance. [11, 12]  
''')
    elif(user=="hard activities for teenagers"):
        txt.insert(tk.END,"\n"+'''bot->Looking for a solid challenge to keep teens off their screens? Here is a simple list of tough, engaging activities that push their limits, build skills, and can be done practically anywhere: 

• The Marathon Read: Challenge them to read a dense, 500+ page classic or non-fiction book from cover to cover in under a week. 
• The Master Chef Test: Give them three random, difficult ingredients (e.g., eggplant, quinoa, and miso) and make them design and cook a cohesive, high-quality dinner from scratch. 
• The 1,000-Piece Puzzle: Dump out an intricate, 1,000-piece puzzle and task them with completing it without looking at the reference box. 
• The Garage Gym WOD: Create an intense, time-capped workout (like a "Murph" challenge) using only bodyweight exercises or household items. 
• The 30-Day Skill Sprint: Have them dedicate 30 minutes daily to mastering a genuinely difficult skill, such as solving a Rubik's Cube in under a minute, learning basic conversational coding, or juggling four balls. 
• The Living Room Escape Room: Design a complex series of logic puzzles, riddles, and physical challenges hidden around the house that they must solve within 60 minutes to "escape." 
''')
    elif(user=="hard activities for kids"):
        txt.insert(tk.END,"\n"+'''bot->Looking for ways to tire them out? Here is a simple, no-equipment list of physically demanding activities that kids can do anywhere to burn off that extra energy: 

• Bear Crawl Relays: Have them race across the room or yard on all fours, keeping their knees off the ground. 
• The Floor is Lava: Challenge them to navigate from one end of the room to the other using only specific furniture or cushions. 
• Living Room Obstacle Course: Combine jumping jacks, crab walks, and balancing a book on their head for a multi-step challenge. 
• Freeze Dance Party: Crank up some music and make them hold intense balancing poses when the music stops. 
• Wall Sit Challenge: See who can hold a "sit against the wall" position the longest. [1, 2, 3, 4, 5]
''')
chatbot=tk.Tk()#Here is our window name, defined as "chatbot"
chatbot.geometry("10000x10000")#this is the size of our window, which is shown as "10000x10000"
chatbot.config(bg="white")#this is just a config function to set our background color
label2=tk.Label(chatbot, text="",fg="white",bg="dark blue",width=400,height=400)#here is one label, which isnt really used within the entirety of this code. As we can see, we have defined its atributes within the code such as "bg=black" or something
label2.place(x=0,y=20)#the place function helps place our label here!
label1=tk.Label(text="WELCOME to the ACTIVITY CHATBOT! Enter your level of intensity of the activity and your age group(adult, kid, teenager)",fg="white",bg="black")#as you can see, this is our title, which will show at the top of our screen. In the next line, we pack it so it actually appears.
label1.pack()
txt=tk.Text(chatbot, width=400, height=400)#this is our text, which is where the chatbot responds on, and in the next line, we placed out text by using the place function, as mentioned several times.
txt.place(y=50,x=2)
input1=tk.Entry(chatbot,fg="white",bg="black")#here, we have our entry widget which is where you enter your input
input1.config(width=250)#we AGAIN use hte config functions to make the width of our input widget wider(so we can actually see it)
input1.place(x=100,y=2500)#then we use the place function to place it at the bottom of the screen, using these coordinates.
Button1=tk.Button(chatbot,text="ENTER!!!!!",fg="white",bg="black",command=send)#Then, we make our button, which we click to send our input to the chatbot. The earlier function that we defined as "send" is the command for this button
Button1.place(x=4000,y=2500)#Then we use the place function AGAIN to place the button next to our input widget
scroll_bar=tk.Scrollbar(width=50)#here we summon our scrollbar, with the width of 50
scroll_bar.pack(side="right", fill="y") #then here, we place our scroll bar in our wanted position
chatbot.mainloop()#Finally, we use the mainloop function to keep the window running, so that our window doesnt appear and then disappear in a blink of an eye!
#This is how we create the chatbot, in simple steps:
#1 we import our tkinter library
#2 we make out window, using the tk.Tk() function
#3 then, we add our widgets using the Label() Text() Button() ScrollBar() functions to create our labels, buttons, text, and  scrollbars required for the operation of this widget
#4 Finally, we define out function so we can put it in our button(in this case, mine's is called "send")