# Run DEV

Asssuming you have everything correct on your setup, insert this commands in terminal to run both frontend and backend. Check /frontend/frontend_commands.md and /backend/backend_commands for more details.

## Frontend

- cd DEV/frontend
- npm start

To stop running: ^C 

## Backend

### Windows

- cd DEV/backend
- .\venv\Scripts\activate
- pip3 install -r .\requirements.txt -q
- python .\main\manage.py runserver

To stop running the server: ^C 
- deactivate

### Mac

- cd DEV/backend
- source ./venv/bin/activate
- pip3 install -r ./requirements.txt -q
- python ./main/manage.py runserver

To stop running the server: ^C 
- deactivate