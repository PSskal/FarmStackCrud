import { useState, useEffect } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

export default function TaskForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const params = useParams();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log(params);
      if (params.id) {
        const res = await axios.put(
          `http://localhost:8000/tasks/${params.id}`,
          {
            title,
            description,
          }
        );
        console.log(res);
      } else {
        await axios.post("http://localhost:8000/tasks", {
          title,
          description,
        });
      }
      navigate("/");
    } catch (error) {
      console.log("hubo un error");
    }
    e.target.reset();
  };

  useEffect(() => {
    if (params.id) {
      fetchTasks();
    }
    async function fetchTasks() {
      const res = await axios.get(`http://localhost:8000/tasks/${params.id}`);
      const data = res.data;
      setTitle(data.title);
      setDescription(data.description);
    }
  }, [params.id]);

  return (
    <div className="flex items-center justify-center h-[calc(100vh-5rem)]">
      <div className="bg-zinc-950 p-7 flex-auto">
        <form className="" onSubmit={handleSubmit}>
          <h1 className="font-bold text-lg my-4">
            {!params.id ? "Create task" : "Update task"}
          </h1>
          <input
            type="text"
            placeholder="title"
            className="block py-2 px-3 mb-4 w-full text-black"
            onChange={(event) => setTitle(event.target.value)}
            value={title}
            autoFocus
          />
          <textarea
            placeholder="description"
            rows={10}
            className="block py-2 px-3 mb-4 w-full text-black"
            onChange={(event) => setDescription(event.target.value)}
            value={description}
          ></textarea>
          {<button>{params.id ? "update task" : "create task"}</button>}
        </form>
        {params.id && (
          <button
            className="bg-red-500"
            onClick={async () => {
              const res = await axios.delete(
                `http://localhost:8000/tasks/${params.id}`
              );
              console.log(res);
              navigate("/");
            }}
          >
            delete
          </button>
        )}
      </div>
    </div>
  );
}
