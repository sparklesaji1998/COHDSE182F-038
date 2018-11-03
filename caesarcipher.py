plaintext=input("Input text:")
alphabet="abcdefghijklmnopqrstuvwxyz"
k=1            
cipher=''
choice=''
if choice =='1':
     for c in plaintext:
         if c in alphabet:
             cipher += alphabet [(alphabet.index(c)+key)%len(alphabet)]
             print("your encrypted message is:"+cipher)
elif choice =='2':
     for c in plaintext:
          if c in alphabet:
             cipher += alphabet [(alphabet.index(c)-key)%len(alphabet)]
             print("your encrypted message is:"+cipher)
else:
     print("you have entered an invalid input")
