from server.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    upldate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    moddate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class WorkSession(Base):
    __tablename__ = 'worksessions'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    upldate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    moddate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    session_begin = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    session_end = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")
