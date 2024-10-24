import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login as apiLogin } from "../api/api"; // Import the login function
import "../css/Login.css";

const Login: React.FC<{ onLogin: (token: string, userId: string) => void }> = ({
  onLogin,
}) => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [error, setError] = useState<string>("");
  const navigate = useNavigate(); // Initialize useNavigate

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError("");

    try {
      const result = await apiLogin(username, password); // Use the imported login function
      onLogin(result.session_token, result.user_id); // Include user_id

      // Redirect to the NIDS page after login
      navigate("/nids");
    } catch (error) {
      setError((error as Error).message);
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit} className="login-form">
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit" className="login-button">
          Login
        </button>
      </form>
      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default Login;
