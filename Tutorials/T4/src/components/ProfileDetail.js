import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

const ProfileDetail = () => {
  const { id } = useParams();
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  // Fetch user details from API
  useEffect(() => {
    const fetchUser = async () => {
      const response = await fetch(`https://express-t4.onrender.com/api/users/${id}`);
      const data = await response.json();
      setUser(data);
    };
    fetchUser();
  }, [id]);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div className="profileDetailContainer">
      <button onClick={() => navigate('/profiles')}>Back</button>
      <h2>{user.name}</h2>
      <img src={user.picture} alt={user.name} />
      <p><strong>Email:</strong> {user.email}</p>
      <p><strong>Phone:</strong> {user.phone}</p>
      <p><strong>Address:</strong> {user.address}</p>
      <p><strong>Age:</strong> {user.age}</p>
      <p><strong>Eye Color:</strong> {user.eyeColor}</p>
      <p><strong>Gender:</strong> {user.gender}</p>
      <p><strong>Company:</strong> {user.company}</p>
      <p><strong>Balance:</strong> {user.balance}</p>
      <p><strong>About:</strong> {user.about}</p>
      <p><strong>Registered:</strong> {new Date(user.registered).toLocaleString()}</p>
      <p><strong>Latitude:</strong> {user.latitude}</p>
      <p><strong>Longitude:</strong> {user.longitude}</p>
      <p><strong>Favorite Fruit:</strong> {user.favoriteFruit}</p>
      <p><strong>Tags:</strong> {user.tags.join(', ')}</p>
      <p><strong>Greeting:</strong> {user.greeting}</p>
      <p><strong>Friends:</strong></p>
      <ul>
        {user.friends.map(friend => (
          <li key={friend.id}>{friend.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default ProfileDetail;
