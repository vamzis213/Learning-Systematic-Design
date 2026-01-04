print('Linux server')
memory = 10
user_check = ''
while memory <= 90 :
    memory += 3
    print(f'{memory}%')
    if memory >= 90 :
        print('"Action Required: Clearing Cache"')
        user_check = input('Clear cache? (yes/no): ').lower()
        if user_check == 'yes':
            memory = 0
            print(f'{memory}%')
            break
        elif user_check == 'no' :
            print('System crash!!!!!!')
                
        

