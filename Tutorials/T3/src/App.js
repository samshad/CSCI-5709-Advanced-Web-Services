import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Registration from './components/Registration';
import Profile from './components/Profile';

function App() {
  const [user, setUser] = useState(null);

  const handleRegistration = (userData) => {
    setUser(userData);
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={user ? <Navigate to="/profile" /> : <Registration onRegister={handleRegistration} />} />
        <Route path="/profile" element={user ? <Profile user={user} /> : <Navigate to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;
