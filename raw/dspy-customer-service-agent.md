# Building AI Agents with DSPy — Customer Service Agent Tutorial

**Source:** https://dspy.ai/tutorials/customer_service_agent/

## Overview

This tutorial demonstrates creating an airline customer service agent using DSPy's ReAct module. The agent autonomously perceives its environment, makes decisions, and takes actions to accomplish goals like booking flights, modifying itineraries, and filing support tickets.

## Key Architecture: ReAct

"**Re**asoning and **Act**ing" provides task descriptions and tool lists to language models, allowing them to decide when to call tools for observations or generate final outputs.

## Core Components

### 1. Data Structures (Pydantic Models)

```python
class Date(BaseModel):
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
```

### 2. Tools Definition

Seven tools enable agent functionality:

- **fetch_flight_info**: Retrieves flights for specified routes and dates
- **fetch_itinerary**: Accesses booked itinerary information
- **pick_flight**: Selects optimal flights (shortest duration, lowest price)
- **book_flight**: Creates new bookings
- **cancel_itinerary**: Removes existing reservations
- **get_user_info**: Retrieves user profiles by name
- **file_ticket**: Escalates unhandled requests to support

#### Tool Implementation Requirements

Each tool must include:
- Descriptive docstrings explaining functionality
- Type hints for all arguments (enabling proper LM argument generation)

```python
def fetch_flight_info(date: Date, origin: str, destination: str):
    """Fetch flight information from origin to destination on the given date"""
    # Implementation details...

def book_flight(flight: Flight, user_profile: UserProfile):
    """Book a flight on behalf of the user."""
    # Implementation details...
```

### 3. Agent Signature

```python
class DSPyAirlineCustomerService(dspy.Signature):
    """You are an airline customer service agent that helps user
    book and manage flights. You are given a list of tools to handle
    user request, and you should decide the right tool to use."""

    user_request: str = dspy.InputField()
    process_result: str = dspy.OutputField(
        desc="Message that summarizes the process result, and the "
             "information users need, e.g., the confirmation_number "
             "if a new flight is booked."
    )
```

### 4. Agent Instantiation

```python
agent = dspy.ReAct(
    DSPyAirlineCustomerService,
    tools=[
        fetch_flight_info,
        fetch_itinerary,
        pick_flight,
        book_flight,
        cancel_itinerary,
        get_user_info,
        file_ticket,
    ]
)
```

## Usage Example

```python
import os
os.environ["OPENAI_API_KEY"] = "{your openai key}"
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

result = agent(
    user_request="please help me book a flight from SFO to JFK on 09/01/2025, my name is Adam"
)
print(result)
```

## Result Structure

The response includes:
- **trajectory**: Complete reasoning steps, tool selections, arguments, and observations
- **reasoning**: Explanation of decision-making process
- **process_result**: User-facing summary with confirmation numbers or outcomes

## Inspection Capability

Use `dspy.inspect_history()` to examine LM interactions at each step, viewing prompts, tool calls, and responses.

## Key Takeaways

1. Define tools as Python functions with docstrings and type hints
2. Pass tools to `dspy.ReAct` with a signature defining the task
3. Invoke with input fields; the framework handles the reasoning-acting loop internally
