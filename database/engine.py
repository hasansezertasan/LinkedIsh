from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker

from .config import ASQLALCHEMY_DATABASE_URL, SQLALCHEMY_DATABASE_URL, connect_args

sync_engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
    echo=False,
)
async_engine = create_async_engine(
    ASQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
    echo=False,
)
LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine,
    class_=Session,
)
AsyncLocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
