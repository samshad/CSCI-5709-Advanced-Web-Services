import React from 'react';
import { Route, Routes } from 'react-router-dom';

import Login from './components/Login';
import ProfileListing from './components/ProfileListing';
import ProfileDetail from './components/ProfileDetail';

// import './App.css';

import { AuthProvider } from './contexts/AuthContext';
import PrivateRoute from './components/PrivateRoute';

const App = () => {
  return (
  <AuthProvider>
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/profiles" element={<PrivateRoute><ProfileListing /></PrivateRoute>} />
      <Route path="/profiles/:id" element={<PrivateRoute><ProfileDetail /></PrivateRoute>} />
    </Routes>
  </AuthProvider>
  );
};

export default App;
