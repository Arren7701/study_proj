import uuid
from datetime import datetime


from internal.extension import db
from sqlalchemy import PrimaryKeyConstraint, Index, Column, Text, DateTime, UUID, String


class App(db.Model):
    """AI 应用的基础模型类"""
    __tablename__ = 'app'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_app_id'),##主键的约束。
        Index('idx_app_account_id','account_id',unique=True),

    )

    id =            Column(UUID, default=uuid.uuid4, primary_key=True)
    account_id =    Column(UUID, nullable=False)
    name =          Column(String(255), default = "", nullable=False)
    icon =          Column(String(255), default= "", nullable=False)
    description =   Column(Text, default= "", nullable=False)
    status =        Column(String(255), default= "", nullable=False)
    updated_at =    Column(DateTime, default=datetime.now,onupdate=datetime.now,nullable=False)
    created_at =    Column(DateTime, default=datetime.now, nullable=False)






