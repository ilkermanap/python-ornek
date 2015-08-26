from flask import Flask, jsonify, request
import json

from sqlalchemy import Column,ForeignKey, Boolean, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Personel(Base):
    __tablename__ = "personel"
    tcno = Column(Integer, primary_key=True)
    adi = Column(String(30))
    soyadi = Column(String(30))

engine = create_engine('postgresql://postgres:system@localhost/deneme')
session = sessionmaker()
session.configure(bind=engine)
s = session()

app = Flask(__name__)


def db_to_json(rows):
    temp  = {}
    return rows[0]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/personel')
@app.route('/personel/<int:tcno>')
def personel(tcno = -1):
    if tcno == -1:
        liste = s.query(Personel).all()
    else:
        liste = s.query(Personel).filter(Personel.tcno == tcno).all()
    temp = {}
    for r in liste:
        temp[r.tcno] = {'adi':r.adi, 'soyadi':r.soyadi}
        
    return jsonify(temp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
