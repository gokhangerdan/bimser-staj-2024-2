# Moderation Model

## Minimum training data specs

- 200 message examples in **Turkish** (100 labeled as 0, 100 labeled as 1)
- 200 message examples in **English** (100 labeled as 0, 100 labeled as 1)

## Data generation prompt example:

I want to train a moderation model for turkish document q&a chat bot messages. What i want to detect is the messages contains swear words addresing the developer of the document q&a chat bot. So can you generate me some data to train such model. Data should include normal q&a messages labeled as 0, mesages including swear words labeled as 0 too and messages including swear words addresing the developer of the chatbot labeled as 1. Generate at least 100 data points as jsonl format.
