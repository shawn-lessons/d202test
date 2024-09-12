# Flask Server and Client for Simulating Gateway/Dashboard and Sensor

This project consists of a Flask-based server (the gateway and dashboard for managing temperature readings) that accepts POST requests to add readings (name and number) to a SQLite database, and a Python client script that simulates a sensor by periodically sending data to the server.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x

Install dependencies (flask .. etc)

`   pip install -r requirements.txt`


## Project Setup

### 1. Setting up the Flask server

#### Create the database

The Flask server uses an SQLite database. Before starting the server, create a database and the required table:

1. Open a terminal and run the following commands:

   `sqlite3 data.db < create_database.sql`
