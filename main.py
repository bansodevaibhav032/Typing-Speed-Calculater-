import tkinter as tk
from tkinter import ttk

root= tk.Tk()

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
selected_paragraph= 'India has given to the world many a great cricketer but perhaps none as ambitious as Virat Kohli. To meet his ambition, Kohli employed the technical assiduousness of Sachin Tendulkar and fitness that was in the league of top athletes in the world, not just cricketers. As a result, Kohli became the most consistent all-format accumulator of his time, making jaw-dropping chases look easy, and finding, in his own words, the safest possible way to score runs. Plenty of them.'
frame_test=tk.LabelFrame(main_frame,text='Test',bg='white',relief='flat')

# paragraph
lbl_paragraph=tk.Label(frame_test,text=selected_paragraph, wraplength=1000,justify='left')
lbl_paragraph.grid(row=0,column=0,pady=5,padx=5)

# inputbox
entry=tk.Text(frame_test,height=8,width=120,border=2)
entry.grid(row=1, column=0,pady=5,padx=5)

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
lbl_remainingtimer= tk.Label(frame_labels,text='0',font='tahoma 10 bold',fg='black',bg='white')


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
btn_start= ttk.Button(frame_control,text='Start')

btn_start.grid(row=0,column=0,padx=10)

# reset 
btn_reset= ttk.Button(frame_control,text='Reset')

btn_reset.grid(row=0,column=1)

frame_control.grid(row=1)


frame_out.grid(row=2,column=0,padx=10)


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
# z-
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

root.mainloop()