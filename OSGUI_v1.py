from tkinter import *
from tkinter import ttk
from random import randint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Operating System GUI")
#root.iconbitmap('python.ico')
root.geometry('500x550')

def hide(widget):
    # This will remove the widget from toplevel
    # widget.place_forget()
    widget.place(y=1000)
#############################################################################
f1 = ttk.Labelframe(root, text="Scheduale Data")
f1.place(x=10, y=5, width=480, height=105)
###########(######## FUNCTION #######################
NoProcess = 5
Quantum = 2
Num_Process = 5
def Scheduale(*args):
    begin()
    if value_inside.get() == options_list[1]:
        lblProcesses.place(x=70, y=59)
        entProcesses.place(width=80, x=200, y=59)
        btnProcesses.place(x=330, y=56)
    elif value_inside.get() == options_list[2] or value_inside.get() == options_list[4]:
        lblProcesses.place(x=70, y=59)
        entProcesses.place(width=80, x=200, y=59)
        btnProcesses.place(x=330, y=56)
        rb1.place(x=265, y=0)
        rb2.place(x=265, y=25)
    elif value_inside.get() == options_list[3]:
        lblProcesses.place(x=70, y=59)
        entProcesses.place(width=80, x=200, y=59)
        btnProcesses.place(x=330, y=56)
        lblQuantum.place(x=10, y=28)
        entQuantum.place(x=105, y=28, width=50)
def Deactivate():
    global NoProcess, Quantum
    if entProcesses.get() == "":
        NoProcess = randint(2, 5)
    if entQuantum.get() == "":
        Quantum = randint(2, 3)
    rb1.configure(state=['disabled'])
    rb2.configure(state=['disabled'])
    question_menu.configure(state=['disabled'])
    btnProcesses.configure(state=['disabled'])
    if pree.get() != 'Preemptive' and pree.get() != 'Non-Preemptive':
        pree.set('Non-Preemptive')
    if entProcesses.get() == "":
        entProcesses.insert(0, str(NoProcess))
    if entQuantum.get() == "":
        entQuantum.insert(0, str(Quantum))
    entQuantum.configure(state=['disabled'])
    entProcesses.configure(state=['disabled'])
def Submit():
    global NoProcess, Quantum, num, Num_Process
    if entProcesses.get() != "":
        NoProcess = int(entProcesses.get())
    if value_inside.get() == options_list[3] and entQuantum.get() != "":
        Quantum = int(entQuantum.get())
    Deactivate()
    Show_Processes_Data()
    if len(lstProcesses) == 0:
        lstProcesses.append(lstTime)
        lstProcesses.append(lstPriority)
        lstProcesses.append(lstArrival)
    num = 0
    string.set("Process no. " + str(num))
    lblProcess.configure(text=string.get())
    Num_Process = NoProcess
def Show_Processes_Data():
    lblProcess.place(x=30, y=0)
    lblTime.place(x=155, y=25)
    lblArrival.place(x=5, y=25)
    #(x=5, y=25) (x=75, y=25, width=50), (x=145, y=25) (x=203, y=25, width=50), (x=270, y=25) (x=350, y=25, width=50)
    entTime.place(x=227, y=25, width=50)
    entArrival.place(x=85, y=25, width=50)
    btnNext.place(x=300, y=52, width=60)
    if value_inside.get() == options_list[4]:
        lblPriority.place(x=297, y=25)
        entPriority.place(x=350, y=25, width=50)
####################################################
# Scheduale Option menu
options_list = ["Scheduale Type", "FCFS", "SJF", "Round-Robin", "Priority"]
value_inside = StringVar(f1)
value_inside.set(options_list[0])
question_menu = ttk.OptionMenu(f1, value_inside, *options_list)
value_inside.trace('w', Scheduale)
question_menu.place(width=120, height=25, x=10, y=0)

# Quantum time lbl & Entry
lblQuantum = ttk.Label(f1, text="Quantum Time :")
lblQuantum.place(x=10, y=28)
entQuantum = ttk.Entry(f1)
entQuantum.place(x=105, y=28, width=50)

# Preemptive or not
rb1 = ttk.Radiobutton(f1, text="Preemptive")
rb2 = ttk.Radiobutton(f1, text="Non-Preemptive")
pree = StringVar()
rb1.config(variable=pree, value="Preemptive")
rb2.config(variable=pree, value="Non-Preemptive")
rb1.place(x=265, y=0)
rb2.place(x=265, y=25)

