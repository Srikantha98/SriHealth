import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Navbar from "./components/Navbar";
import { isAuthenticated } from "./services/auth";

function App() {
  return (
    <BrowserRouter>
      {/* Navbar visible on all pages */} 

      <Routes>
        {/* Public Home Page */}
        <Route path="/" element={<Home />} />

        {/* Auth Pages */}
        <Route path="/login" element={isAuthenticated() ? <Navigate to="/dashboard" /> : <Login />} />
        <Route path="/register" element={isAuthenticated() ? <Navigate to="/dashboard" /> : <Register />} />

        {/* Protected Dashboard */}
        <Route
          path="/dashboard"
          element={
            isAuthenticated() ? <Dashboard /> : <Navigate to="/login" replace />
          }
        />

        {/* Catch-all: redirect unknown routes */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
