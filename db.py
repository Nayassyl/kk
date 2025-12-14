from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.ext.asyncio import async_sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///./test.db")

new_session = AsyncSession(engine, expire_on_commit=False)
class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "tasks"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(50))
    description : Mapped[str | None] = mapped_column(String(250), nullable=True)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)