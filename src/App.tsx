import { ToastContainer } from "react-toastify";
import { TodoList } from "./components/todoList";

import "react-toastify/dist/ReactToastify.css";
import "./App.css"

function App() {


  return (
    <div className="main">
      <TodoList/>
      <ToastContainer/>
    </div>
  )
}

export default App
