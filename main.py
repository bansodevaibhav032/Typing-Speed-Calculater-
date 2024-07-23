import tkinter as tk
from tkinter import ttk
import ttkthemes as tt
import time as tm
import threading as td 
import random as r 

# initial variables

timelimit=60
remainingtime= timelimit
elpasedtime=0
elpasedtimeinmin=0

totalwords=0
wrongwords=0

wpm=0
accuracy=0

def start_time():
    global elpasedtime


    entry.focus()
    entry.config(state='normal')
    btn_start.config(state='disabled')

    for time in range(1,timelimit+1):
        elpasedtime=time
        lbl_elpasedtimer['text']=elpasedtime

        updatedremainingtime= remainingtime-elpasedtime
        lbl_remainingtimer['text']=updatedremainingtime


        tm.sleep(1)
        root.update()

    entry.config(state='disabled')
    btn_reset.config(state='normal')


def count():
    global wrongwords
    global elpasedtime
    global elpasedtimeinmin

    para_words=lbl_paragraph['text'].split()

    while elpasedtime != timelimit:
        enteredparagraph= entry.get(1.0,'end-1c').split()
        totalwords=len(enteredparagraph)

    # para words
    # enteredparagraph 

    for pair in list(zip(para_words,enteredparagraph)):
        if pair[0] !=pair[1]:
            wrongwords +=1

    elpasedtimeinmin=elpasedtime/60

    #wpm
    # ( totalwords=wrongwords) / time in minutes
    wpm = (totalwords-wrongwords)/elpasedtimeinmin
    lbl_wpm['text']=wpm

    #accuracy
    # accuracy=(wpm/gross_wpm)*100
    gross_wpm=totalwords/elpasedtimeinmin
    accuracy=(wpm/gross_wpm)*100
    lbl_accuracy['text']=round(accuracy,2)
    

    # total words
    lbl_tw['text']=totalwords

    # wrong words
    lbl_ww['text']=wrongwords



def start():
    thr1=td.Thread(target=start_time)
    thr1.start()
    thr2=td.Thread(target=count)
    thr2.start()


def reset():
    global remainingtime
    global elpasedtime

    btn_reset.config(state='disabled')
    btn_start.config(state='normal')

    entry.config(state='normal')
    entry.delete(1.0,tk.END)
    entry.config(state='disabled')

    remainingtime=timelimit
    elpasedtime=0

    lbl_elpasedtimer['text']=0
    lbl_remainingtimer['text']=0
    lbl_wpm['text']=0
    lbl_accuracy['text']=0
    lbl_tw['text']=0
    lbl_ww['text']=0

# Channging Paragraph 

with open('paragraph.txt', encoding='utf-8') as f:
    paragraphs= f.readlines()
    selected_paragraph=r.choice(paragraphs)








# ****************************** GUI ************************************

root= tt.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.title("Typing Speed Calculater!")
root.geometry('1140x800+250+10')
root.resizable(False,False)
 

# main frame
main_frame= tk.Frame(root,bg="white",bd=4)


# title frame
frame_title= tk.Frame(main_frame,bg='orange',relief='groove')
lbl_title=tk.Label(frame_title,text='Typo speed',font='algerian 35 bold',bg='cyan',fg='black',relief='flat',bd=10,width=37)
lbl_title.grid(row=0,column=0,pady=10)


frame_title.grid(row=0,column=0)

# test frame
frame_test=tk.LabelFrame(main_frame,text='Test',bg='white',relief='groove')

# paragraph
lbl_paragraph=tk.Label(frame_test,text=selected_paragraph, wraplength=1000,justify='left')
lbl_paragraph.grid(row=0,column=0,pady=5,padx=5)

# inputbox
entry=tk.Text(frame_test,height=8,width=120,border=2)
entry.grid(row=1, column=0,pady=5,padx=5)
entry.config(state='disabled')

frame_test.grid(row=1,column=0)

# output frame
frame_out=tk.Frame(main_frame,bg='white',relief='flat')

frame_labels=tk.Frame(frame_out,bg='white')

# elapsed time
lbl_elpasedtime= tk.Label(frame_labels,text='Elpased time',font='tahoma 10 bold', fg='red',bg='white')
lbl_elpasedtimer= tk.Label(frame_labels,text='0',font='tahoma 10 bold',fg='black',bg='white')


lbl_elpasedtime.grid(row=0,column=0,padx=10,pady=10)
lbl_elpasedtimer.grid(row=0,column=1,padx=10,pady=10)

# remaining time 
lbl_remainingtime= tk.Label(frame_labels,text='Remaining time',font='tahoma 10 bold', fg='red',bg='white')
lbl_remainingtimer= tk.Label(frame_labels,text='60',font='tahoma 10 bold',fg='black',bg='white')


