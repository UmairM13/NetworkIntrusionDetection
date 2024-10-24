import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "../css/Navbar.css";

interface NavbarProps {
  isLoggedIn: boolean;
  onLogout: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ isLoggedIn, onLogout }) => {
  const navigate = useNavigate(); // Use useNavigate hook for navigation

  const handleLogout = () => {
    onLogout(); // Call the logout function
    navigate("/"); // Navigate to the home page after logout
  };

  return (
    <nav className="navbar">
      <Link to="/">
        <h1>NIDS App</h1>
      </Link>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        {isLoggedIn ? (
          <>
            <li>
              <Link to="/nids">NIDS</Link>
            </li>
            <li>
              <button onClick={handleLogout}>Logout</button>
            </li>
            <li>
              <Link to="/create-user">Create User</Link>{" "}
              {/* Link to Create User page */}
            </li>
          </>
        ) : (
          <li>
            <Link to="/login">Login</Link>
          </li>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
