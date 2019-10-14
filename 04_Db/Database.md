# Database(DB)

## 1. Intro

> 데이터베이스는 체계화된 데이터의 모임이다.
>
> 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합이다.
>
> 논리적으로 연관된 하나 이상의 자료의 모음으로 그 내용을 고도로 구조화함으로써 검색과 갱신의 효율화를 꾀한 것이다.
>
> 즉, 몇 개의 **자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료의 구조화하여 기억시켜 놓은 자료의 집합체**라고 할 수 있다.



### 1.1. Components of Database

개체(entity)와 그들이 가지는 속성(attribute), 그리고 개체 사이의 관계(relation)



### 1.2. RDBMS(Relation Database Management System)

> 관계형 데이터 베이스 관리 시스템는 개체와 개체 사이의 관계를 표현하기 위하여 2차원의 표(table)를 사용



- 모든 데이터를 2차원으로 표현
- 데이블은 row(record, tuple)와 column(field, item)으로 구성
- 데이블은 상호 연관성을 가지고 하나의 DB에 여러 개 존재 가능
- 데이터베이스의 설계도를 ER(Entity Relationship) 모델이라고 하고 ER모델에 따라 DB가 만들어짐



### 1.3. Basic Terminology

#### 1.3.1. Scheme(스키마)

> 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조
>
> 데이터베이스의 구조와 제약조건(자료의 구조, 표현 방법, 관계)에 관련한 전반적인 명세를 기술한 것

#### 1.3.2. Table(테이블)

> 열(column / field)과 행(record / value)의 모델을 사용해 조직된 데이터 요소들의 집합.
>
> SQL 데이터베이스에서는 테이블을 '관계' 라고도 한다.

#### 1.3.2. Column(컬럼)

> 각 열에는 고유한 데이터 형식이 지정된다.
>
> INTEGER TEXT NULL ...

#### 1.3.3. Row(레코드)

> 테이블의 데이터는 행에 저장된다.

#### 1.3.4. PK(기본키)

> 각 행의 고유값으로 Primary Key로 불린다.
>
> 반드시 설정해야하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용된다.



### 1.4. SQL



