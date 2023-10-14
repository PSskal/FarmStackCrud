

from fastapi import APIRouter, HTTPException, status
from app.db.client import get_all_task, create_task, get_one_task_title, get_one_task_id, delete_task, update_task
from app.models.task import Task, UpdateTask

router = APIRouter()


@router.get('/tasks')
async def get_tasks():
    tasks = await get_all_task()
    return tasks


@router.get('/tasks/{id}', response_model=Task)
async def get_task(id: str):
    taskfound = await get_one_task_id(id)
    if not taskfound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    return taskfound


@router.post('/tasks', response_model=Task)
async def save_tasks(task: Task):
    taskfound = await get_one_task_title(task.title)
    if not taskfound:
        response = await create_task(task.model_dump())
        if not response:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="something went wrong")
        print(response)
        return response
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Task already exists")


@router.put('/tasks/{id}', response_model=Task)
async def put_task(id: str, task: UpdateTask):
    print(task)
    response = await update_task(id, task)
    if not response:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Task already exists, nothing to update")
    return response


@router.delete('/tasks/{id}')
async def remove_task(id: str):
    response = await delete_task(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_423_LOCKED,
                            detail="Task not deleted")
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,
                        detail="Task successfully removed")
