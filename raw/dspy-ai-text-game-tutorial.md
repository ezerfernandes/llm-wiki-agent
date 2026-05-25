# Building a Creative Text-Based AI Game with DSPy

Source: https://dspy.ai/tutorials/ai_text_game/
Fetched: 2026-05-24 via WebFetch

## Introduction

This tutorial demonstrates how to create an interactive text-based adventure game using DSPy's modular programming approach. You'll build a dynamic game where AI handles narrative generation, character interactions, and adaptive gameplay.

## What You'll Build

An intelligent text-based adventure game featuring:

- Dynamic story generation and branching narratives
- AI-powered character interactions and dialogue
- Adaptive gameplay that responds to player choices
- Inventory and character progression systems
- Save/load game state functionality

## Setup

```bash
pip install dspy rich typer
```

## Section Outline

1. Step 1: Core Game Framework
2. Step 2: AI-Powered Story Generation
3. Step 3: Game Interface and Interaction
4. Step 4: Main Game Loop
5. Example Gameplay
6. Next Steps

## LM Configuration

```python
lm = dspy.LM(model='openai/gpt-4o-mini')
dspy.configure(lm=lm)
```

## Game Framework Components

- `Player` dataclass: character stats (health, level, experience, inventory, skills)
- `GameContext` dataclass: narrative state (location, story progress, NPCs met, completed quests)
- `GameEngine` class: orchestrates game state and save/load functionality
- `GameState` enum: phases (menu, playing, inventory, character, game_over)

## Signatures

### StoryGenerator

```python
class StoryGenerator(dspy.Signature):
    """Generate dynamic story content based on current game state."""
    location: str = dspy.InputField(desc="Current location")
    player_info: str = dspy.InputField(desc="Player information and stats")
    story_progress: int = dspy.InputField(desc="Current story progress level")
    recent_actions: str = dspy.InputField(desc="Player's recent actions")

    scene_description: str = dspy.OutputField(desc="Vivid description of current scene")
    available_actions: list[str] = dspy.OutputField(desc="List of possible player actions")
    npcs_present: list[str] = dspy.OutputField(desc="NPCs present in this location")
    items_available: list[str] = dspy.OutputField(desc="Items that can be found or interacted with")
```

### DialogueGenerator

```python
class DialogueGenerator(dspy.Signature):
    """Generate NPC dialogue and responses."""
    npc_name: str = dspy.InputField(desc="Name and type of NPC")
    npc_personality: str = dspy.InputField(desc="NPC personality and background")
    player_input: str = dspy.InputField(desc="What the player said or did")
    context: str = dspy.InputField(desc="Current game context and history")

    npc_response: str = dspy.OutputField(desc="NPC's dialogue response")
    mood_change: str = dspy.OutputField(desc="How NPC's mood changed (positive/negative/neutral)")
    quest_offered: bool = dspy.OutputField(desc="Whether NPC offers a quest")
    information_revealed: str = dspy.OutputField(desc="Any important information shared")
```

### ActionResolver

```python
class ActionResolver(dspy.Signature):
    """Resolve player actions and determine outcomes."""
    action: str = dspy.InputField(desc="Player's chosen action")
    player_stats: str = dspy.InputField(desc="Player's current stats and skills")
    context: str = dspy.InputField(desc="Current game context")
    difficulty: str = dspy.InputField(desc="Difficulty level of the action")

    success: bool = dspy.OutputField(desc="Whether the action succeeded")
    outcome_description: str = dspy.OutputField(desc="Description of what happened")
    stat_changes: dict[str, int] = dspy.OutputField(desc="Changes to player stats")
    items_gained: list[str] = dspy.OutputField(desc="Items gained from this action")
    experience_gained: int = dspy.OutputField(desc="Experience points gained")
```

## GameAI Module

```python
class GameAI(dspy.Module):
    """Main AI module for game logic and narrative."""

    def __init__(self):
        super().__init__()
        self.story_gen = dspy.ChainOfThought(StoryGenerator)
        self.dialogue_gen = dspy.ChainOfThought(DialogueGenerator)
        self.action_resolver = dspy.ChainOfThought(ActionResolver)
```

Methods include `generate_scene()`, `handle_dialogue()`, and `resolve_action()`.

## UI

Rich library panels for: game headers / status displays, location descriptions with NPCs and items, available action menus, inventory management, help system documentation.

## Main Game Loop

- Generate dynamic scenes from current state
- Display player status and location context
- Present action options
- Process player selections (incl. save/inventory commands)
- Resolve NPC interactions via dialogue
- Apply action consequences (stat changes, items, experience)
- Check game-over conditions

## Features Demonstrated

- Character creation with skill point allocation across strength, intelligence, charisma, stealth
- Persistent state via JSON save/load
- NPC interactions with quest detection
- Experience accumulation + leveling
- Inventory collection and management
