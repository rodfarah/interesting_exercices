print('Groceries List\n')

groceries_list = []
action_tuple = 'a', 'd', 'l', 'e'

# Let's ask the action and validade it:

while True:
    action = input('Choose an option\n[a]dd [d]elete [l]list [e]exit: ').lower()
    if action not in action_tuple:
        print('Invalid Entry!\n')
    elif action == action_tuple[0]:
        item_to_add = input('Type the product name: ')
        groceries_list.append(item_to_add)
        print('Item successfuly added to the groceries list.\n')
    elif action == action_tuple[1]:
        if len(groceries_list) == 0:
            print('The groceries list is empty! No need to delete items!\n')
        try:
            item_to_clear_string = input('Type product index to be deleted: ')
            item_to_clear_int = int(item_to_clear_string)
            groceries_list.pop(item_to_clear_int)
            print(f'Ok! Product {item_to_clear_int} successfully deleted!\n')
        except IndexError: 
            print('Invalid Index Number!\n')
        except ValueError:
            print('Please, enter a number!\n')
            
    elif action == action_tuple[2]:
        if len(groceries_list)== 0:
            print('The groceries list is empty!\n')
        try:
            print('Here goes the actual list:')
            for indx, product in enumerate(groceries_list):
                print(indx, product)
            print('')
        except IndexError:
            print('There is no suck index number in your groceries list!')
        except ValueError:
            print('Please, enter a number!')
            
    elif action == action_tuple[3]:
        print('See you later!')
        break

