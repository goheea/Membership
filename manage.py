class Membership:
    def __init__(self,id,password):
        self.id=id
        self.password=password
    def ID(self):
        return self.id
    def PASSWORD(self):
        return self.password

class Login:
    def __init__(self,id_,password_):
        self.id=id_
        self.password=password_

    def l_id(self):
        return self.id
    def l_password(self):
        return self.password

class Register:
        def __init__(self):
            self.name_list=[]
            self.phone_list=[]

        def n_add(self):
            name=input("이름을 입력하시오 : ")
            self.name_list.append(name)

        def p_add(self):
            phone=input("전화번호를 입력하시오 : ")
            self.phone_list.append(phone)

        def get_n(self):
            return self.name_list

        def get_p(self):
            return self.phone_list

        def print(self):
            print("회원 리스트")
            print("-----------------------------")
            for i in range((len(self.name_list))) :
                print("이름 : ",self.name_list[i])
                print("전화번호 : ",self.phone_list[i])
                print("-----------------------------")

class Choice:
    def __init__(self):
        self.cp=[]
        self.np=[]
        self.cpp=[]
    def setCp(self,n,m):
        self.cp.append(n)
        self.cpp.append(m)
    def setNp(self,n):
        self.np.append(n)
    def printCp(self):
        print(self.cp)
        print(self.cpp)
    def printNp(self):
        print(self.np)
        
class Sending:
    def __init__(self):
        self.Receiver = []
        self.Tel = []
        self.c = ""
    def SendCt(self):
        self.c = input("\n보낼 내용 작성: ")
    def Notice(self):
        print(f'{self.Receiver} 에게 해당 내용을 전송했습니다. \n{self.c}')
        #문자 발송 확인 안내 출력


print("회원가입을 진행합니다.")
ID=input("아이디를 입력하시오: ")
PASSWORD=input("비밀번호를 입력하시오: ")
a=Membership(ID,PASSWORD)

print("\n로그인을 진행합니다.")
while True:
    id=input("아이디를 입력하시오: ")
    password=input("비밀번호를 입력하시오: ")
    b=Login(id,password)
    if((b.l_id()==a.ID())&(b.l_password()==a.PASSWORD())):
        print("로그인에 성공하였습니다.")
        break;
    else:
        print("로그인에 실패하였습니다.")

name_list=[]
phone_list=[]
c=Register()
while True:
    print("=============================")
    print("1. 회원 등록")
    print("2. 회원 리스트 확인")
    print("3. 종료")
    print("=============================")
    menu=int(input("메뉴를 선택하시오: "))
    print("=============================")
    if menu==1:
        c.n_add()
        c.p_add()
    elif menu==2:
        c.print()
    elif menu==3:
        break;
name_list=c.get_n()
phone_list=c.get_p()

b=name_list
c=phone_list
m=Choice()
for i in range(len(b)): 
    menu=input(b[i]+" 선택(1:대상자 채택, 2:채택하지 않음, 3:종료): ")
    
    if(menu=="1"):
        m.setCp(b[i],c[i])
    elif(menu=="2"):
        m.setNp(b[i])
    elif(menu=="3"):
        print("대상자 선택을 종료합니다.")
    else:
        print("다시 선택해 주세요")
print("\n선택된 회원 대상자 입니다.")
m.printCp()

s = Sending()

ReList = []
PNList = []
CtList = []

s.Receiver = m.cp
s.Tel = m.cpp
ReList += s.Receiver
PNList += s.Tel
s.SendCt()
for i in range(len(s.Receiver)):
            CtList.append(s.c)
s.Notice()
print("\n보낸 메세지 함")
for i in range(len(ReList)):
    print(f'회원 이름: {ReList[i]}, 전화번호: {PNList[i]}, 내용: {CtList[i]}')