lbl_remainingtime.grid(row=0,column=2,padx=10,pady=10)
lbl_remainingtimer.grid(row=0,column=3,padx=10,pady=10)

# wpm
lbl_wpm_title= tk.Label(frame_labels,text='WPM',font='tahoma 10 bold', fg='red',bg='white')
lbl_wpm= tk.Label(frame_labels,text='0',font='tahoma 10 bold',fg='black',bg='white')


lbl_wpm_title.grid(row=0,column=4,padx=10,pady=10)
lbl_wpm.grid(row=0,column=5,padx=10,pady=10)

# accuracy 
lbl_accuracy_title= tk.Label(frame_labels,text='Accuracy',font='tahoma 10 bold', fg='red',bg='white')
lbl_accuracy= tk.Label(frame_labels,text='0',font='tahoma 10 bold',fg='black',bg='white')


lbl_accuracy_title.grid(row=0,column=6,padx=10,pady=10)
lbl_accuracy.grid(row=0,column=7,padx=10,pady=10)

# total words
lbl_tw_title= tk.Label(frame_labels,text='Total Words',font='tahoma 10 bold', fg='red',bg='white')
lbl_tw= tk.Label(frame_labels,text='0',font='tahoma 10 bold',fg='black',bg='white')


lbl_tw_title.grid(row=0,column=8,padx=10,pady=10)
lbl_tw.grid(row=0,column=9,padx=10,pady=10)

# wrong words
lbl_ww_title= tk.Label(frame_labels,text='Wrong Words',font='tahoma 10 bold', fg='red',bg='white')
lbl_ww= tk.Label(frame_labels,text='0',font='tahoma 10 bold',fg='black',bg='white')


lbl_ww_title.grid(row=0,column=10,padx=10,pady=10)
lbl_ww.grid(row=0,column=11,padx=10,pady=10)


frame_labels.grid(row=0)

# Control Frame 
frame_control = tk.Frame(frame_out,bg='white')
# start 
btn_start= ttk.Button(frame_control,text='Start',command=start)

btn_start.grid(row=0,column=0,padx=10)

# reset 
btn_reset= ttk.Button(frame_control,text='Reset',command=reset)
btn_reset.grid(row=0,column=1,padx=10)
btn_reset.config(state="disabled")

frame_control.grid(row=1)


frame_out.grid(row=2,column=0)


# keyword frame 
frame_keyword = tk.Frame(main_frame,bg='white')
# 1-0
frame_1_0= tk.Frame(frame_keyword,bg='white')

