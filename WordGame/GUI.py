from tkinter import *
from tkinter import messagebox
import Connection
import pymysql
import random


## 변수 선언 부분 ##
dic = {};number_key={};new_dic={};new_number_key={};my_dic={};
num =0
temp = {};
question_check = 0
dic_choice = True

#객관식 보기 만들어주는 함수
def make_exam(num):
    selec = {};number=1
    number = 1
    exam = random.sample(range(len(dic)), num)
    for i in exam:
        selec[number] = [number_key[i],dic[number_key[i]]]
        number += 1
    return selec

## 클래스 선언 부분 ##
class Gui :

    def __init__(self, master) :

        self.master = master       # 주체를 바꿈
        self.master.title("공부할 영역 선택")   # 제목
        #self.master.deiconify()  # 보이게 만듬.
        self.frame = Frame(self.master, background = "lightskyblue")   # 객체를 달기위한 프레임 , 프레임 색상

        self.englishButton = Button(self.frame, text = "영어 단어", bg = "cyan", font = "bold", command = self.english_level_window) # 글자 색깔 바꾸려면 fg, bg는 배경색, font("bold", "고딕체") 이런것도 가
        self.phraseButton = Button(self.frame, text = "사자 성어", bg = "coral", font = "bold", command = self.phrase_window)

        self.englishButton.pack(expand = 1, side = LEFT, fill = BOTH)  # pack, grid, place 있는데 알아서 잘 사용하시고.
        self.phraseButton.pack(expand = 1, side = RIGHT, fill = BOTH)
        self.frame.pack(expand = 1, fill = BOTH)

    def english_level_window(self) :
        # 영어 문장 테스트를 위한 DB열기
        Connection.OpenSentence("sentencequiz", new_dic, new_number_key)
        global dic_choice
        dic_choice = True

        self.master.withdraw()  # 기존 window를 인비져블 하게 하고
        self.root2 = Toplevel() # Toplevel로 새로운 window창 생성
        self.root2.geometry("350x130+450+350") # 순서대로 가로길이 새로길이 창이 뜨는 고정 위치(x,y 좌표)
        self.root2.resizable(width = FALSE, height = FALSE)   # window창 크기를 변화할 수 없게 만듬.

        window2 = Gui2(self.root2)

    def phrase_window(self) :
        #사자 성어를 위한 DB열기
        global dic_choice
        dic_choice = False

        Connection.OpenWord("idiom", dic, number_key)
        self.master.withdraw()
        self.root3 = Toplevel()
        self.root3.geometry("872x600+450+350")
        self.root3.resizable(width = FALSE, height = FALSE)

        window3 = Gui3(self.root3)


class Gui2 :

    def __init__(self, master) :

        self.selectLevel = 0
        #result = False

        self.master = master
        self.master.title("난이도 선택")
        self.frame = Frame(self.master, background = "lightskyblue")

        self.selectLevel = IntVar()   # selectLevel은 라디오 버튼으로부터 값을 얻어오고 후에 여러 용도로 쓰임

        self.middleSt1 = Radiobutton(self.frame, text = "중학교 1학년 난이도",
                                     variable = self.selectLevel, value = 1, font = "bold", background = "lightskyblue")
        self.middleSt2 = Radiobutton(self.frame, text = "중학교 2학년 난이도",
                                     variable = self.selectLevel, value = 2, font = "bold", background = "lightskyblue")
        self.middleSt3 = Radiobutton(self.frame, text = "중학교 3학년 난이도",
                                     variable = self.selectLevel, value = 3, font = "bold", background = "lightskyblue")

        self.okBtn = Button(self.frame, text = "확인", font = "bold", background = "deepskyblue", command = self.checkOkCancel)
        #self.okBtn.bind("<Button-1>", self.clickOk)

        self.middleSt1.grid(row = 0, column = 15, padx = 30, pady = 7)
        self.middleSt2.grid(row = 11, column = 15, padx = 30, pady = 7)
        self.middleSt3.grid(row = 12, column = 15, padx = 30, pady = 7)
        self.okBtn.grid(row = 11, column = 25, padx = 20, pady = 7)
        self.frame.pack(expand = 1, fill = BOTH)

    def checkOkCancel(self) :

        if self.selectLevel.get() == 0 : # 아무것도 선택하지않고 확인을 눌렀을때 나타나는 경고
            messagebox.showinfo("선택하세요!", "난이도를 선택해 주세요~")
            return

        self.root4 = Toplevel()
        self.root4.geometry("350x130+450+350")
        self.root4.resizable(width = FALSE, height = FALSE)

        self.wrongAnswer = False # GUI_check를 사용할 때 쓰임

        window4 = Gui_check(self.root4, self.selectLevel, self.master, self.wrongAnswer)


