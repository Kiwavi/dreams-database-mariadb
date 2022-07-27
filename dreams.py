#!/usr/bin/python
import sys
import mariadb
from decouple import config
import locale
config.encoding = locale.getpreferredencoding(False)

dreams = {'1':'Positive Dream','2':'Nostalgic Dream','3':'Nightmare','4':'Awkward Dream','5':'Erotic Dream'}

rememberance = input('Can you remember yesterday\'s dream? Type Y for Yes and N for No: ').strip()

if rememberance == 'Y' or rememberance == 'y':
    the_category = ''
    category = input(' 1) Positive Dream \n 2) Nostalgic Dream \n 3) Nightmare \n 4) Awkward Dream \n 5) Erotic Dream \n What type of dream did you have?: ').strip()
    category = int(category)
    if category > 0 and category <= 5:
        the_category = dreams[str(category)]
    else:
        print('Please choose any option between 1 and 5')
        sys.exit()
    dream_description = input('Please describe your dream below: \n').strip()

    try:
        conn = mariadb.connect (
            user=config('user'),
            password=config('password'),
            host=config('host'),
            database=config('database')
        )
    
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    cur.execute("INSERT INTO dreams (Category,Description,Date) VALUES (?,?,CURDATE())",(the_category,dream_description,))
    conn.commit() #to save the instance 
    conn.close() #close the connection
    print('Thanks for your input, have a good day!')


elif rememberance == 'N' or rememberance == 'n':
    try:
        conn = mariadb.connect(
            user=config('user'),
            password=config('password'),
            host=config('host'),
            database=config('database')
        )
    
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    val = 'Can\'t Remember'
    cur.execute("INSERT INTO dreams (Category,Description,Date) VALUES (?,?,CURDATE())",(val,val,))
    conn.commit() #to save the instance 
    conn.close() #close the connection
    print('Thanks for your participation!')

else:
    print('Please insert the correct value')

# ensure there's a mariadb installation and there's a user named tecumseh and he's at localhost and has privileges to the database Personal
