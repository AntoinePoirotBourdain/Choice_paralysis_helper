# -*- coding: utf-8 -*-
"""
Created on Tue May 17 08:57:12 2022
5
@author: ANTOINE
"""

import pandas as pd
import random as rd
import sys





############################# bases functions #################################

def read_database():
    db = pd.read_csv('database.csv',index_col=0)
    return db
    

def activity(db):
    
    activity_list= list(db.index)
    weight_list = list(1/db['Counter'])
    
    choice = rd.choices(activity_list,weight_list)[0]
    
    print('The chosen activity is :',choice)
    
    
    return choice

def add_counter(db,choice):
    db['Counter'].loc[choice]+= 1 
    return db

def update_database(db):
    db.to_csv('database.csv')


############################# choices functions ###############################


def chose_activity():
    print('\n\n############# Choice of an activity ##########################')
    db = read_database()
#    choice = activity(db)
    choice = 'Study history'
    db = add_counter(db,choice)
    update_database(db)

    input('')
    main()
    
def activity_list():
    print('\n\n############# List of the activities #########################')
    db = read_database()
    for activity in list(db.index):
        print(activity, '( count : ',db['Counter'].loc[activity],')')
    input('')
    main()
        
def add_activity():
    print('\n\n################ Add an activity##############################')
    db = read_database()
    activity =input('name of the activity to add : ')
    print ('\nTou want to add the activity :',activity,'? (y/n)')
    yesno = input('')
    if yesno == 'y':
        db.loc[activity] = [0]
        
        print('activity', activity, 'added to the database')
        update_database(db)
        input()
        main()
    else:
        main()

# def remove_activity():   
#     print('\n\n################ Emove an activity ############################')
#     db = pd.read_csv('database.csv')
#     i = 0
    
#     for index in list(db.index):
#         activity = db.loc[index]['Activity']
#         print(index, ' : ',activity)
#     input()
    
#     print('Are you want to remove the activity')
    
#     yesno = input()
    
#     if yesno == 'y':
#         db.loc[activity] = [0]
        
#         print('activity', activity, 'added to the database')
#         update_database(db)
#         input()
#         main()
#     else:
#         main()    
#     print()

# remove_activity()

def reset_counters():
    print('\n\n################ Reset Counters ##############################')
    db = read_database()
    for activity in db.index:
        db['Counter'].loc[activity] =0
    print(db)
    print ('\nAre you sure you want to reset the counters ?(y/n)')
    yesno = input('')
    if yesno == 'y':
        update_database(db)
        input()
        main()
    else:
        main()  
def exit_program():
        print('\n\n################ End of program #########################')
        sys.exit()

################################## program ####################################


def main():
    
    print('\n\n############# Main Menu ######################################')
    print('Select a functionaly:'
          '\n1 : Chose an activity '
          '\n2 : List of activity '
          '\n3 : Add an activity '
          '\n4 : Reset counters '
          '\n5 : Exit Program')
    
    selection = input()
    if selection == '1':
        chose_activity()
    elif selection =='2':
        activity_list()
    elif selection == '3':
        add_activity()
    elif selection == '4':
        reset_counters()
    elif selection =='5':
        exit_program()
        
    else:
        print('not_in_list')
        main()
        
main()