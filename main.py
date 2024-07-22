import tkinter as tk

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



frame_out.grid(row=2,column=0)





main_frame.grid()

root.mainloop()