class Gui_check : # 얘는 경고창이랑, 그림상 4번에 해당하는거를 동시에 사용하는데
    # wrongAnswerCheck가 false면 난이도 선택 확인,  true면 그림4번의 오답확인을 위해 사용.
    def __init__(self, master, selectLevel, parent, wrongAnswerCheck) :

        self.parent = parent
        self.master = master
        self.master.title("확인!")
        self.frame = Frame(self.master, background = "lightskyblue")
        self.selectLevel = selectLevel
        self.wrongAnswerCheck = wrongAnswerCheck

        if wrongAnswerCheck == False :
            if self.selectLevel.get() == 1 :
                self.lab = Label(self.frame, text = "정말 중1 난이도를 선택 하시겠습니까?", background = "lightskyblue")
                Connection.OpenWord("wordlevel1", dic, number_key)
            elif self.selectLevel.get() == 2 :
                self.lab = Label(self.frame, text = "정말 중2 난이도를 선택 하시겠습니까?", background = "lightskyblue")
                Connection.OpenWord("wordlevel2", dic, number_key)
            elif self.selectLevel.get() == 3 :
                self.lab = Label(self.frame, text = "정말 중3 난이도를 선택 하시겠습니까?", background = "lightskyblue")
                Connection.OpenWord("wordlevel3", dic, number_key)

            self.okButton = Button(self.frame, text = "OK", font = "bold", background = "deepskyblue", command = self.function_implement_window)
            self.cancelButton = Button(self.frame, text = "CALCEL", font = "bold", background = "deepskyblue", command = self.window_close) # deiconify() : 보이기

        else :
            self.lab = Label(self.frame, text = "오답 확인을 하셨습니까?")

            self.okButton = Button(self.frame, text = "YES", font = "bold", background = "deepskyblue", command = self.goto_initialiize_window)
            self.cancelButton = Button(self.frame, text = "NO", font = "bold", background = "deepskyblue", command = self.window_close)


        self.lab.place(x = 70, y = 30)
        self.okButton.place(x = 70, y = 70)
        self.cancelButton.place(x = 210, y = 70)
        self.frame.pack(expand = 1, fill = BOTH)

    def window_close(self) :
        self.master.withdraw()

        #self.master.destroy()

    def function_implement_window(self) :

        self.parent.withdraw()
        self.master.withdraw()
        self.root3 = Toplevel()
        self.root3.geometry("872x600+450+350")
        self.root3.resizable(width = FALSE, height = FALSE)

        window3 = Gui3(self.root3)

    def goto_initialiize_window(self) :

        self.parent.withdraw()
        self.master.withdraw()
        main()

