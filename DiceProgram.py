import sys
stop1 = 0
while stop1 != "q":
    import random
    print ("This is my first program")
    print ("This program gives the random dice ")
    raw_input("press Enter to start")
    number = random.choice([1,2,3,4,5,6])

    if number == 1:
        print ("[-----------]")
        print ("[           ]")
        print ("[     0     ]")
        print ("[           ]")
        print ("[-----------]")
        print ("Press q to stop")
        stop1 = raw_input()
    if number == 2:
        print ("[-----------]")
        print ("[           ]")
        print ("[   0   0   ]")
        print ("[           ]")
        print ("[-----------]")
        print ("Press q to stop")
        stop1 = raw_input()
    if number == 3:
        print ("[-----------]")
        print ("[     0     ]")
        print ("[     0     ]")
        print ("[     0     ]")
        print ("[-----------]")
        print ("Press q to stop")
        stop1 = raw_input()
    if number == 4:
        print ("[-----------]")
        print ("[     0     ]")
        print ("[   0   0   ]")
        print ("[     0     ]")
        print ("[-----------]")
        print ("Press q to stop")
        stop1 = raw_input()
    if number == 5:
        print ("[-----------]")
        print ("[     0     ]")
        print ("[  0  0  0  ]")
        print ("[     0     ]")
        print ("[-----------]")
        print ("Press q to stop")
        stop1 = raw_input()
    if number == 6:
        print ("[-----------]")
        print ("[   0  0    ]")
        print ("[   0  0    ]")
        print ("[   0  0    ]")
        print ("[-----------]")
        print ("Press q to stop")
        stop1 = raw_input()
