# Tutorial 5

- _Date Created_: 12 July 2024
- _Last Modification Date_: 12 July 2024
- _Hosted Tutorial 5 URL_: <https://csci-5709-advanced-web-services.onrender.com>
- _Gitlab Tutorial URL_: <https://git.cs.dal.ca/msrahman/csci-5709-tutorials>
- _Gitlab Tutorial 5 URL_: <https://git.cs.dal.ca/msrahman/csci-5709-tutorials/-/tree/main/Tutorial5>

## Authors

- Md Samshad Rahman (samshad@dal.ca)

## Deployment

I uploaded the codes in a private repository on GitHub for tutorial 5 deployment and pushed my code to it. Then, I imported the tutorial 5 codes from GitHub into [Render.com](https://dashboard.render.com/) and configured the build settings to deploy the app using Dockerfile.
Finally, it was deployed and is available with the provided link.
The API allows users to perform CRUD (except delete as it was not specified for this tutorial) operations on a list of users stored in a JSON file (`DB.json`).

## Built With

- **Python 3.12**: Programming language used to build the application.
- **Flask**: Web framework used to build the RESTful API.
- **Docker**: Containerization tool used to package the application and its dependencies.
- **Render**: Cloud platform used to host the application.
- **Git**: Version control system used to manage the source code.
- **GitHub**: Web-based Git repository hosting service used to store the source code.
- **Postman**: API development environment used to test the API endpoints.

## Features

- **Health Check Endpoint**: Check the health status of the application.
- **Get All Users**: Retrieve a list of all users.
- **Add User**: Add a new user to the list.
- **Update User**: Update an existing user's details.
- **Get User by ID**: Retrieve a specific user by their ID.

## API Endpoints

### Health Check

**GET** `/health`

Checks the health status of the application.

**Response:**
```json
{
    "message": "Healthy",
    "success": true
}
```

### Get All Users

**GET** `/users`

Retrieves a list of all users.

**Response:**
```json
{
    "message": "Users retrieved",
    "success": true,
    "users": [
        {
            "email": "abc@abc.ca",
            "firstName": "ABC",
            "id": "1"
        },
        {
            "email": "xyz@xyz.ca",
            "firstName": "XYZ",
            "id": "2"
        }
    ]
}
```

### Add User

**POST** `/add`

Adds a new user to the list.

**Request Body:**
```json
{
    "email": "newuser@test.com",
    "firstName": "NewUser"
}
```

**Response:**
```json
{
    "message": "User added",
    "success": true
}
```

### Update User

**PUT** `/update/<user_id>`

Updates the details of an existing user.

**Request Body:**
```json
{
    "email": "updateduser@test.com",
    "firstName": "UpdatedUser"
}
```

**Response:**
```json
{
    "message": "User updated",
    "success": true
}
```

### Get User by ID

**GET** `/user/<user_id>`

Retrieves a specific user by their ID.

**Response:**
```json
{
    "success": true,
    "user": {
        "id": "1",
        "email": "abc@abc.ca",
        "firstName": "ABC"
    }
}
```



