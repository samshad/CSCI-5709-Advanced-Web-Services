import React from 'react';
import '../styles/base.css'


const Profile = ({ user }) => {
    return (
        <div className="container">
            <h2>Profile</h2>
            <p><strong>First Name:</strong> {user.firstName}</p>
            <p><strong>Last Name:</strong> {user.lastName}</p>
            <p><strong>Email:</strong> {user.email}</p>
        </div>
    );
};

export default Profile;
