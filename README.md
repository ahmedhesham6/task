# Thndr Programming Assignment

## Usage

```bash
docker-compose up
```
Then go to the local development url

```
http://localhost:8000/
```

## Components

The System is divided to three services, one datastore

### 1. Streamer

Streaming realtime stock prices

### 2. Subscriber

Subscribing to the queue and listening to the new stock prices and populating it in the datastore

### 3. Portfolio

- Deposit/Withdraw money into/from user account
- Buy/Sell stocks for user
- Stock details
- User Portfolio details


## Concept

In an Event sourcing manner, each event is recorded whether its

- Deposit/Withdraw money
- Stock new Price & Availability
- Buy/Sell stocks
 
And then a database view is created to accumulate this events in order to get

- User's Balance
- Stock Price
- User Stock Portfolio

This Approach is taken from my side for two reasons

1. Reducing the application logic
2. Recording all the events to have the ability to rollback at anytime


