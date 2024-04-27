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
    git clone https://github.com/yeguezn/WhatMessage.git && cd WhatMessage
    ```

2. Run the following command
    
    ## Linux
    ```bash
    sudo docker compose up -d
    ```

    ## Windows
    ```bash
    docker compose up -d
    ```

3. Copy the genericMessages.sql file to your Docker container
    
    ## Linux
    ```bash
    sudo docker cp genericMessages.sql db-container:/docker-entrypoint-initdb.d/
    ```
    
    ## Windows
    ```bash
    docker cp genericMessages.sql db-container:/docker-entrypoint-initdb.d/
    ```

4. Open this link http://localhost:5173

