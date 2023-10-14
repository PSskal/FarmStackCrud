import React from "react";
import { useNavigate } from "react-router-dom";

function TaskList({ task }) {
  if (!task) {
    return null; // O muestra un mensaje de error adecuado
  }
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-950 p-4 hover:cursor-pointer hover:bg-gray-950"
      onClick={() => {
        navigate(`/task/${task._id}`);
      }}
    >
      <h2>{task.title}</h2>
      <p>{task.description}</p>
    </div>
  );
}

export default TaskList;
