import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./pages/Homepage";
import TaskForm from "./pages/TaskForm";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <main className="container mx-auto px-10">
        <Navbar />
        <Routes>
          <Route path="/" element={<Homepage />} />h
          <Route path="/task/new" element={<TaskForm />} />
          <Route path="/task/:id" element={<TaskForm />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;
