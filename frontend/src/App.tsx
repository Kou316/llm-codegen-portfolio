import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./components/Home";
import CodeGeneration from './components/CodeGeneration'

const App = () => {
  return (
    <BrowserRouter>
  <div
    style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "flex-start",
      minHeight: "100vh",
      fontFamily: "sans-serif",
      paddingTop: "2rem"
    }}
  >
    <h1 style={{ paddingLeft: "28rem",marginBottom: "1rem" }}>試作品</h1>

    <nav style={{ paddingLeft: "30rem", marginTop: "2rem", marginBottom: "2rem" }}>
      <Link to="/" style={{ marginRight: "1rem" }}>Home</Link>
      <Link to="/code-generation" style={{ marginRight: "1rem" }}>コード生成</Link>
    </nav>

    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/code-generation" element={<CodeGeneration />} />
    </Routes>
  </div>
</BrowserRouter>

  );
};

export default App;
