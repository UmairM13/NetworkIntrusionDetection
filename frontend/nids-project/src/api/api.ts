// src/api/api.ts
const BASE_URL = "http://127.0.0.1:5000/api";

export const login = async (username: string, password: string) => {
  const response = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    throw new Error("Login failed");
  }

  return response.json();
};

export const predict = async (csvData: string) => {
  console.log("Sending CSV Data:", csvData); // Log the data being sent
  const response = await fetch(`${BASE_URL}/nids/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "text/plain", // Set content type to text/plain
    },
    body: csvData, // Send raw CSV data as the body
  });

  if (!response.ok) {
    throw new Error("Failed to fetch predictions");
  }

  return response.json();
};
