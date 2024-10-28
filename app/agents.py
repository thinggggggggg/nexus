from uagents import Agent, Context, Model
from flask import Flask
from time import sleep
from requests import post, get
import json

class Message(Model):
    message: str

class Request(Model):
    text: str

class Response(Model):
    text: str
    agent_address: str

DESTINATION_1 = "agent1q02jy3kk437pywwnjdrdqux44xksq9cg47n9gmwyu0ezegp0u5r675xkqre"  # agent 2's address (destination for agent 1)
SEED_PHRASE_1 = "ILoveSendingMessages"  # agent 1's seed phrase
AGENT_MAILBOX_KEY_1 = "4f598b12-d856-4f59-ae72-b7409396960f"  # agent 1's mailbox key

DESTINATION_2 = "agent1qd4mdj8rv6zkhf9zu2uhzct95egmzv60tx0q05kgw003983a40585sdttjp"  # agent 1's address (destination for agent 2)
SEED_PHRASE_2 = "ILoveSendingMessagesToo"  # agent 2's seed phrase
AGENT_MAILBOX_KEY_2 = "3fc55f41-1f70-4bbf-ad06-bf7bb5b2ee5f"  # agent 2's mailbox key

user_choice = ''
while user_choice != 1 and user_choice != 2:
    input('Enter agent to use (1 or 2): ')
if user_choice.strip() == '1':
    DESTINATION = DESTINATION_1
    SEED_PHRASE = SEED_PHRASE_1
    AGENT_MAILBOX_KEY = AGENT_MAILBOX_KEY_1
else:
    DESTINATION = DESTINATION_2
    SEED_PHRASE = SEED_PHRASE_2
    AGENT_MAILBOX_KEY = AGENT_MAILBOX_KEY_2

agent = Agent(
    name="user1",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

received_messages = []

@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    received_messages.append(msg.message)  # Store the incoming message

@agent.on_rest_post("/rest/post", Request, Response)
async def handle_post(ctx: Context, req: Request) -> Response:
    ctx.logger.info("Received POST request")
    await ctx.send(DESTINATION, Message(message=req.text))
    return Response(text="Message sent", agent_address=DESTINATION)

# Endpoint to retrieve messages
@agent.on_rest_get("/rest/get_messages", Response)
async def get_messages(ctx: Context):
    # Return the list of received messages as a JSON response
    print(received_messages)
    return json.dumps(str(received_messages))

if __name__ == "__main__":
    agent.run()