from motor.motor_asyncio import AsyncIOMotorClient
from app.models.task import Task
from bson import ObjectId


client = AsyncIOMotorClient("mongodb://localhost")
database = client.taskdatabase
collection = database.tasks


async def get_one_task_id(id):
    task = await collection.find_one({"_id": ObjectId(id)})
    return task


async def get_one_task_title(title):
    task = await collection.find_one({"title": title})
    return task


async def get_all_task():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks


async def create_task(task):
    del task["id"]
    task_id = await collection.insert_one(task)
    new_task = await collection.find_one({'_id': task_id.inserted_id})
    return new_task


async def update_task(id: str, newTask):
    task = {k: v for k, v in newTask.model_dump().items() if v is not None}
    await collection.update_one({"_id": ObjectId(id)}, {"$set": task})
    document = await collection.find_one({"_id": ObjectId(id)})
    return document


async def delete_task(id: str):
    await collection.delete_one({"_id": ObjectId(id)})
    return True
