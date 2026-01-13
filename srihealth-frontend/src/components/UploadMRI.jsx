import { useState } from "react";
import axios from "axios";

export default function UploadMRI({ setResult }) {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    setFile(selectedFile);
    setError("");

    // Create preview URL
    const reader = new FileReader();
    reader.onloadend = () => setPreview(reader.result);
    reader.readAsDataURL(selectedFile);
  };

  const handleSubmit = async () => {
    if (!file) {
      setError("Please select an MRI image");
      return;
    }

    const token = localStorage.getItem("token");
    if (!token) {
      setError("Authentication required. Please login again.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    try {
      const res = await axios.post("http://localhost:5000/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${token}`,
        },
      });

      setResult(res.data);
      setError(""); // Clear previous errors
    } catch (err) {
      console.error(err); // Log for debugging
      setError(
        err.response?.data?.message || "Prediction failed. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-4 max-w-md mx-auto">
      {preview && (
        <img
          src={preview}
          alt="MRI Preview"
          className="w-full h-auto rounded-xl border border-slate-300"
        />
      )}

      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="block w-full text-sm text-slate-600
                   file:mr-4 file:py-2 file:px-4
                   file:rounded-xl file:border-0
                   file:text-sm file:font-semibold
                   file:bg-slate-100 file:text-slate-700
                   hover:file:bg-slate-200"
      />

      {error && <p className="text-red-600 text-sm">{error}</p>}

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="w-full py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800 transition"
      >
        {loading ? "Analyzing MRI..." : "Predict Alzheimer’s Stage"}
      </button>
    </div>
  );
}
