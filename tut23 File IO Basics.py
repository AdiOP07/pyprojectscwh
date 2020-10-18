# File Io Basics

'''

read mode==          "r" - Open File For Reading -default      / kisi v file ko padhne ke liye
write mode==         "w" - Open a File For Writing   / Kisi v file me Kuch Likh Sakte ho
Exclusive Creation= "x" - Create File If Not Exist    /Agar us Naam ki File Hai to Operation Fail ho jayega
Append==             "a" - Add More Content To a File  / Kisi v File Mein Kuch Add Karna
"t" - Text Mode -default / Agar main apne data ko string me deal karna ho... Notepad File...
"b" - Binary Mode  / Binary Hai Mereko nhi samajh aata sasura ye
"+" - Read and Write / padho v likho v ...LOL
'''

#Question Of The Day

def func1():
    """This Is Doc String"""
    return "okay"

print(func1.__doc__)