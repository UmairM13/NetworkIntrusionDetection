// src/App.tsx

import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import NIDS from "./components/NIDS";
import Navbar from "./components/Navbar";
import CreateUser from "./components/CreateUser";
import Home from "./components/Home";

const App: React.FC = () => {
  const [token, setToken] = useState<string | null>(null);
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    const storedToken = localStorage.getItem("session_token");
    const storedUserId = localStorage.getItem("user_id");
    if (storedToken) setToken(storedToken);
    if (storedUserId) setUserId(storedUserId);
  }, []);

  const handleLogin = (sessionToken: string, userId: string) => {
    setToken(sessionToken);
    setUserId(userId);
    localStorage.setItem("session_token", sessionToken);
    localStorage.setItem("user_id", userId);
  };

  const handleLogout = () => {
    setToken(null);
    setUserId(null);
    localStorage.removeItem("session_token");
    localStorage.removeItem("user_id");
  };

  return (
    <Router>
      <Navbar isLoggedIn={!!token} onLogout={handleLogout} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/nids" element={<NIDS token={token as string} />} />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/create-user" element={<CreateUser />} />
      </Routes>
    </Router>
  );
};

export default App;
