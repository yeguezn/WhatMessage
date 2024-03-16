# What is this app about?
This app offers predefined messages that you can send to your friends via Whatsapp. These messages are categorized, so you can choose all of kind of messages (Love, Motivational, Movie phrases).

# DB credentials
- username: prueba
- password: root

# Admin credentials
If you want to add more categories and messages, go to http://localhost:8000/admin and log in with the following credentials
- username: admin
- password: 1234

# Set Up
1. Clone this repository
```bash
git clone https://github.com/yeguezn/WhatMessage.git
```
2. Get into the directory
```bash
cd WhatMessage
```
3. Run the following command
```bash
docker compose up
```

4. Open a new terminal tab in the project directory and run the following command in order to import the database
```bash
docker exec -i <DB_CONTAINER_ID> psql -U prueba -d genericMessages < genericMessages.sql
```
(You can get the `DB_CONTAINER_ID` running the `docker ps command`)

5. Return to the terminal tab where you ran the `docker compose up`and press crtl + c

6. Run the `docker compose up` command again
```bash
docker compose up
```
7. Open this link http://localhost:5173

