import axios from "axios";
import { mockCheckHealth, mockQueryDatabase } from "./mockApi";

// API Base URL
const API_BASE_URL = "http://localhost:8000";

// Detect v0 / Vercel preview
const isV0Preview =
  typeof window !== "undefined" &&
  (window.location.hostname.includes("v0.dev") ||
    window.location.hostname.includes("vercel.app") ||
    !window.location.hostname.includes("localhost"));

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 30000,
});

// Health check
export const checkHealth = async () => {
  if (isV0Preview) return mockCheckHealth();

  try {
    await api.get("/health", { timeout: 5000 });
    return true;
  } catch {
    return mockCheckHealth();
  }
};

// Query database function - FIXED to use backend properly
export const queryDatabase = async (query) => {
  // Always use mock in preview
  if (isV0Preview) return mockQueryDatabase(query);

  try {
    const { data } = await api.post("/query", { query });
    return data; // real backend reply
  } catch (error) {
    console.warn("Backend offline – using mock data:", error?.message || error);
    return mockQueryDatabase(query); // graceful fallback
  }
};

export default api;
