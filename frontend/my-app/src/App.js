
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import './App.css';
import Home  from "./components/Home";
import Login from "./components/Login";
function App() {
  return (
    <Router>
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/home" element={<Home />} />
    </Routes>
  </Router>
  );
}

export default App;
