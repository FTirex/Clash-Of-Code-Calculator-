#Creating By FTirex 
#Ranking Point System Clash Of Code Tournament

""" 
Time Points 

0 => 5 min : + 15 

5 => 10 min : +10 

10 => 15 min : +5

Ranks points : 

1 : +50 

2 => 5 : +40

6 => 10 : +25

10+ : +15

Task Points  : 

0 => 50% : +15

50%+ : +25

"""
# Everytime you execute the Program it will be a New Round and all details will be registred in 2 files 
# Details.txt to check all players infos 
# Results.txt to check players points 

import os 

from time import sleep

import json

                    
def Check():         #======= Creating Folder + File .tct ==========    
    
    path = "C:\COC Calculator"                         #Directory Path 

    if os.path.isdir(path) == True:      #Check if Path is correct or No 

        print("Available Directory")

    else:

        try:

            os.mkdir(path)

            sleep(2)

        except OSError:

            print ("Creation of the directory %s failed" % path)

            sleep(2)

        else:

            print ("Successfully created the directory %s " % path)

            sleep(2)

    if os.path.isfile(path+'\Results.txt'):       #Check if file path Exist or No 

        print('Available File')                                       
  
    else:                                                                #Creating txt File into custom path 

        print("unavailable File We Should Create One")

        sleep(1)

        print("Creating ... ")

        sleep(2)

        f = open(path+'\Results.txt',"x")

        f1 = open(path+'\Details.txt',"x")

        print("Results.txt Is Available Now ")

        print("Details.txt Is Available Now ")

        print("Check Here",path," To See The folder")

Check()
        #========= Clash Of Code Calculation Function =========== 
def COC(): 

        #Fill Out Players Detials 

    print("Number of players : ")

    Players_Number = int(input())

    for i in range(Players_Number):

        print("Player",i+1,"Name :")

        Player_Name = input()

        print(Player_Name,'Rank ')

        Rank = int(input())

        print("""Attention Please if you have Time Like this 

                    5:01:03

                    5 min , 01 sec and 03 ms 
                    
                    Just Make Input like this 

                    Time : 5.01 ( Float Type)

                    No Need for ms 

                    Thank You 
        """)

        print("Time of",Player_Name)

        Time = float(input("Time : \n"))

        Time = round(Time)

        print(""" Attention Please Task Percentage is so important 

                    so Try to Give Then Int Number without %. 

                    Thank You  
        """)

        print("Task Percentage of",Player_Name)

        Task = int(input())

        if (Time >= 0) and (Time <= 5):

            ScoreTime = 15

        if (Time >= 5) and (Time <= 15):
            
            ScoreTime = 10

        if (Time >= 10) and (Time <= 15):

            ScoreTime = 5 

        if (Task >=0) and (Task<=50): 

            ScoreTask = 15

        if (Task >=50) and (Task<=100): 

            ScoreTask = 25
        
        if(Rank == 1):

            ScoreRank = 50

        if (Rank >= 2) and (Rank <= 5):

            ScoreRank = 40 

        if (Rank >= 6) and (Rank <= 10):

            ScoreRank = 25 

        if (Rank > 10) :

            ScoreRank = 15 

        ScoreFinal = ScoreTask + ScoreTime + ScoreRank

        FinalScore= {}
        Details ={}

        FinalScore.update({Player_Name:ScoreFinal})

        Details.update({Player_Name:ScoreFinal})

        Details.update({'Rank':Rank,'Time':Time,'Task percentage':Task})
        
        with open("C:\COC Calculator\Details.txt", 'a') as f:

            for key, value in Details.items():

                f.write('%s:%s\n' % (key, value))

            f.write("============= Next Player Details ===================\n")

        with open("C:\COC Calculator\Results.txt", 'a') as f:
            
            for key, value in FinalScore.items():

                f.write('%s:%s\n' % (key, value))

    with open("C:\COC Calculator\Results.txt", 'a') as f:

        f.write("============= Next Round ===================\n")

    
COC()