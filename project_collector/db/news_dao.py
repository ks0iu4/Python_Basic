# DAO: Database Access Object
#  - 데이터 작업(CRUD)을 하는 객체

# 예시)
#  회원 => member_dao
#  로그인 => login_dao
#  뉴스 => news_dao
#  상품 => product_dao

from db.common.connection import conn_mongodb

# 뉴스(제목, 본문, 날짜, URL) 저장
def add_news(data):
    # 1.Connection
    #  pymongo를 사용해서 -> Python - MongoDB
    #                     (IP, PORT, ID, PW)
    # 2.SQL(명령)을 통해서 CRUD 작업 진행
    # 3.결과 확인
    conn = conn_mongodb()  # 1.connection
    conn.insert_one(data)  # 2.DB에 저장