lbl_1=tk.Label(frame_1_0,text='1',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_2=tk.Label(frame_1_0,text='2',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_3=tk.Label(frame_1_0,text='3',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_4=tk.Label(frame_1_0,text='4',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_5=tk.Label(frame_1_0,text='5',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_6=tk.Label(frame_1_0,text='6',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_7=tk.Label(frame_1_0,text='7',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_8=tk.Label(frame_1_0,text='8',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_9=tk.Label(frame_1_0,text='9',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_0=tk.Label(frame_1_0,text='0',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)

lbl_1.grid(row=0,column=0,padx=10,pady=5)
lbl_2.grid(row=0,column=1,padx=10,pady=5)
lbl_3.grid(row=0,column=2,padx=10,pady=5)
lbl_4.grid(row=0,column=3,padx=10,pady=5)
lbl_5.grid(row=0,column=4,padx=10,pady=5)
lbl_6.grid(row=0,column=5,padx=10,pady=5)
lbl_7.grid(row=0,column=6,padx=10,pady=5)
lbl_8.grid(row=0,column=7,padx=10,pady=5)
lbl_9.grid(row=0,column=8,padx=10,pady=5)
lbl_0.grid(row=0,column=9,padx=10,pady=5)

frame_1_0.grid(row=0)

# q-p
frame_p_q=tk.Frame(frame_keyword,bg='white')

lbl_Q=tk.Label(frame_p_q,text='Q',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_W=tk.Label(frame_p_q,text='W',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_E=tk.Label(frame_p_q,text='E',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_R=tk.Label(frame_p_q,text='R',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_T=tk.Label(frame_p_q,text='T',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_Y=tk.Label(frame_p_q,text='Y',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_U=tk.Label(frame_p_q,text='U',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_I=tk.Label(frame_p_q,text='I',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_O=tk.Label(frame_p_q,text='O',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_P=tk.Label(frame_p_q,text='P',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)

lbl_Q.grid(row=1,column=0,padx=10,pady=5)
lbl_W.grid(row=1,column=1,padx=10,pady=5)
lbl_E.grid(row=1,column=2,padx=10,pady=5)
lbl_R.grid(row=1,column=3,padx=10,pady=5)
lbl_T.grid(row=1,column=4,padx=10,pady=5)
lbl_Y.grid(row=1,column=5,padx=10,pady=5)
lbl_U.grid(row=1,column=6,padx=10,pady=5)
lbl_I.grid(row=1,column=7,padx=10,pady=5)
lbl_O.grid(row=1,column=8,padx=10,pady=5)
lbl_P.grid(row=1,column=9,padx=10,pady=5)

frame_p_q.grid(row=1)


# a-l
frame_a_l=tk.Frame(frame_keyword,bg='white')

lbl_A=tk.Label(frame_a_l,text='A',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_S=tk.Label(frame_a_l,text='S',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_D=tk.Label(frame_a_l,text='D',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_F=tk.Label(frame_a_l,text='F',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_G=tk.Label(frame_a_l,text='G',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_H=tk.Label(frame_a_l,text='H',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_J=tk.Label(frame_a_l,text='J',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_K=tk.Label(frame_a_l,text='K',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_L=tk.Label(frame_a_l,text='L',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)

lbl_A.grid(row=2,column=0,padx=10,pady=5)
lbl_S.grid(row=2,column=1,padx=10,pady=5)
lbl_D.grid(row=2,column=2,padx=10,pady=5)
lbl_F.grid(row=2,column=3,padx=10,pady=5)
lbl_G.grid(row=2,column=4,padx=10,pady=5)
lbl_H.grid(row=2,column=5,padx=10,pady=5)
lbl_J.grid(row=2,column=6,padx=10,pady=5)
lbl_K.grid(row=2,column=7,padx=10,pady=5)
lbl_L.grid(row=2,column=8,padx=10,pady=5)

frame_a_l.grid(row=2)
# z-m
frame_z_m=tk.Frame(frame_keyword,bg='white')

lbl_Z=tk.Label(frame_z_m,text='Q',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_X=tk.Label(frame_z_m,text='E',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_C=tk.Label(frame_z_m,text='R',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_V=tk.Label(frame_z_m,text='T',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_B=tk.Label(frame_z_m,text='Y',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_N=tk.Label(frame_z_m,text='W',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)
lbl_M=tk.Label(frame_z_m,text='U',bg='black',fg='white',width=5,height=2,relief='groove',bd=10)

lbl_Z.grid(row=3,column=0,padx=10,pady=5)
lbl_X.grid(row=3,column=1,padx=10,pady=5)
lbl_C.grid(row=3,column=2,padx=10,pady=5)
lbl_V.grid(row=3,column=3,padx=10,pady=5)
lbl_B.grid(row=3,column=4,padx=10,pady=5)
lbl_N.grid(row=3,column=5,padx=10,pady=5)
lbl_M.grid(row=3,column=6,padx=10,pady=5)

frame_z_m.grid(row=3)
# space
frame_space=tk.Frame(frame_keyword,bg='white')
lbl_space=tk.Label(frame_space,bg='black',fg='white',width=50,height=2,relief='groove',bd=10)

lbl_space.grid(row=0,column=0,padx=10,pady=5)
frame_space.grid(row=4)

frame_keyword.grid(row=3,pady=10)

main_frame.grid()


# key binding 
def changeBG(widget):
    bg='black'
    widget.configure(background='blue')
    widget.after(100,lambda color=bg : widget.configure(background=color))

labels_numbers=[lbl_1,lbl_2,lbl_3,lbl_4,lbl_5,lbl_6,lbl_7,lbl_8,lbl_9,lbl_0]
labels_alpha=[lbl_A,lbl_B,lbl_C,lbl_D,lbl_E,lbl_F,lbl_G,lbl_H,lbl_I,lbl_J,lbl_K,lbl_L,lbl_M,lbl_N,lbl_O,lbl_P,lbl_Q,lbl_R,lbl_S,lbl_T,lbl_U,lbl_V,lbl_S,lbl_T,lbl_U,lbl_V,lbl_W,lbl_X,lbl_Y,lbl_Z]
labels_space=[lbl_space]

binding_numbers=['1','2','3','4','5','6','7','8','9','0']
binding_capital_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
binding_small_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for num in range(len(binding_numbers)):
    root.bind(f"{binding_numbers[num]}",lambda event, label=labels_numbers[num]:changeBG(label))

for alphabet in range(len(binding_capital_alpha)):
    root.bind(f"{binding_capital_alpha[alphabet]}",lambda event, label=labels_alpha[alphabet]:changeBG(label))

for alphabet2 in range(len(binding_small_alpha)):
    root.bind(f"{binding_small_alpha[alphabet2]}",lambda event, label=labels_alpha[alphabet2]:changeBG(label))

root.bind("<space>",lambda event, label=labels_space[0]:changeBG(label))

root.mainloop() 