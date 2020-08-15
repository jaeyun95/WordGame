import pymysql

conn = pymysql.connect(
    host='localhost',
    user='jh',
    passwd="6572609",
    db="wordprogram",
    charset="utf8",
    port=3306
)


#wordDB를 여는 함수--> 중1~3단어, 사자성어 여는 부분
def OpenWord(tablename,dic,number_key):
    cur = conn.cursor()
    sql = "select * from "+tablename
    cur.execute(sql)
    result = cur.fetchall()
    i=0
    for word,mean in result:
        if "\ufeff" in word:
            word = word.replace("\ufeff","")
        dic[word] = mean
        number_key[i] = word
        i += 1
    cur.close()


#영어 문장 테스트를 위한 DB열기
def OpenSentence(tablename,dic,number_key):
    cur = conn.cursor()
    sql = "select * from "+tablename
    cur.execute(sql)
    result = cur.fetchall()
    i=0
    for correctanswer,wordclass,mean,synonym,sentence in result:
        dic[correctanswer] = (correctanswer,wordclass,mean,synonym,sentence)
        number_key[i] = correctanswer
        i += 1
    cur.close()

#새로운 단어 추가를 위한 DB연결
def InsertWord(word,mean):
    data = (word, mean)
    cur = conn.cursor()
    sql1 = "select * from word where Word=%s"
    cur.execute(sql1,word)
    if cur.fetchone() is not None:
        return False
    else:
        sql2 = "insert into word(Word,Mean) value(%s, %s)"
        cur.execute(sql2, data)
        conn.commit()
        return True
    cur.close()