import { Link } from "react-router-dom";
export default function Navbar() {
  return (
    <header className="flex justify-between items-center my-7">
      <Link to="/">
        <h1 className="text-3xl font-bold">Navbar</h1>
      </Link>
      <Link
        to="/task/new"
        className="bg-zinc-950 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded-sm "
      >
        create task
      </Link>
    </header>
  );
}
