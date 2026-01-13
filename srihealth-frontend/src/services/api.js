import axios from "axios";

/**
 * Centralized API configuration
 * Used for all backend communication
 */

const API = axios.create({
  baseURL: "http://localhost:5000", // Flask / FastAPI backend
});

/**
 * Automatically attach JWT token to every request
 */
API.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

/**
 * Prediction API
 * @param {FormData} formData - MRI image
 */
export const predictMRI = async (formData) => {
  const res = await API.post("/predict", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return res.data;
};

export default API;