class Gui3 :

    def __init__(self, master) :
        self.master = master
        self.master.title("퀴즈를 풀어봅시다~~")
        self.frame = Frame(self.master, background = "lightskyblue")
        global dic_choice

        #self.btn = []
        self.chk = IntVar()
        question = ["단어 검색", "뜻으로 단어 맞추기", "언스크램블", "단어 객관식", "틀린짝 찾기", "문장 밑줄","오답 확인"]
        command = ["find", "quiz", "unscramble", "select","sentence","sentence_line","add_word", "show_my_dic"]
        self.btn = [None for i in range(0,8)]
        self.btn[0] = Button(self.frame, text=question[0], font=("monospace", 13), command=self.find)
        self.btn[0].grid(row=0, column=0, ipadx=6, ipady=5)

        self.btn[1] = Button(self.frame, text=question[1], font=("monospace", 13), command=self.quiz)
        self.btn[1].grid(row=0, column=1, ipadx=6, ipady=5)

        self.btn[2] = Button(self.frame, text=question[2], font=("monospace", 13), command=self.unscramble)
        self.btn[2].grid(row=0, column=2, ipadx=6, ipady=5)

        self.btn[3] = Button(self.frame, text=question[3], font=("monospace", 13), command=self.select)
        self.btn[3].grid(row=0, column=3, ipadx=6, ipady=5)


        self.btn[4] = Button(self.frame, text=question[4], font=("monospace", 13), command=self.sentence)
        self.btn[4].grid(row=0, column=4, ipadx=6, ipady=5)

        if dic_choice != False:
            self.btn[5] = Button(self.frame, text=question[5], font=("monospace", 13), command=self.sentence_line)
            self.btn[5].grid(row=0, column=5, ipadx=6, ipady=5)

        # self.btn[6] = Button(self.frame, text=question[6], font=("monospace", 12), command=self.add_word)
        # self.btn[6].grid(row=0, column=6, ipadx=6, ipady=5)

        self.btn[6] = Button(self.frame, text=question[6], font=("monospace", 13), command=self.show_my_dic)
        self.btn[6].grid(row=0, column=7, ipadx=6, ipady=5)


        # for i in range(0, 8) :
        #     self.btn.append(None)
        #     self.btn[i] = Button(self.frame, text = question[i], font = "monospace")
        #     self.btn[i].grid(row = 0, column = i, padx = 6, pady = 10)
        # self.btn[9]["text"] = "오답노트" 대호형 코드
        #
        self.quizLabel = Label(self.frame, text = "문제",background = "white", height = 18, width = 80)
        self.answerText = Entry(self.frame, bd = 3, width = 80, text="정답을 입력하세요.")
        self.resultLabel = Label(self.frame, text = "결과", background = "yellow", height = 10, width = 80)
        self.wrongAnswer = Label(self.frame, text = "오답노트", background = "lightgreen", height = 35, width = 35)

        self.submitButton = Button(self.frame, text = "제출", font = "bold", command=self.click_submit) # command 추가.
        self.exitButton = Button(self.frame, text = "나가기", font = "bold", command = self.click_exit)

        self.submitButton.place(x = 10, y = 560)
        self.exitButton.place(x = 520, y = 560)
        self.quizLabel.place(x = 10, y = 50)
        self.answerText.place(x = 10, y = 350)
        self.resultLabel.place(x = 10, y = 400)
        self.wrongAnswer.place(x = 600, y = 50)
        self.frame.pack(expand = 1, fill = BOTH)

    def click_submit(self) :
        global question_check
        global dic
        global number_key
        global my_dic
        global num
        global temp

        if question_check == 0:
            word = self.answerText.get()
            if word in dic:
                self.resultLabel.configure(text=dic[word])
            else:
                self.resultLabel.configure(text="단어가 없습니다.")
        elif question_check == 1:
            word = self.answerText.get()
            if word == number_key[num]:
                self.resultLabel.configure(text="맞았습니다.")
            else:
                my_dic[number_key[num]] = dic[number_key[num]]
                self.resultLabel.configure(text="정답은 {} 입니다.".format((number_key[num])))
        elif question_check == 2:
            word = self.answerText.get()
            if word == number_key[num]:
                self.resultLabel.configure(text="맞았습니다.")
            else:
                my_dic[number_key[num]] = dic[number_key[num]]
                self.resultLabel.configure(text="정답은 "+number_key[num] + "입니다.")
        elif question_check == 3:
            word = self.answerText.get()
            if int(word) == num:
                self.resultLabel.configure(text="맞았습니다.")
            else:
                my_dic[temp[num][0]] = temp[num][1]
                self.resultLabel.configure(text="정답은 ("+str(num)+")번 "+temp[num][0]+"입니다.")
        elif question_check == 4:
            word = self.answerText.get()
            if int(word) == num:
                self.resultLabel.configure(text="맞았습니다.")
            else:
                my_dic[temp[num][0]] = temp[num][1]
                self.resultLabel.configure(text="정답은 ("+str(num)+")번 "+temp[num][0]+":"+temp[num][1]+"입니다.")
        elif question_check == 5:
            word = self.answerText.get()
            if word == temp:
                self.resultLabel.configure(text="맞았습니다.")
            else:
                my_dic[new_number_key[num]] = (new_dic[new_number_key[num]])[2]
                self.resultLabel.configure(text="정답은 "+new_number_key[num]+"입니다.")
        # elif question_check == 6:
        #     words = self.answerText.get()
        #     print(words)
        #     word = words.split(" ")[0]
        #     mean = words.split(" ")[1]
        #     print(word+","+mean)
        #
        #     if Connection.InsertWord(word, mean):
        #         self.resultLabel.configure(text="이미 있는 단어 입니다.")
        #     else:
        #         self.resultLabel.configure(text="단어를 추가 했습니다.")
        #

    def click_exit(self) :

        self.root4 = Toplevel()
        self.root4.geometry("350x200+450+350")
        self.root4.resizable(width = FALSE, height = FALSE)

        self.selectLevel = 0
        self.wrongAnswer = True

        window4 = Gui_check(self.root4, self.selectLevel, self.master, self.wrongAnswer)

    # (1)단어 검색 함수
    def find(self):
        global question_check
        num = question_check
        question_check = 0
        self.quizLabel.configure(text="찾을 단어를 입력하세요.")
        self.answerText.configure(text="")

    # (2)뜻으로 단어 맞추기
    def quiz(self):
        global question_check
        global dic
        global number_key
        global num
        question_check = 1
        num = random.randint(0,len(dic)+1)
        self.quizLabel.configure(text="뜻 : "+dic[number_key[num]])
        self.answerText.configure(text=" ")

    # (3)언스크램블
    def unscramble(self):
        mix = [];
        p = ""
        global question_check
        global dic
        global number_key
        global num

        question_check = 2
        num = random.randint(0, len(dic))
        string = number_key[num]
        for i in range(0, len(string)):
            mix.append(string[i])
        random.shuffle(mix)  # 순서 바꾸기
        for i in mix:
            p += i
        self.answerText.configure(text=" ")
        self.quizLabel.configure(text="뜻 : "+dic[number_key[num]]+"\n"+"==>문제:"+p)

    # (4)단어 객관식
    def select(self):
        global question_check
        global dic
        global number_key
        global num
        global temp

        question_check = 3
        selec = make_exam(4)
        temp = selec
        num = random.randint(1, 4)
        self.answerText.configure(text=" ")
        self.quizLabel.configure(text="뜻 : "+selec[num][1] + "\n\n" + "(1)"+selec[1][0]+"(2)"+selec[2][0]+"(3)"+selec[3][0]+"(4)"+selec[4][0])

    # (5)틀린 짝 찾기
    def sentence(self):
        global question_check
        global dic
        global number_key
        global num
        global temp

        question_check = 4
        selec = make_exam(4)
        temp = selec
        num = random.randint(1, 4)
        (selec[num])[1] = (selec[4])[1]
        self.answerText.configure(text=" ")
        self.quizLabel.configure(text="(1) "+selec[1][0]+": "+selec[1][1]+"\n"+"(2) "+selec[2][0]+": "+selec[2][1]+"\n"+"(3) "+selec[3][0]+": "+selec[3][1]+"\n"+"(4) "+selec[4][0]+": "+selec[4][1])

    # (6)문장 밑줄
    def sentence_line(self):
        global question_check
        global dic
        global number_key
        global num
        global temp
        global new_dic
        global new_number_key

        question_check = 5
        num = random.randint(1, len(new_dic))
        ans = new_number_key[num]
        wordclass = (new_dic[ans])[1]
        mean = (new_dic[ans])[2]
        synonym = (new_dic[ans])[3]
        sentence = (new_dic[ans])[4]
        self.answerText.configure(text=" ")
        if ans in sentence:
            temp = ans
            self.quizLabel.configure(text="****hint****\n품사 : "+wordclass+"\n뜻 : "+mean+"\n동의어 : "+synonym+"\n************\n"+sentence.replace(ans,"________"))

    # # (7)단어 추가
    # def add_word(self):
    #     global question_check
    #     question_check = 6
    #     self.answerText.configure(text=" ")
    #     self.quizLabel.configure(text="추가 하고 싶은 단어와 뜻을 입력하세요.")

    # (8)오답 확인
    def show_my_dic(self):
        self.answerText.configure(text="")
        total = ""
        if len(my_dic) is not 0:
            for word, mean in my_dic.items():
                text = "단어 : "+word+"  뜻 : "+mean+"\n"
                total += text
            self.wrongAnswer.configure(text=total)

        else:
            self.wrongAnswer.configure(text="저장된 단어가 없습니다.")
## 함수 선언 부분 ##

def main() :
    global question_check
    global dic
    global number_key
    global num
    global temp
    global new_dic
    global new_number_key
    global my_dic

    dic = {};
    number_key = {};
    new_dic = {};
    new_number_key = {};
    my_dic = {};
    num = 0
    temp = {};
    question_check = 0

    root = Tk()
    root.geometry("300x130+450+350")
    root.resizable(width = FALSE, height = FALSE)
    window = Gui(root)
    root.mainloop()


## 메인 코드 부분 ##

if __name__ == "__main__" :
    main()

























