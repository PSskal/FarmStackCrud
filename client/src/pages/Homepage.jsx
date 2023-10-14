import axios from "axios";
import { useState } from "react";
import { useEffect } from "react";
import TaskList from "../components/TaskList";

export default function Homepage() {
  const [tasks, SetTasks] = useState([]);
  useEffect(() => {
    async function fetchTasks() {
      const res = await axios.get("http://127.0.0.1:8000/tasks");
      SetTasks(res.data);
      console.log(res.data);
    }
    fetchTasks();
  }, []);

  return (
    <>
      <div className="grid grid-cols-3 gap-4">
        {tasks.map((task) => (
          <TaskList task={task} key={task._id} />
        ))}
      </div>
    </>
  );
}
