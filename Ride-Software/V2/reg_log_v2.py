# Functions
users_data = {'Username': [], 'E-mail': [], 'Password': []}
valid_emails_types = [
    '@gmail',
    '@yahoo',
    '@hotmail'
    '@oulook'
]

def UserRegister(username, useremail, userpassword):
    users_data['Username'].append(username)
    if '@' and '.com' in useremail:
        users_data['E-mail'].append(useremail)
    users_data['Password'].append(userpassword)
    print(f'User regist successful!\nWelcome, {username}!')
    
def UserLogin(UserRegister):
    for nome in users_data['Username']:
        if nome in users_data['Username']:
            True
    for email in users_data['E-mail']:
        if email in users_data['E-mail']:
            True
    for senha in users_data['Password']:
        if senha in users_data['Password']:
            True
            
            print(f'Welcome, {UserRegister.username}!')