# Number of Processes
lblProcesses = ttk.Label(f1, text="Number of Processes : ")
lblProcesses.place(x=70, y=59)
# Processes Entry
entProcesses = ttk.Entry(f1)
entProcesses.place(width=80, x=200, y=59)
# Processes btn
btnProcesses = ttk.Button(f1, text="Submit")
btnProcesses.config(command=lambda: Submit())
btnProcesses.place(x=330, y=56)
#################################################################################
f2 = ttk.Labelframe(root, text="Processes Data")
f2.place(x=10, y=115, width=480, height=100)
f3 = ttk.Labelframe(root, text="Gantt Chart")
f3.place(x=10, y=220, width=480, height=265)
################### FUNCTION #######################
avgWT = 0
# Declaring a figure "gnt"
fig, gnt = plt.subplots()
canvas = FigureCanvasTkAgg(fig, f3)
lstArrival = []
lstTime = []
lstPriority = []
lstProcesses = []
lstProcesses.append(lstTime)
lstProcesses.append(lstPriority)
lstProcesses.append(lstArrival)
lstStart = []
lstEnd = []
lstIndex = []
lstLegend = []
def Next():
    global Num_Process, num, string
    if int(Num_Process) == 1:
        hide(btnNext)
        btnOutput.place(x=380, y=52, width=80)
        entPriority.configure(state=["disabled"])
        entTime.configure(state=["disabled"])
        entArrival.configure(state=["disabled"])
    else:
        num = num + 1
        string.set("Process no. " + str(num))
        lblProcess.configure(text=string.get())
    Num_Process = int(Num_Process) - 1
    if entTime.get() != "":
        lstProcesses[0].append(int(entTime.get()))
    else:
        lstProcesses[0].append(randint(1, 5))
    if entArrival.get() != "":
        lstProcesses[2].append(int(entArrival.get()))
    else:
        lstProcesses[2].append(randint(1, 5))
    if value_inside.get() == options_list[4]:
        if entPriority.get() != "":
            lstProcesses[1].append(int(entPriority.get()))
        else:
            lstProcesses[1].append(randint(1, 5))
    entTime.delete(0, END)
    entArrival.delete(0, END)
    if value_inside.get() == options_list[4]:
        entPriority.delete(0, END)
