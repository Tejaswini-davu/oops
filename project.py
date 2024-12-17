##chatbook it has 3 option signin,signup,post
class chatbook:
    def __init__ (self):
        self.username = " "  # Removed trailing comma
        self.mail = ''      
    def menu(self):
        print("1 for signup")
        print("2 for signin")
        print("3 for post")
        n = int(input("enter yournumber"))
        if n ==1:
            self.signup()
        elif n==2:
            self.signin()
        elif n==3:
            self.post()
        else:
            print("please enter the proper number")
         
    def signup(self):
        username = input("enter your name")
        mail = input("enter your mail")
        self.username=username
        self.mail= mail
        print("signup successfull")
        self.signin()
        
    
    def signin(self):
        print("if you are not signined plase signin")
        signin_name= input("enter the name")
        signin_mail = input("enter the mail")
        if (signin_name==self.username)  & (signin_mail ==  self.mail):
            print("signin succesfull")
        else:
            print("please sugnin")

    def post(self):
        u = input("Enter your comment")
        print(f"  your post {u} had been posted on your accout")

   
book = chatbook()
book.menu()