from tkinter import *
import pickle
window = Tk()
window.title("dataBase")

name=Frame(window)
name.grid(row=0,column=0,sticky=N)
Label(name,text="이름: ").grid(row=0,column=0,sticky=N)
Nm=Entry(name,width=20,bg="light green")
Nm.grid(row=0,column=1,sticky=N)

datas=Frame(window)
datas.grid(row=0,column=1,sticky=E)

dataList={'score':{'title':'점수:','width':7,'color':'light green'},'num':{'title':'번호:','width':5, 'color':'light green'},"file":{'title':'파일이름:','width':20,'color':'light blue'}}
dataListKey=['score','num','file','file']
buttonList=["추가","삭제","저장","열기"]

dtNm=[] # 엔티티 네임의 리스
Dt=[]   # 저장할 데이터들을 위한 리스트
numDt=0 # 데이터 갯수
maxId=1 # Id의 MAX 값
def is_digit(str):
    print(str)
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False

def click(Name):
    print("Name",Name)
    global numDt
    global maxId
    global Dt
    isTrue=True
    if Name == "추가":
        print("numDT",numDt)
        for i in range(0,numDt):
            print("DT",Dt[i][1])
            if Nm.get()==Dt[i][1]:
                print("이름같음")
                STR="동일한 이름이 존재합니다."
                isTrue=False
                break
        print
        if not is_digit(dtNm[0].get()):
            print("점수")
            STR="점수가 정확하지 않습니다."
            isTrue=False
        if Nm.get()=="":
            print("이름이 공백입니다.")
            STR="이름이 공백입니다."
            isTrue=False

        if isTrue:            
            try:
                print("numDT1",numDt)
                numDt+=1
                print("numDT2",numDt)
                Dt.append([maxId,Nm.get(),dtNm[0].get()])
                string="%3d %15s %2.2f\n" %(Dt[numDt-1][0],Dt[numDt-1][1],eval(Dt[numDt-1][2]))
                state.delete("1.0",END)
                print("numDT2",numDt)
                dataOut.insert(END,string)
                print("numDT2",numDt)
                Nm.delete(0,END)
                print("numDT2",numDt)
                dtNm[0].delete(0,END)
                print("numDT2",numDt)
                maxId+=1
                print(Dt)
            except:
                numDt-=1
                Dt.pop()
            state.delete("1.0",END)
            state.insert(END,"성공적으로 추가하였습니다.")
        else:
            state.delete("1.0",END)
            state.insert(END,"[추가 실패] "+STR)
        
    elif Name=="삭제":
        
        try:
            if not is_digit(dtNm[1].get()):
                raise
            if numDt>=eval(dtNm[1].get()):
                Dt= Dt[:eval(dtNm[1].get())-1] + Dt[eval(dtNm[1].get()):]
                if numDt>0:
                    numDt-=1
                    click("출력")
                
                state.delete("1.0",END)
                state.insert(END,"성공적으로 삭제하였습니다.")
            else:
                raise
            maxId=Dt[-1][0]
        except:
            state.delete("1.0",END)
            state.insert(END,"삭제에 실패하였습니다.")

    elif Name=="저장":
        try:
            f=open(dtNm[2].get()+".txt","wb")
            pickle.dump(Dt, f)
            f.close()
            state.delete("1.0",END)
            state.insert(END,"성공적으로 저장하였습니. (파일이름 :"+dtNm[2].get()+")")
            dtNm[2].delete(0,END)
        except:
            state.delete("1.0",END)
            state.insert(END,"파일 저장에 실패하였습니다.")
    elif Name=="열기":
        try:
            f=open(dtNm[3].get()+".txt","rb")
            Dt=pickle.load(f)
            print(Dt)
            click("출력")
            f.close()
            state.delete("1.0",END)
            state.insert(END,"성공적으로 파일을 읽었습니다. (파일이름 : "+dtNm[3].get()+")")
            dtNm[3].delete(0,END)
            maxId=Dt[-1][0]+1
        except:
            state.delete("1.0",END)
            state.insert(END,"파일 불러오기에 실패하였습니다.")
    elif Name=="출력":
        numDt=len(Dt)
        dataOut.delete("1.0",END)
        for index in range(0,numDt):
            string="%3d %15s %2.2f\n" %(Dt[index][0],Dt[index][1],eval(Dt[index][2]))
            dataOut.insert(END,string)
            print("index",index)
    elif Name == 0:
        def nThElement(value):
            return value[0]
        Dt=sorted(Dt,reverse=False, key=nThElement)
        state.delete("1.0",END)
        click("출력")
    elif Name == 1:
        def nThElement(value):
            return value[1]
        state.delete("1.0",END)
        Dt=sorted(Dt,reverse=False, key=nThElement)
        click("출력")
    elif Name == 2:
        def nThElement(value):
            print(value[2])
            return float(value[2])
        state.delete("1.0",END)
        Dt=sorted(Dt,reverse=False, key=nThElement)
        click("출력")
    elif Name == 3:
        def nThElement(value):
            print(value[2])
            return float(value[2])
        state.delete("1.0",END)
        Dt=sorted(Dt,reverse=True, key=nThElement)
        click("출력")
        

        

                  
rowNum=0
for key in dataListKey:
    Label(datas,text=dataList[key]['title']).grid(row=rowNum,column=0,sticky=E)
    dtNm.append(Entry(datas,width=dataList[key]['width'],bg=dataList[key]['color']))
    dtNm[rowNum].grid(row=rowNum,column=1,sticky=W)
    rowNum+=1

rowNum=0
for buttonName in buttonList:
    def cmd(x=buttonName):
        click(x)
    Button(datas, text = buttonName, width = 5, command=cmd).grid(row=rowNum,column=3)
    rowNum+=1


sortBtn=Frame(window)
sortBtn.grid(row=1,column=0,columnspan=2)

sortBtnL={"num":{"title":"번호순","width":5,"func":0},
          "name":{"title":"이름순","width":5,"func":1},
          "scoreAsc":{"title":"점수내림차순","width":15,"func":2},
          "scoredesc":{"title":"점수오름차","width":15,"func":3}
          }
sortL=["num","name","scoreAsc","scoredesc"]
colNum=0 
for key in sortL:
    def cmd(x=sortBtnL[key]['func']):
        print(sortBtnL[key]['func'])
        click(x)
    Button(sortBtn, text = sortBtnL[key]['title'], width = sortBtnL[key]['width'], command=cmd).grid(row=0,column=colNum,sticky=E)
    colNum+=1


data=Frame(window, width=750,height=10,bg="light yellow")
data.grid(row=2,column=0,columnspan=2)

dataOut=Text(data,width=75,height=10,wrap=WORD,background="light yellow")
dataOut.grid(row=0,column=0)

state=Text(data,width=75,height=1,bg="pink")
state.grid(row=1,column=0)