def Calc():
    global lstStart, lstEnd, lstIndex, avgWT, lstProcesses
    done = 0
    time = 0
    first = 0
    q = []
    tmp = []
    time = min(lstProcesses[2])
    if value_inside.get() == options_list[1]:
        #FCFS
        ##FCFS(NoProcess, lstProcesses[0], lstProcesses[2])
        ##avgWT = waitingTimeFCFS()
        while done < NoProcess:
            for j in range(NoProcess):
                if lstProcesses[2][j] == time:
                    q.append([lstProcesses[0][j], j])
            if len(q) != 0:
                i = q[0][1]
                if done == 0:
                    lstStart.append(time)
                    lstEnd.append(lstStart[-1] + lstProcesses[0][i])
                else:
                    if lstProcesses[2][i] > lstEnd[-1]:
                        lstStart.append(time)
                    else:
                        lstStart.append(lstEnd[-1])
                    lstEnd.append(lstStart[-1] + lstProcesses[0][i])
                lstIndex.append(i)
                q.pop(0)
                done += 1
            time += 1

    elif value_inside.get() == options_list[2] and pree.get() == "Preemptive":
        # SJF #Preemptive
        while done < NoProcess:
            if len(q) == 0:
                first = 1
            else:
                first = 0
            for j in range(NoProcess):
                if lstProcesses[2][j] == time:
                    q.append([lstProcesses[0][j], j])
            q.sort()
            if len(q) != 0:
                i = q[0][1]
                if q[0][0] != 999:
                    if q[0][0] > 1:
                        if first == 1:
                            lstStart.append(time)
                        else:
                            if lstProcesses[2][i] > lstEnd[-1]:
                                lstStart.append(time)
                            else:
                                lstStart.append(lstEnd[-1])
                        q[0][0] -= 1
                        lstEnd.append(time + 1)
                    else:
                        if first == 1:
                            lstStart.append(time)
                        else:
                            if lstProcesses[2][i] > lstEnd[-1]:
                                lstStart.append(time)
                            else:
                                lstStart.append(lstEnd[-1])
                        lstEnd.append(time + 1)
                        q[0][0] = 999
                        done += 1
                    lstIndex.append(i)
            time += 1

    elif value_inside.get() == options_list[2] and pree.get() == "Non-Preemptive":
        #SJF #Non-Preemptive
        while done < NoProcess:
            for j in range(NoProcess):
                if lstProcesses[2][j] == time:
                    q.append([lstProcesses[0][j], j])
            q.sort()
            if len(q) != 0:
                i = q[0][1]
                if q[0][0] != 999:
                    if done == 0:
                        lstStart.append(time)
                        lstEnd.append(lstStart[-1] + lstProcesses[0][i])
                    else:
                        if lstProcesses[2][i] > lstEnd[-1]:
                            lstStart.append(time)
                        else:
                            lstStart.append(lstEnd[-1])
                        lstEnd.append(lstStart[-1] + lstProcesses[0][i])
                    lstIndex.append(i)
                    q[0][0] = 999
                    done += 1
            time += 1
    elif value_inside.get() == options_list[3]:
        #Round Robin
        #rr(NoProcess)
        for i in range(NoProcess):
            tmp.append(lstProcesses[2][i])
        for j in range(NoProcess):
            if tmp[j] <= time and tmp[j] != -1:
                q.append([lstProcesses[0][j], j])
                tmp[j] = -1
        while done < NoProcess:
            if len(q) != 0:
                i = q[0][1]
                if lstProcesses[0][i] > Quantum:
                    lstProcesses[0][i] = lstProcesses[0][i] - Quantum
                    lstStart.append(time)
                    lstEnd.append(lstStart[-1] + Quantum)
                    time += Quantum
                else:
                    lstStart.append(time)
                    lstEnd.append(lstStart[-1] + lstProcesses[0][i])
                    time += lstProcesses[0][i]
                    lstProcesses[0][i] -= lstProcesses[0][i]
                    done += 1
                lstIndex.append(i)
                for j in range(NoProcess):
                    if tmp[j] <= time and tmp[j] != -1:
                        q.append([lstProcesses[0][j], j])
                        tmp[j] = -1
                if lstProcesses[0][i] > 0:
                    q.append([lstProcesses[0][i], i])
                q.pop(0)
            else:
                for j in range(NoProcess):
                    if tmp[j] <= time and tmp[j] != -1:
                        q.append([lstProcesses[0][j], j])
                        tmp[j] = -1
                time += 1
    elif value_inside.get() == options_list[4] and pree.get() == "Preemptive":
        #Priority #Preemptive
        while done < NoProcess:
            if len(q) == 0:
                first = 1
            else:
                first = 0
            for j in range(NoProcess):
                if lstProcesses[2][j] == time:
                    q.append([lstProcesses[1][j], j])
            q.sort()
            if len(q) != 0:
                i = q[0][1]
                if q[0][0] != 999:
                    if lstProcesses[0][i] > 1:
                        if first == 1:
                            lstStart.append(time)
                        else:
                            if lstProcesses[2][i] > lstEnd[-1]:
                                lstStart.append(time)
                            else:
                                lstStart.append(lstEnd[-1])
                        lstProcesses[0][i] -= 1
                        lstEnd.append(time + 1)
                    else:
                        if first == 1:
                            lstStart.append(time)
                        else:
                            if lstProcesses[2][i] > lstEnd[-1]:
                                lstStart.append(time)
                            else:
                                lstStart.append(lstEnd[-1])
                        lstEnd.append(time + 1)
                        q[0][0] = 999
                        done += 1
                    lstIndex.append(i)
            time += 1

    elif value_inside.get() == options_list[4] and pree.get() == "Non-Preemptive":
        while done < NoProcess: #Priority #nonPreemptive
            for j in range(NoProcess):
                if lstProcesses[2][j] == time:
                    q.append([lstProcesses[1][j], j])
            q.sort()
            if len(q) != 0:
                i = q[0][1]
                if q[0][0] != 999:
                    if done == 0:
                        lstStart.append(time)
                        lstEnd.append(lstStart[-1] + lstProcesses[0][i])
                        lstIndex.append(i)
                        q[0][0] = 999
                        done += 1
                    else:
                        if time >= lstEnd[-1]:
                            if lstProcesses[2][i] > lstEnd[-1]:
                                lstStart.append(time)
                            else:
                                lstStart.append(lstEnd[-1])
                            lstEnd.append(lstStart[-1] + lstProcesses[0][i])
                            lstIndex.append(i)
                            q[0][0] = 999
                            done += 1
            time += 1
    ### When finish delete these lists ###
    #lstStart = [0, 5, 8, 10, 13, 17]
    #lstEnd = [5, 8, 10, 13, 17, 22]
    #lstIndex = [1, 2, 1, 3, 4, 3]
    ######################################
    lstProcesses.append(lstStart)
    lstProcesses.append(lstEnd)
    lstProcesses.append(lstIndex)
