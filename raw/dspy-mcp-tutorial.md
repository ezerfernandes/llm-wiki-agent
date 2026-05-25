# Tutorial: Use MCP tools in DSPy

*Source: https://dspy.ai/tutorials/mcp/*

## MCP, Standing for Model Context Protocol

"MCP, standing for Model Context Protocol, is an open protocol that standardizes how applications provide context to LLMs."

Despite development overhead, MCP allows sharing tools and resources across different technical stacks.

## Tutorial Overview

"In this guide, we will walk you through how to use MCP tools in DSPy. For demonstration purposes, we will build an airline service agent that can help users book flights and modify or cancel existing bookings."

This example relies on an MCP server with custom tools but generalizes to community-built MCP servers.

## Important Note on Execution

> "This tutorial cannot be run in hosted IPython notebooks like Google Colab or Databricks notebooks. To run the code, you will need to follow the guide to write code on your local device. The code is tested on macOS and should work the same way in Linux environments."

## Installation

```
pip install -U "dspy[mcp]"
```

## MCP Server Setup

The airline agent includes:

**Databases:**
- User database storing user information
- Flight database storing flight information
- Ticket database storing customer tickets

**Tools:**
- fetch_flight_info: retrieve flight information for specific dates
- fetch_itinerary: obtain booked itinerary information
- book_itinerary: book a flight for the user
- modify_itinerary: modify an itinerary or cancel it
- get_user_info: retrieve user information
- file_ticket: create a support ticket for human assistance

### `mcp_server.py` (full source)

```python
import random
import string

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

# Create an MCP server
mcp = FastMCP("Airline Agent")


class Date(BaseModel):
    # Somehow LLM is bad at specifying `datetime.datetime`
    year: int
    month: int
    day: int
    hour: int


class UserProfile(BaseModel):
    user_id: str
    name: str
    email: str


class Flight(BaseModel):
    flight_id: str
    date_time: Date
    origin: str
    destination: str
    duration: float
    price: float


class Itinerary(BaseModel):
    confirmation_number: str
    user_profile: UserProfile
    flight: Flight


class Ticket(BaseModel):
    user_request: str
    user_profile: UserProfile


user_database = {
    "Adam": UserProfile(user_id="1", name="Adam", email="adam@gmail.com"),
    "Bob": UserProfile(user_id="2", name="Bob", email="bob@gmail.com"),
    "Chelsie": UserProfile(user_id="3", name="Chelsie", email="chelsie@gmail.com"),
    "David": UserProfile(user_id="4", name="David", email="david@gmail.com"),
}

flight_database = {
    "DA123": Flight(
        flight_id="DA123",
        origin="SFO",
        destination="JFK",
        date_time=Date(year=2025, month=9, day=1, hour=1),
        duration=3,
        price=200,
    ),
    "DA125": Flight(
        flight_id="DA125",
        origin="SFO",
        destination="JFK",
        date_time=Date(year=2025, month=9, day=1, hour=7),
        duration=9,
        price=500,
    ),
    "DA456": Flight(
        flight_id="DA456",
        origin="SFO",
        destination="SNA",
        date_time=Date(year=2025, month=10, day=1, hour=1),
        duration=2,
        price=100,
    ),
    "DA460": Flight(
        flight_id="DA460",
        origin="SFO",
        destination="SNA",
        date_time=Date(year=2025, month=10, day=1, hour=9),
        duration=2,
        price=120,
    ),
}

itinery_database = {}
ticket_database = {}


@mcp.tool()
def fetch_flight_info(date: Date, origin: str, destination: str):
    """Fetch flight information from origin to destination on the given date"""
    flights = []

    for flight_id, flight in flight_database.items():
        if (
            flight.date_time.year == date.year
            and flight.date_time.month == date.month
            and flight.date_time.day == date.day
            and flight.origin == origin
            and flight.destination == destination
        ):
            flights.append(flight)
    return flights


@mcp.tool()
def fetch_itinerary(confirmation_number: str):
    """Fetch a booked itinerary information from database"""
    return itinery_database.get(confirmation_number)


@mcp.tool()
def pick_flight(flights: list[Flight]):
    """Pick up the best flight that matches users' request."""
    sorted_flights = sorted(
        flights,
        key=lambda x: (
            x.get("duration") if isinstance(x, dict) else x.duration,
            x.get("price") if isinstance(x, dict) else x.price,
        ),
    )
    return sorted_flights[0]


def generate_id(length=8):
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choices(chars, k=length))


@mcp.tool()
def book_itinerary(flight: Flight, user_profile: UserProfile):
    """Book a flight on behalf of the user."""
    confirmation_number = generate_id()
    while confirmation_number in itinery_database:
        confirmation_number = generate_id()
    itinery_database[confirmation_number] = Itinerary(
        confirmation_number=confirmation_number,
        user_profile=user_profile,
        flight=flight,
    )
    return confirmation_number, itinery_database[confirmation_number]


@mcp.tool()
def cancel_itinerary(confirmation_number: str, user_profile: UserProfile):
    """Cancel an itinerary on behalf of the user."""
    if confirmation_number in itinery_database:
        del itinery_database[confirmation_number]
        return
    raise ValueError("Cannot find the itinerary, please check your confirmation number.")


@mcp.tool()
def get_user_info(name: str):
    """Fetch the user profile from database with given name."""
    return user_database.get(name)


@mcp.tool()
def file_ticket(user_request: str, user_profile: UserProfile):
    """File a customer support ticket if this is something the agent cannot handle."""
    ticket_id = generate_id(length=6)
    ticket_database[ticket_id] = Ticket(
        user_request=user_request,
        user_profile=user_profile,
    )
    return ticket_id


if __name__ == "__main__":
    mcp.run()
```