![image](https://user-images.githubusercontent.com/12672315/66534012-e1845280-eb4f-11e9-91d0-8ee362d39e57.png)

![sql](https://user-images.githubusercontent.com/12672315/66725443-06890600-ee6d-11e9-851d-8329002abbad.png)



SQL 특징

; 까지 하나의 명령으로 간주

.은 sqlite3 프로그램 기능 실행

-.schema 테이블이름 -> ;를 붙이지 않음

테이블은 여러 개 존재 가능

소문자로 표현해도 됨. 단, 대문자를 강력하게 권장함







```
$ sqlite3       // sqlite3 진입
sqlite> .exit   // 종료
sqlite> ^Z      // Ctrl + Z -> 엔터
```



sqlite3를 이용한 Database 생성

```
$ sqlite3 tutorial.sqlite3

sqlite> .databases
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqplite> SELECT * FROM examples;

1, "길동", "홍", 600, "충청도", 010-2424-1232
```



보기 좋게 출력하기

```
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM examples;

id          first_name  last_name   age         country     phone
----------  ----------  ----------  ----------  ----------  -------------
1           길동          홍           600         충청도         010-2424-1232
```



테이블 생성

```
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> 
```



테이블 목록 조회

```
sqlite> .tables

classmates  examples
```



특정 테이블 스키마 조회

```
sqlite> .schema classmates

CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);
```



특정 테이블 삭제하기

```
sqlite> DROP TABLE classmates;
sqlite> .tables

examples
```



데이터 추가 - 특정 table에 새로운 행을 추가하여 데이터를 추가할 수 있음

```sqlite
INSERT INTO classmates(name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;

name        age         address
----------  ----------  ----------
홍길동         23

INSERT INTO classmates(name, age, address) VALUES ('홍길동', 30, '서울');
SELECT * FROM classmates;

name        age         address
----------  ----------  ----------
홍길동         23
홍길동         30          서울
```



PRIMARY KEY를 따로 지정하지 않으면 pk값으로 하는 `rowid` 가 자동으로 지정된다.

```sqlite
SELECT rowid, * FROM classmates;

rowid       name        age         address
----------  ----------  ----------  ----------
1           홍길동         23
2           홍길동         30          서울
```



공백을 허용하지 않는 column 속성을 지정

```sqlite
sqlite> CREATE TABLE classmates(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
   
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

Error: NOT NULL constraint failed: classmates.address
```



`rowid`는 원래 자동으로 작성되었는데 pk컬럼을 직접 작성한 이후로는 직접 id를 적어줘야한다.

```sqlite
INSERT INTO classmates VALUES('홍길동', 30, '서울');

Error: table classmates has 4 columns but 3 values were supplied
```



특정 컬럼을 몇 개를 출력할지 선택

```sqlite
SELECT rowid, name FROM classmates LIMIT 1;

rowid       name
----------  ----------
1           홍길동
```



특정한 `rowid`를 출력

```sqlite
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

rowid       name
----------  ----------
3           박나래
```



특정한 address로 조회

```sqlite
SELECT rowid, name FROM classmates WHERE address='서울';

rowid       name
----------  ----------
1           홍길동

SELECT rowid, name, address FROM classmates WHERE address='서울';

rowid       name        address
----------  ----------  ----------
1           홍길동         서울
```



테이블에서 특정 컬럼 값을 중복없이 가져오기

```sqlite
SELECT DISTINCT age FROM classmates;

age
----------
30
23
33
```



중복이 불가능한 값인 `rowid`를 기준으로 삭제

```sqlite
DELETE FROM classmates WHERE rowid=4;
```



특정한 `rowid` 의 테이블 값 바꾸기

```
sqlite> UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;
sqlite> SELECT * FROM classmates;

name        age         address
----------  ----------  ----------
홍길동         30          서울
김철수         23          대전
박나래         23          광주
홍길동         45          제주도
```



Q. users에서 age가 30 이상인 사람만 가져온다면?

```sqlite
SELECT * FROM users WHERE age>=30;
```



Q. users에서 age가 30 이상인 사람의 이름만 가져온다면?

```sqlite
SELECT last_name, first_name FROM users WHERE age>=30;
```



Q. users에서 age가 30 이상이고 성이 김인 사람의 성과 나이만 가져온다면?

```sqlite
SELECT last_name, age FROM users WHERE age>=30 and last_name='김';
```



Q. users에서 테이블의 레코드 총 개수는?

```sqlite
SELECT COUNT(*) FROM users;
```



Q. users에서 30살 이상인 사람들의 평균나이는?

```sqlite
SELECT AVG(age) FROM users WHERE age>=30;
```



Q. users에서 계좌에 가장 많은 금액을 가지고 있는 사람의 이름과 잔액은?

``` sqlite
SELECT first_name, MAX(balance) FROM users;
```



Q. users에서 나이가 30 이상인 사람의 계좌에 들어있는 평균 잔액은?

```sqlite
SELECT AVG(balance) FROM users WHERE age>=30;
```



와일드 카드 2가지 패턴

`-` 반드시 이자리에 <u>한 개</u>의 문자가 존재해야 한다.

`%` 이자리에 있을 수도 없을 수도 있다.



Q. users에서 20대인 사람은?

```sqlite
SELECT * FROM users WHERE age LIKE '2_';
```



Q. users에서 지역번호가 02인 사람은?

```sqlite
SELECT * FROM users WHERE phone LIKE '02-%';
```



Q. users에서 이름이 '준'으로 끝나는 사람은?

```sqlite
SELECT * FROM users WHERE phone LIKE '%준';
```



Q. users에서 중간 번호가 5114 인 사람은?

```sqlite
SELECT * FROM users WHERE phone LIKE '%-5114-%';
```



Q. users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑으면?

```sqlite
SELECT * FROM users ORDER BY age ASC LIMIT 10; // DEFAULT
```



Q. users에서 나이순으로 내림차순 정렬하여 상위 10개만 뽑으면?

```sqlite
SELECT * FROM users ORDER BY age DESC LIMIT 10;
```



Q. users에서 나이순, 성 순으로 오름차순 정렬하여 상위 10개만 뽑으면?

```sqlite
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
```



Q. users에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개만 뽑으면?

```sqlite
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
```



테이블명 변경 `ALTER TABLE exist_table RENAME TO new_table;`



users에서 article이라는 테이블을 news라는 테이블로 이름 변경

```sqlite
ALTER TABLE articles RENAME TO news;
```