def Get_Color(Num):
    if Num % 10 == 0:
        return 'tab:green'
    elif Num % 10 == 1:
        return 'tab:blue'
    elif Num % 10 == 2:
        return 'tab:orange'
    elif Num % 10 == 3:
        return 'tab:red'
    elif Num % 10 == 4:
        return 'tab:purple'
    elif Num % 10 == 5:
        return 'tab:brown'
    elif Num % 10 == 6:
        return 'tab:pink'
    elif Num % 10 == 7:
        return 'tab:gray'
    elif Num % 10 == 8:
        return 'tab:cyan'
    elif Num % 10 == 9:
        return 'tab:olive'
def Unique_List():
    global lstProcesses, lstLegend, NoProcess
    for i in range(len(lstProcesses[5])):
        flag = False
        for j in range(len(lstLegend)):
            if lstLegend[j] == lstProcesses[5][i]:
                flag = True
                break
        if flag == False:
            lstLegend.append(lstProcesses[5][i])
def Gantt():
    global NoProcess, toolbar, canvas, fig, gnt, lstLegend
    Calc()
    #Draw The Chart
    # Setting X,Y-axis limits
    gnt.set_ylim(0, 20)
    Sum = lstProcesses[4][len(lstProcesses[5])-1]
    Sum += Sum / 10
    gnt.set_xlim(0, Sum)
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time in clks')
    gnt.set_ylabel('Tasks')
    # Setting ticks on y-axis
    lstYLines = [5, 20, 30]
    lstYNames = []
    lstXLines = []
    Unique_List()
    gnt.set_yticks(lstYLines)
    for i in range(1, NoProcess+1):
        if (value_inside.get() == options_list[4] and pree.get() == "Preemptive") or (value_inside.get() == options_list[2] and pree.get() == "Preemptive") or value_inside.get() == options_list[3]:
            Str = "P" + str(lstLegend[i - 1])
        else:
            Str = "P" + str(lstProcesses[5][i - 1])
        lstYNames.append(Str)
        gnt.set_yticklabels([])
    if (value_inside.get() == options_list[2] and pree.get() == "Preemptive") or (value_inside.get() == options_list[4] and pree.get() == "Preemptive"):
        new_start = []  # new start array for drawing
        new_end = []  # new end array for drawing
        new_index = []  # new index array for drawing
        for k in range(len(lstIndex)):
            if k == 0:
                new_start.append(lstStart[0])
                new_index.append(lstIndex[k])
            elif lstIndex[k] != lstIndex[k - 1]:
                new_end.append(lstEnd[k - 1])
                new_start.append(lstStart[k])
                new_index.append(lstIndex[k])
        new_end.append(lstEnd[-1])  # To add the last item in end array
        lstProcesses[3].clear()
        lstProcesses[4].clear()
        lstProcesses[5].clear()
        lstProcesses[3] = new_start
        lstProcesses[4] = new_end
        lstProcesses[5] = new_index
    lstXLines.append(0)
    if lstProcesses[3][0] != 0:
        lstXLines.append(lstProcesses[3][0])
    for i in range(len(lstProcesses[5])):
        if lstXLines[-1] != lstProcesses[3][i]:
            lstXLines.append(lstProcesses[3][i])
        lstXLines.append(lstProcesses[4][i])
        gnt.set_xticks(lstXLines)
        gnt.set_xticklabels(lstXLines)
    # Labelling tickes of y-axis
    # Setting graph attribute
    gnt.grid(True)
    # Declaring a bar in schedule
    for i in range(len(lstProcesses[3])):
        gnt.broken_barh([(lstProcesses[3][i], lstProcesses[4][i]-lstProcesses[3][i])], (5, 15), facecolors=(Get_Color(lstProcesses[5][i])))
    gnt.legend(lstYNames, bbox_to_anchor=(0.9, 1.15), loc='upper left')
    if (value_inside.get() == options_list[4] and pree.get() == "Preemptive") or (
            value_inside.get() == options_list[2] and pree.get() == "Preemptive") or value_inside.get() == options_list[3]:
        ax = plt.gca()
        leg = ax.get_legend()
        for i in range(len(lstLegend)):
            leg.legendHandles[i].set_color(Get_Color(lstLegend[i]))
    # Declaring multiple bars in at same level and same widthgnt.clear()
    canvas.draw()
    Show_AvgTime()
    btnOutput.config(state=["disabled"])
