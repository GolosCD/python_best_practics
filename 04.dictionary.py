#ПРОГРАММА ДЛЯ ХРАНЕНИЯ ДНЕЙ РОЖДЕНИЯ
import os
#this dict save all pepople birthday
birthday = dict()

#this function add new element to dictionray birthday
def add_new_birthday():
        try:
            person_name = input('Input name: ')
            if person_name not in birthday:
                person_date = input('Input birthday date: ')
                #add new name in dict
                birthday[person_name]=person_date
                input('new person additional, press enter...')
                print('\n'*10)
                main()
            else:
                print('The data on this person is already in the database... try again!')
                main()  
        except:
            print('Error __add_new_birthday__,: ',ValueError)
            input('Press Enter for skip...')
            main()

# this function delete input person name to dictionary birthday   
def del_current_person():
    try:
        name_for_dalate = input('Input name for delete: ')
        if name_for_dalate in birthday:
            del birthday[name_for_dalate]
            input('birtday deleted, press enter...')
            print('\n'*10)
            main()
        else:
            print('Person not find...try again!')
            main()
    except:
        print('Error __del_current_person__,: ',ValueError)
        input('Press Enter for skip...')
        main()

#this function find and print you input person birthday
def search_birthday():
    try:
        person_name_for_serach = input('Input name: ')
        if person_name_for_serach in birthday:
            print('\n'*10)
            print('Name: ',person_name_for_serach)
            print('Birthday: ', birthday.get(person_name_for_serach))
            print()
            input('search finished, press enter...')
            print('\n'*10)
            main()
        else:
            print('Thsi name not find.. try again!')
            input('Press Enter for skip...')
            main()
    except:
        print('Error __search_birthday__,: ',ValueError)
        input('Press Enter for skip...')
        main()                   
                
def change_person_birthday():
    try:
        change_person_birthday = input('Input name for change date: ')
        if change_person_birthday in birthday:
            new_birthday = input('Input new date birthday: ')
            birthday[change_person_birthday] = new_birthday
            input('birtday changed, press enter...')
            print('\n'*10)
            main()
        else:
            print('Thsi name not find.. try again!')
            input('Press Enter for skip...')
            main()
    except:
        print('Error __change_person_birthday__,: ',ValueError)
        input('Press Enter for skip...')
        main()

menu_dict={'1':'Find birthday',
           '2':'Add new birthday',
           '3':'Change birthday',
           '4':'Delete birthday',
           '5':'Quit'
           }

menu_dict_action={'1':search_birthday,
                  '2':add_new_birthday,
                  '3':change_person_birthday,
                  '4':del_current_person,
                  '5':quit
                  }

def print_menu():
    for key in menu_dict:
        print(f'{key}:',menu_dict.get(key))

def choice_menu_item(choice_input:int):
    try:
        if choice_input in menu_dict_action.keys():          
            menu_dict_action[choice_input]()
        else:
            print('Error item menu, item menu not found...')
            input('Press Enter for skip...and nex input menu item')
            main()
    except:
            print('Error __choice_menu_item__,: ',ValueError)
            input('Press Enter for skip...')
            main()

def main():
    try:
        print_menu()

        input_choice=input('Input menu item:>>> ')

        choice_menu_item(input_choice)
    except:
        print('Error __choice_menu_item__,: ',ValueError)
        input('Press Enter for skip...')
        main()

if __name__=='__main__':
    main()        
            