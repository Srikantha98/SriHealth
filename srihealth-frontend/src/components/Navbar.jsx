import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");
  const user = JSON.parse(localStorage.getItem("user") || "{}");

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <nav className="flex items-center justify-between px-8 py-4 bg-white shadow-sm">
      {/* Left: Project Title */}
      <Link to="/" className="text-lg font-semibold tracking-wide">
        Alzheimer’s Disease Prediction System
      </Link>

      {/* Right: Navigation */}
      <div className="flex items-center space-x-4">
        {!token ? (
          <>
            <Link
              to="/login"
              className="px-4 py-2 rounded-xl border border-slate-300 hover:bg-slate-100"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="px-4 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800"
            >
              Register
            </Link>
          </>
        ) : (
          <>
            <span className="text-slate-600 text-sm">
              {user?.name || "User"}
            </span>
            <Link
              to="/dashboard"
              className="px-4 py-2 rounded-xl border border-slate-300 hover:bg-slate-100"
            >
              Dashboard
            </Link>
            <button
              onClick={handleLogout}
              className="px-4 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800"
            >
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  );
}
