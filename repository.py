from db import new_session, TaskOrm
from schemas import STaskAdd, STask
from sqlalchemy.future import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task) 
            await session.flush() 
            await session.commit()
            return task.id
    @classmethod
    async def find_all(cls):
        async with new_session as session:
            result = await session.execute(select(TaskOrm))
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task) for task in task_models]
            return task_schemas
    
    