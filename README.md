# Word Game Project

## Word Game Computer Educational Theory Project
- - -
### 팀원  
* #### [jaeyun95](https://github.com/jaeyun95)     
* #### [blesk011](https://github.com/blesk011)      

### 실행 방법   
```
1. mysql을 설치 --> local에 설치하기를 원하지 않는다면 2번으로
1-1. 데이터베이스, 계정 생성 (ex. database : wordprogram, user : jh)
1-2. wordprogram.sql 실행 (table 생성 및 데이터 insert 등)
1-3. Connection.py의 connect 인자값들을 알맞게 수정
	conn = pymysql.connect(
    		host='localhost',
    		user='jh', //사용자 이름으로 수정
    		passwd="6572609", //설정한 비밀번호로 수정
    		db="wordprogram",
    		charset="utf8",
    		port=3306
	)
1-4.GUI.py을 실행

2. 외부 DB에 데이터들이 insert되어 있다고 가정
2-1. Connection.py의 connect 인자값들을 알맞게 수정
	conn = pymysql.connect(
    		host='localhost',		//ip주소
    		user='jh', 		//db에 접속할 계정
    		passwd="6572609", 	//비밀번호
    		db="wordprogram",	//db
    		charset="utf8",
    		port=3306		//port번호
	)
2.2 GUI.py를 실행
```

![WordGame1](/image/WordGame1.jpg)   
![WordGame2](/image/WOrdGame2.jpg)

 

