#%%x =10
n = int(input("Enter the number:"))
print (n)
if (x > n):
    print('is greater than ')
else:
    print('x is smaller than n')


# %%


1>0

# %%
#y = str('AAA') 
#z = str('BBB')
bool('AAA'>'BBB')
bool('AAB'>'AAA')
bool('aaa'>'AAA')

# %% 
9>= 9
    #
# %%
6.2 < 7

# %%
1 == True

# %%
False < True
# %%
shop = {'price':{'item1':'Tomatoes','value1':5,
'item2':'Sugar','value2':1.8},'pack_size':{'Tomatoes':'cofee',
    'value1':500}}

# %%

Name = input('Name : ')
# %%
t = 0
def countdown (t):
    while t > 0:
        t-= 1
        time.sleep(2)       
countdown(3)

# %%
24<42<53.2

# %%

42==42<53.2
# %%
505>42<=53.2
# %%
def hypotenus (a, b):
    c= (a**2 + b**2)
    return c

# %%
d = hypotenus (3,4)

# %%
#%%
mini = int(input('Enter the minimum number:'))
maxi = int(input('Enter the maximum number:'))

for i in range(mini, maxi+1):
    prime = True
    for j in range(2,i-1):
        (i % j) == 0
        prime = False
    if prime == True:
        print(i)
# %%
