import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import UploadMRI from "../components/UploadMRI";
import ResultCard from "../components/ResultCard";

export default function Dashboard() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [result, setResult] = useState(null);

  // Effect to check authentication and redirect if no token
  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      // Defer navigation to avoid synchronous state updates
      setTimeout(() => navigate("/login", { replace: true }), 0);
    }
  }, [navigate]);

  // Effect to load user from localStorage if token exists
  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      try {
        // Defer setState to avoid synchronous state update warning
        setTimeout(() => setUser(JSON.parse(storedUser)), 0);
      } catch (err) {
        console.error("Failed to parse user from localStorage:", err);
        localStorage.removeItem("user");
      }
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login", { replace: true });
  };

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Header */}
      <header className="flex items-center justify-between px-8 py-5 bg-white shadow-sm">
        <h1 className="text-xl font-semibold">
          Alzheimer’s Disease Prediction Dashboard
        </h1>
        <button
          onClick={handleLogout}
          className="px-4 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800"
        >
          Logout
        </button>
      </header>

      {/* Main Content */}
      <main className="px-10 py-10">
        {/* Welcome Section */}
        <div className="mb-10">
          <h2 className="text-2xl font-semibold">
            Welcome{user?.name ? `, ${user.name}` : ""}
          </h2>
          <p className="text-slate-600 mt-2">
            Upload an MRI image to predict the stage of Alzheimer’s disease
            using the trained GAN-augmented deep learning model.
          </p>
        </div>

        {/* Prediction Section */}
        <div className="grid md:grid-cols-2 gap-10">
          <div className="bg-white p-8 rounded-2xl shadow">
            <h3 className="text-xl font-semibold mb-4">MRI Image Upload</h3>
            <UploadMRI setResult={setResult} />
          </div>

          <div className="bg-white p-8 rounded-2xl shadow">
            <h3 className="text-xl font-semibold mb-4">Prediction Result</h3>
            <ResultCard result={result} />
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="text-center py-6 text-slate-500 text-sm">
        Secure Medical Decision Support System • M.Tech CSE Project
      </footer>
    </div>
  );
}