## Starting the Server

Launch the MCP server with:

```
python path_to_your_working_directory/mcp_server.py
```

## Building the DSPy Agent

### Gathering Tools from MCP Servers

"We first need to gather all available tools from the MCP server and make them usable by DSPy."

"DSPy provides an API `dspy.Tool` as the standard tool interface. Let's convert all the MCP tools to `dspy.Tool`."

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=["path_to_your_working_directory/mcp_server.py"],
    env=None,
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()

            # Convert MCP tools to DSPy tools
            dspy_tools = []
            for tool in tools.tools:
                dspy_tools.append(dspy.Tool.from_mcp_tool(session, tool))

            print(len(dspy_tools))
            print(dspy_tools[0].args)

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

### Creating the Agent

"Now we will use `dspy.ReAct` to build the agent for handling customer requests."

"`ReAct` stands for 'reasoning and acting,' which asks the LLM to decide whether to call a tool or wrap up the process."

```python
import dspy

class DSPyAirlineCustomerService(dspy.Signature):
    """You are an airline customer service agent. You are given a list of tools to handle user requests. You should decide the right tool to use in order to fulfill users' requests."""

    user_request: str = dspy.InputField()
    process_result: str = dspy.OutputField(
        desc=(
            "Message that summarizes the process result, and the information users need, "
            "e.g., the confirmation_number if it's a flight booking request."
        )
    )
```

```python
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
```

### Full agent script (`dspy_mcp_agent.py`)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import dspy

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=["script_tmp/mcp_server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)


class DSPyAirlineCustomerService(dspy.Signature):
    """You are an airline customer service agent. You are given a list of tools to handle user requests.
    You should decide the right tool to use in order to fulfill users' requests."""

    user_request: str = dspy.InputField()
    process_result: str = dspy.OutputField(
        desc=(
            "Message that summarizes the process result, and the information users need, "
            "e.g., the confirmation_number if it's a flight booking request."
        )
    )


dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))


async def run(user_request):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()

            # Convert MCP tools to DSPy tools
            dspy_tools = []
            for tool in tools.tools:
                dspy_tools.append(dspy.Tool.from_mcp_tool(session, tool))

            # Create the agent
            react = dspy.ReAct(DSPyAirlineCustomerService, tools=dspy_tools)

            result = await react.acall(user_request=user_request)
            print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run("please help me book a flight from SFO to JFK on 09/01/2025, my name is Adam"))
```

Run the agent script with:

```
python path_to_your_working_directory/dspy_mcp_agent.py
```

## Sample Output

The agent produces a `Prediction` object containing the complete reasoning and acting trajectory, showing each thought, tool selection, and observation throughout the booking process.

## Conclusion

"In this guide, we built an airline service agent that utilizes a custom MCP server and the `dspy.ReAct` module. In the context of MCP support, DSPy provides a simple interface for interacting with MCP tools, giving you the flexibility to implement any functionality you need."
