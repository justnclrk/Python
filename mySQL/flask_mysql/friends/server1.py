import md5 # imports the md5 module to generate a hash
password = 'password'
salt = '123' #where the value 123 changes randomly
hashed_password = md5(password + salt)
print hashed_password #this will show you the hashed value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!