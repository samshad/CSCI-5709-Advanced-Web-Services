from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from faker import Faker
from load_dotenv import load_dotenv
import os
from time import sleep

load_dotenv()
fake = Faker()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)

db = client['Tutorial6']
collection = db['users']

"""
Schema for 'users' collection
{
    "name": name,
    "email": email,
    "address": address,
    "phone": phone
}
"""


def health_check():
    """Check the health of the database."""
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        server_info = client.server_info()
        print(server_info)
    except Exception as e:
        print(e)


def create_user(user):
    """Create a new user."""
    result = collection.insert_one(user)
    print(f"User created with ID: {result.inserted_id}")


def read_users():
    """Read all users."""
    users = collection.find()
    for user in users:
        print(user)


def read_user(user_id):
    """Read a single user by ID."""
    user = collection.find_one({"_id": ObjectId(user_id)})
    print(user)


def update_user(user_id, update_fields):
    """Update a user by ID."""
    result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_fields})
    print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s)")


def delete_user(user_id):
    """Delete a user by ID."""
    result = collection.delete_one({"_id": ObjectId(user_id)})
    print(f"Deleted {result.deleted_count} document(s)")


if __name__ == "__main__":
    # health_check()

    # name = fake.name()
    # email = fake.email()
    # address = fake.address()
    # phone = fake.phone_number()

    # for _ in range(15):
    #     new_user = {
    #         "name": fake.name(),
    #         "email": fake.email(),
    #         "address": fake.address(),
    #         "phone": fake.phone_number()
    #     }
    #     create_user(new_user)
    #     sleep(2)

    # new_user = {
    #     "name": fake.name(),
    #     "email": fake.email(),
    #     "address": fake.address(),
    #     "phone": fake.phone_number()
    # }
    # create_user(new_user)

    # Read all users
    # print("Reading all users:")
    # read_users()

    # Read a single user by ID

    # user_id = "6695c4e2f6737865cdc660b6"
    # print(f"Reading user with ID {user_id}:")
    # read_user(user_id)

    user_id = "6695c4e2f6737865cdc660b6"

    # Update a user by ID
    update_fields = {"email": "test.testing@example.com"}
    print(f"Updating user with ID {user_id}:")
    update_user(user_id, update_fields)
    print(f"Reading user with ID {user_id}:")
    read_user(user_id)

    # Delete a user by ID
    # print(f"Deleting user with ID {user_id}:")
    # delete_user(user_id)

