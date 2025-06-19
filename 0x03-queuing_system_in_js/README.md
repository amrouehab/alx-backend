# 0x03. Queuing System in JS

This project explores queuing systems using Node.js, Redis, and Kue. It covers basic Redis client operations, publish/subscribe patterns, and job queue management with Kue.

## Requirements

-   Ubuntu 18.04
-   Node.js 12.x
-   Redis 5.0.7 or higher

## Setup

1.  **Install Dependencies:**
    ```bash
    npm install
    ```

2.  **Install and Run Redis:**
    Follow the instructions in Task 0 to download, compile, and run a Redis server.
    
    ```bash
    wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    tar xzf redis-6.0.10.tar.gz
    cd redis-6.0.10
    make
    src/redis-server &
    ```

3.  **Verify Redis:**
    Ensure the server is running by pinging it.
    ```bash
    cd redis-6.0.10
    src/redis-cli ping
    # Expected output: PONG
    ```

4.  **Create `dump.rdb` (Task 0):**
    The `dump.rdb` file is a snapshot of your Redis database. To generate it as required by the task:
    -   Connect to your Redis instance using `redis-cli`.
    -   Set the key `ALX` with the value `School`: `set ALX School`.
    -   Shut down the Redis server gracefully (e.g., `src/redis-cli shutdown` or `kill [PID]`). This will cause Redis to save its data to `dump.rdb`.
    -   Copy the generated `dump.rdb` file from your Redis directory to the root of this project.

## Running the Scripts

Use the provided npm scripts to run each exercise file. For example, to run the first task:

```bash
npm run dev 0-redis_client.js
