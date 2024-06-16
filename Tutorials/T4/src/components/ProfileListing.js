import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import { useAuth } from '../contexts/AuthContext'; // Import the useAuth hook from the AuthContext

function ProfileListing() {
  const [users, setUsers] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const { logout } = useAuth(); // Import the logout function from the AuthContext

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await fetch('https://express-t4.onrender.com/api/users');
      if (response.ok) {
        const data = await response.json();
        setUsers(data);
      } else {
        console.error('Failed to fetch users');
      }
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  // Handle search input change
  const handleSearchChange = event => {
    setSearchQuery(event.target.value);
  };

  // Filter users based on search query
  const filteredUsers = users.filter(user =>
    user.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <div className='profileListContainer'>
      <button onClick={handleLogout}>Logout</button>
      <h1>Profile Listing</h1>
      <input
        type="text"
        placeholder="Search by Name"
        value={searchQuery}
        onChange={handleSearchChange}
        className='searchBox'
      />
      <div className="profileList">
        {filteredUsers.map(user => (
          <div key={user._id} className="user-item" onClick={() => navigate(`/profiles/${user._id}`)}>
            <img src={user.picture} alt={user.name} />
            <p>{user.name}</p>
            <p>{user.email}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProfileListing;
