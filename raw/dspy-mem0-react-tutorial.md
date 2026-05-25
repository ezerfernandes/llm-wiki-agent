# Memory-Enabled ReAct Agents with DSPy and Mem0 - Complete Tutorial

Source: https://dspy.ai/tutorials/mem0_react_agent/

## Overview

This tutorial demonstrates building conversational agents that retain information across interactions by combining DSPy's ReAct framework with Mem0's memory system.

## What You'll Build

The tutorial guides creation of agents capable of:

- Storing and recalling user preferences from previous conversations
- Managing factual information about users and topics
- Making decisions informed by accumulated context
- Sustaining coherent multi-turn dialogues
- Categorizing different memory types (preferences, facts, experiences)

## Prerequisites

- Working knowledge of DSPy and ReAct agents
- Python 3.9 or newer
- API credentials for an LLM service

## Installation

```
pip install dspy mem0ai
```

## Implementation Steps

### Step 1: Mem0 Integration Setup

Initialize the memory system with language model and embedding configurations:

```python
import dspy
from mem0 import Memory
import os
from typing import List, Dict, Any, Optional
from datetime import datetime

os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o-mini",
            "temperature": 0.1
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}
```

### Step 2: Memory-Aware Tools

Create a dedicated tools class for memory operations:

```python
import datetime

class MemoryTools:
    """Tools for interacting with the Mem0 memory system."""

    def __init__(self, memory: Memory):
        self.memory = memory

    def store_memory(self, content: str, user_id: str = "default_user") -> str:
        """Store information in memory."""
        try:
            self.memory.add(content, user_id=user_id)
            return f"Stored memory: {content}"
        except Exception as e:
            return f"Error storing memory: {str(e)}"

    def search_memories(self, query: str, user_id: str = "default_user", limit: int = 5) -> str:
        """Search for relevant memories."""
        try:
            results = self.memory.search(query, user_id=user_id, limit=limit)
            if not results:
                return "No relevant memories found."

            memory_text = "Relevant memories found:\n"
            for i, result in enumerate(results["results"]):
                memory_text += f"{i}. {result['memory']}\n"
            return memory_text
        except Exception as e:
            return f"Error searching memories: {str(e)}"

    def get_all_memories(self, user_id: str = "default_user") -> str:
        """Get all memories for a user."""
        try:
            results = self.memory.get_all(user_id=user_id)
            if not results:
                return "No memories found for this user."

            memory_text = "All memories for user:\n"
            for i, result in enumerate(results["results"]):
                memory_text += f"{i}. {result['memory']}\n"
            return memory_text
        except Exception as e:
            return f"Error retrieving memories: {str(e)}"

    def update_memory(self, memory_id: str, new_content: str) -> str:
        """Update an existing memory."""
        try:
            self.memory.update(memory_id, new_content)
            return f"Updated memory with new content: {new_content}"
        except Exception as e:
            return f"Error updating memory: {str(e)}"

    def delete_memory(self, memory_id: str) -> str:
        """Delete a specific memory."""
        try:
            self.memory.delete(memory_id)
            return "Memory deleted successfully."
        except Exception as e:
            return f"Error deleting memory: {str(e)}"

def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

### Step 3: Memory-Enhanced ReAct Agent

Build the main agent with memory capabilities:

```python
class MemoryQA(dspy.Signature):
    """
    You're a helpful assistant and have access to memory method.
    Whenever you answer a user's input, remember to store the information in memory
    so that you can use it later.
    """
    user_input: str = dspy.InputField()
    response: str = dspy.OutputField()

class MemoryReActAgent(dspy.Module):
    """A ReAct agent enhanced with Mem0 memory capabilities."""

    def __init__(self, memory: Memory):
        super().__init__()
        self.memory_tools = MemoryTools(memory)

        # Create tools list for ReAct
        self.tools = [
            self.memory_tools.store_memory,
            self.memory_tools.search_memories,
            self.memory_tools.get_all_memories,
            get_current_time,
            self.set_reminder,
            self.get_preferences,
            self.update_preferences,
        ]

        # Initialize ReAct with our tools
        self.react = dspy.ReAct(
            signature=MemoryQA,
            tools=self.tools,
            max_iters=6
        )

    def forward(self, user_input: str):
        """Process user input with memory-aware reasoning."""

        return self.react(user_input=user_input)

    def set_reminder(self, reminder_text: str, date_time: str = None, user_id: str = "default_user") -> str:
        """Set a reminder for the user."""
        reminder = f"Reminder set for {date_time}: {reminder_text}"
        return self.memory_tools.store_memory(
            f"REMINDER: {reminder}",
            user_id=user_id
        )

    def get_preferences(self, category: str = "general", user_id: str = "default_user") -> str:
        """Get user preferences for a specific category."""
        query = f"user preferences {category}"
        return self.memory_tools.search_memories(
            query=query,
            user_id=user_id
        )

    def update_preferences(self, category: str, preference: str, user_id: str = "default_user") -> str:
        """Update user preferences."""
        preference_text = f"User preference for {category}: {preference}"
        return self.memory_tools.store_memory(
            preference_text,
            user_id=user_id
        )
```

### Step 4: Running the Agent

Execute a demonstration with sample conversations:

```python
import time

def run_memory_agent_demo():
    """Demonstration of memory-enhanced ReAct agent."""

    # Configure DSPy
    lm = dspy.LM(model='openai/gpt-4o-mini')
    dspy.configure(lm=lm)

    # Initialize memory system
    memory = Memory.from_config(config)

    # Create our agent
    agent = MemoryReActAgent(memory)

    # Sample conversation demonstrating memory capabilities
    print("🧠 Memory-Enhanced ReAct Agent Demo")
    print("=" * 50)

    conversations = [
        "Hi, I'm Alice and I love Italian food, especially pasta carbonara.",
        "I'm Alice. I prefer to exercise in the morning around 7 AM.",
        "I'm Alice. What do you remember about my food preferences?",
        "I'm Alice. Set a reminder for me to go grocery shopping tomorrow.",
        "I'm Alice. What are my exercise preferences?",
        "I'm Alice. I also enjoy hiking on weekends.",
        "I'm Alice. What do you know about me so far?"
    ]

    for i, user_input in enumerate(conversations, 1):
        print(f"\n📝 User: {user_input}")

        try:
            response = agent(user_input=user_input)
            print(f"🤖 Agent: {response.response}")
            time.sleep(1)

        except Exception as e:
            print(f"❌ Error: {e}")

# Run the demonstration
if __name__ == "__main__":
    run_memory_agent_demo()
```

## Expected Output Sample

The agent demonstrates context retention across multiple turns:

- Initial user introduction about food preferences is stored
- Exercise routine information gets persisted
- Later queries successfully retrieve stored preferences
- Reminders can be set and tracked
- Agent synthesizes all collected information when asked for summary

## Advanced Recommendations

The tutorial suggests pursuing these enhancements:

- Implement persistent memory storage using relational or document databases
- Add organizational tags and categorization systems
- Create expiration rules for memory lifecycle management
- Build user isolation mechanisms for multi-user deployments
- Develop analytics capabilities for memory insights
- Integrate vector databases for semantic search improvements
- Establish compression strategies for efficient long-term storage

## Key Concepts

"Whenever you answer a user's input, remember to store the information in memory so that you can use it later" - this principle enables agents to build personalized knowledge bases.

The combination allows agents to reason through multi-step problems while simultaneously managing contextual information for future interactions, creating more coherent and personalized AI experiences.
