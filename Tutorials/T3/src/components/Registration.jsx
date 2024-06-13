import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/base.css'


const Registration = ({ onRegister }) => {
    const [formData, setFormData] = useState({
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: ''
    });

    const [errors, setErrors] = useState({});
    const navigate = useNavigate();

    const validateForm = () => {
        let errors = {};

        // First Name Validation (letters only)
        if (!/^[a-zA-Z\s]+$/.test(formData.firstName)) {
            errors.firstName = 'First Name must contain only letters.';
        }

        // Last Name Validation (letters only)
        if (!/^[a-zA-Z\s]+$/.test(formData.lastName)) {
            errors.lastName = 'Last Name must contain only letters.';
        }

        // Email Validation (basic check for @ and .)
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(formData.email)) {
            errors.email = 'Please enter a valid email address.';
        }

        // Password Validation (at least 1 letter, 1 number, and 1 special character)
        const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$/;
        if (!passwordPattern.test(formData.password)) {
            errors.password = 'Password must have least 1 letter, 1 number, and 1 special character.';
        }

        // Password Validation (at least 8 characters long)
        if (formData.password.length < 8) {
            errors.password = 'Password must be at least 8 characters long.';
        }

        // Confirm Password Validation (must match password)
        if (formData.password !== formData.confirmPassword) {
            errors.confirmPassword = 'Passwords do not match.';
        }

        setErrors(errors);
        return Object.keys(errors).length === 0;
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (validateForm()) {
            onRegister(formData);
            navigate('/profile');
        }
    };

    return (
        <div className="container">
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="firstName">First Name</label>
                    <input
                        type="text"
                        id="firstName"
                        name="firstName"
                        value={formData.firstName}
                        onChange={handleChange}
                        required
                    />
                    {errors.firstName && <div className="error">{errors.firstName}</div>}
                </div>
                <div className="form-group">
                    <label htmlFor="lastName">Last Name</label>
                    <input
                        type="text"
                        id="lastName"
                        name="lastName"
                        value={formData.lastName}
                        onChange={handleChange}
                        required
                    />
                    {errors.lastName && <div className="error">{errors.lastName}</div>}
                </div>
                <div className="form-group">
                    <label htmlFor="email">Email</label>
                    <input
                        type="text"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                    {errors.email && <div className="error">{errors.email}</div>}
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                    {errors.password && <div className="error">{errors.password}</div>}
                </div>
                <div className="form-group">
                    <label htmlFor="confirmPassword">Confirm Password</label>
                    <input
                        type="password"
                        id="confirmPassword"
                        name="confirmPassword"
                        value={formData.confirmPassword}
                        onChange={handleChange}
                        required
                    />
                    {errors.confirmPassword && <div className="error">{errors.confirmPassword}</div>}
                </div>
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Registration;
