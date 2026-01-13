import API from "./api";

/**
 * Register a new user
 * @param {Object} data - { name, email, password }
 */
export const registerUser = async (data) => {
  const res = await API.post("/register", data);
  return res.data;
};

/**
 * Login user
 * @param {Object} data - { email, password }
 */
export const loginUser = async (data) => {
  const res = await API.post("/login", data);
  return res.data;
};

/**
 * Logout user (client-side)
 */
export const logoutUser = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("user");
};

/**
 * Check authentication status
 */
export const isAuthenticated = () => {
  return !!localStorage.getItem("token");
};
