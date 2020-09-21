'''
About Function in Python:
Function 2 type ke hote hain:
    1. pre-defined function ()
    2. user-defined function ()

Pre-defined function: 
1. Ye function programming lanaguage me pahle se define hote hain.
2. In work aur behaviour pahle se set hota hai.
3. Jaise ki example ke liye: print() function.
    a. print function python me output show karne ke liye use hota hai.
    b. Is funciton me number of aruments ka use kiya jata hai.
    c. Jaise ki print me hum direct math solve kar sakte hain.
    d. Koi dusra pre-define fucntion bhi use kar sakte hain. Jaise ki datatype check karne ke liye type() function.
4. Har pre-define fucntion ka work behaviour bilkul user-define function jaisa hi hota hai. Bas in funciton ko pahle se hi define kar diya gaya hai.
5. Jin funciton ya work behavious ko pahle se define nahi kiya gaya hai. Un ke liye hi hum user-define fucniton create karte hain.

User-defined function:
Note: funciton create karne ke liye 'def' keyword ka use karte hain.
1. User-define funciton ka name user define karta hai.
2. Funciton name hamesa relevent name hona cahiye. Taki name se function ka work behaviour pata chale.
3. Function ke sub types bhi hain:
    a. Function with arguments & with return value
    b. Function without arguments & without return value
    c. Function with arguments & without return value
    d. Function without arguments & with return value
4. Funciton ka work kisi bhi specific problem ko solve karne ke liye kiya jata hai.
5. Ek funciton ke andar aap multiple condtion, loops, function ya class tak call kar sakte hain.
Function ka syntax:
def your_function_name():
    funciton body

Funciton name ke limitations:
1. Fucntion name ko bhi create karte time varibale ke rules ko dhyan rakho.
2. Jaise new variable number se ya fir space se nahi start kar sakte ho. Same to same yaha par bhi wahi sare varaible ruls follow hote hain.
Note: Yaad rahe complete programming lanaguage me hame 2 chije bar bar milti hain.
1. Keywords: Jaise ke del, def, class etc...
2. Function: Jaise ki print(), if(), for() etc....

Function me argument aur return ka matlab:
1. Argument asal me ek simple varaibel jaisa hi hai. Jab bhi hum fucntion me argument ki baat karte hain. To iska matlab hota hai ki hum kuch varible ya values fucntion me recive kar rahae hain.
2. Because function me hum koi bhi ek specific work karte hain aur uska result show karate hain ya fir result ko return karte hain.
3. Jaise hamesa yaad rakho ki arguments ko funciton me recive hi kiya jayega. Waise hi jab bhi function koi work complete kar dega then yata result fucniton me hi show karado. Ya fir result ko return bhi karaya ja sakta hai.
4 Jab bhi bat result ko return karane ki ho, iska matlab hoga ki hum wo resutl funciton ke bahar recive karenge. Then usko kisi varibel me store kar sakte hain.

Static aur dynamic values ka matlab:
1. Static values means ye fix values hain jo hum ek bar define kar diye wahi rahega.
2. Dynamic values means jab hum user input ke through valeus recive karte hain use time user kuch bhi values de sakta hain.
'''

# Function without arguments & without return value

# function definition | Yaha par hum fucntion ko define kar rahe hain. Yad rahe ye fucntion jab tak call nahi kiya jayega tub tak useme me nahi aayega
def myFirstFunction():
    print('\nHello fucntion how are you?')
    # print 1 to 10 number
    mysum = 0
    for r in range(1, 11):
        mysum += r
        print(r ,' : ', mysum)
updates
# fucntion call
myFirstFunction()

# Function with arguments & without return value

# fucntion define only
def fucntionWithArgument(num1, num2):
    addition = num1 + num2
    print('Addition of num1 and num2: ', addition)

# function call
fucntionWithArgument(10, 20)

# Function without arguments & with return value

# funciton define here
def functionWithRetrunValue():
    addition = 50 + 100
    return addition
    # print('Addition of num1 and num2: ', addition)

# call fucntion and recive the result value
myresutl = functionWithRetrunValue()
print('Myreustl answer is : ', myresutl)

print('Again my reustl: ', functionWithRetrunValue())


# Function with arguments & with return value

# multiplication fucntion which recives 2 arguments
# def functionWithArguentAndWithReturnValue()
def function_with_arguent_and_with_return_value(n1, n2):
    multiplication = n1 * n2
    return multiplication

# call fucntion
number1 = int(input('Enter 1st number: '))
number2 = int(input('Enter 2nd number: '))

result = function_with_arguent_and_with_return_value(number1, number2)

print('Result: ', result)
    

'''
Questions:
Easy Questions:
1. sum, subtract, multiplication, division ke funciton banane hain. Ye funtion indivial files me banane hain. Aur in file me ye 4 function behaviour ke through yeahi same functions bane hain.
    
    a. Function without arguments & without return value
    b. Function with arguments & without return value
    c. Function without arguments & with return value
    d. Function with arguments & with return value


1. Ek funciton create karna hai jisme ki apne firneds ki list dict ke form me bana hai aur usko fucntion ko pass karna hai. Then fucntion me usko multi line string ka use karke apne sabhi friends ak detail show karan hai.
2. User se multiple numbers get karne hain. Isske liye list aur appned ka use karna hai.
Then ye values alag-alag fucntion banae hai aur un sab me recive karn hai. Means sum, subtract, multiplication etc... ke funciton banae hai aur unme recive kar ke result show karana hai.
3. Same second number ke qustion ka use karna hai aur result ko fucntion ke andar na show karke usko return karna hai. Aur jo kuch result aaya usko chek karna hai agar result:
    a. agar result < 100 hai then:  isme 100 add karke result show karna hai.
    b. agar result > 100 and < 200 hai to to 200 add karke result show karn hai.
    c. agar result > 200 hai then 500 add karke result show karna hai.
Exta Questions:
1. What is cookies? How usefull or dangers it is?
2. What is session?
'''