import configparser
from openai import OpenAI # type: ignore

# Read the API key from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['OpenAI']['API_KEY']

client = OpenAI(
    # This is the default and can be omitted
    api_key = api_key,
)

client.models.list()

assistant = client.beta.assistants.create(
    name = "Terminal Assistant",
    instructions = "Assist me in downloading packages for arch linux.",
    tools = [{"type": "code_interpreter"}],
    model = "gpt-4o"
)

thread = client.beta.threads.create()
print(thread)

# Prompt the user for input
user_input = input("Enter your query: ")

message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = "user",
    content = "Find out what package I need to download from my goal: {user_input}"
)

print(message)

run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
)

run = client.beta.threads.runs.retrieve(
    thread_id = thread.id,
    run_id = run.id
)

messages = client.beta.threads.messages.list(
    thread_id = thread.id
)

# get oldest messages first
for message in reversed(messages.data):
    print(message.role + ": " + message.content[0].text.value)