# Create the virtual environment
python -m venv env

#Activate the environemnt
source env/bin/activate

# Install fastapi and unicorn
pip install fastapi uvicorn python-multipart requests python-dotenv psycopg2 peewee python-jose[cryptography] pydantic[email] passlib[bcrypt] pytest

# Run the API
uvicorn main:app --reload