def avgWaitingTime (n,start,end,at,index):
    wt = []
    for i in range (n):
        count = 0
        wait = 0
        for j in range (len(index)):
            if i == index[j]:
                count += 1
        for j in range (len(index)):
            if i != index[j]:
                gap = 0
                if start[j] != end[j-1] and j != 0:
                    gap = start[j] - end[j-1]
                wait += end[j] - start[j] + gap
            else:
                count -= 1
                if count == 0:
                    break;
        wait -= (at[i] - start[0])
        if wait < 0:
            wait = 0
        wt.append(wait)
    s = 0   #sum
    for j in range (len(wt)):
        s += wt[j]
    avg = s / n     #average time
    return avg
def Show_AvgTime():
    global strAvg, avgWT, NoProcess
    lblAvgWT.place(x=15, y=5)
    avgWT = avgWaitingTime(NoProcess, lstProcesses[3], lstProcesses[4], lstProcesses[2], lstProcesses[5])
    strAvg.set(str(avgWT))
    lblAvgWTValue.config(text=strAvg.get())
    lblAvgWTValue.place(x=127, y=5)
####################################################
# label Process
num = 0
string = StringVar()
string.set("Process no. " + str(num))
lblProcess = ttk.Label(f2, text=string.get())
lblProcess.place(x=30, y=0)

# Burst Time lbl & Entry
lblTime = ttk.Label(f2, text="Burst Time :")
lblTime.place(x=5, y=25)
entTime = ttk.Entry(f2)
entTime.place(x=75, y=25, width=50)
# Priority lbl & Entry
lblPriority = ttk.Label(f2, text="Priority :")
lblPriority.place(x=145, y=25)
entPriority = ttk.Entry(f2)
entPriority.place(x=203, y=25, width=50)
# Arrival lbl & Entry
lblArrival = ttk.Label(f2, text="Arrival Time :")
lblArrival.place(x=242, y=25)
entArrival = ttk.Entry(f2)
entArrival.place(x=320, y=25, width=50)
# Next btn
btnNext = ttk.Button(f2, text="Next")
btnNext.config(command=lambda: Next())
btnNext.place(x=300, y=48, width=60)
# Get Output btn
btnOutput = ttk.Button(f2, text="Get Output")
btnOutput.config(command=lambda:Gantt())
btnOutput.place(x=380, y=48, width=80)
#################################################################################
f4 = ttk.Labelframe(root, text="Average Waiting Time")
f4.place(x=10, y=490, width=480, height=50)
################### FUNCTION #######################
strAvg = StringVar()
strAvg.set(avgWT)
def begin():
    global gnt, canvas
    hide(lblQuantum)
    hide(entQuantum)
    hide(rb1)
    hide(rb2)
    hide(entProcesses)
    hide(lblProcesses)
    hide(btnProcesses)
    hide(lblProcess)
    hide(lblTime)
    hide(entTime)
    hide(lblArrival)
    hide(entArrival)
    hide(lblPriority)
    hide(entPriority)
    hide(btnOutput)
    hide(btnNext)
    hide(lblAvgWT)
    hide(lblAvgWTValue)
    canvas.draw()
    canvas.get_tk_widget().place(x=5, y=10, width=468, height=225)
    gnt.clear()
def clean():
    entQuantum.configure(state=['!disabled'])
    entProcesses.configure(state=['!disabled'])
    entTime.configure(state=['!disabled'])
    entArrival.configure(state=['!disabled'])
    entPriority.configure(state=['!disabled'])
    rb1.configure(state=['!disabled'])
    rb2.configure(state=['!disabled'])
    question_menu.configure(state=['!disabled'])
    btnProcesses.configure(state=['!disabled'])
    btnOutput.configure(state=['!disabled'])
    entQuantum.delete(0, END)
    entProcesses.delete(0, END)
    entTime.delete(0, END)
    entArrival.delete(0, END)
    entPriority.delete(0, END)
    pree.set("")
def start():
    begin()
    value_inside.set(options_list[0])
    clean()
    for i in range(len(lstProcesses)):
        lstProcesses[i].clear()
    lstProcesses.clear()
    lstLegend.clear()
    lstStart.clear()
    lstEnd.clear()
    lstIndex.clear()
    lstTime.clear()
    lstArrival.clear()
    lstPriority.clear()
####################################################
# Average Waiting Time Show
lblAvgWT = ttk.Label(f4, text="Avg Waiting Time : ")
lblAvgWT.place(x=15, y=5)
# Deactivated Entry
lblAvgWTValue = ttk.Label(f4, text=strAvg.get())
lblAvgWTValue.place(x=127, y=5)
# Reset btn
btnReset = ttk.Button(f4, text="Reset")
btnReset.config(command=lambda: start())
btnReset.place(x=390, y=3, width=80)
btnReset.invoke()


root.mainloop()