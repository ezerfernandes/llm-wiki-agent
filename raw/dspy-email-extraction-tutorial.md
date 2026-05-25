# Email Information Extraction with DSPy

Source: https://dspy.ai/tutorials/email_extraction/

## Overview
This tutorial demonstrates building an intelligent email processing system using DSPy that automatically extracts, classifies, and structures information from various email types.

## Core Capabilities
The system performs five main functions:
- Classification of email types (orders, support requests, meetings, newsletters, etc.)
- Entity extraction (dates, amounts, product names, contact details)
- Urgency level determination and action identification
- Data structuring into consistent formats
- Robust handling of multiple email formats

## Data Structures

### Enumerations Defined
```python
class EmailType(str, Enum):
    ORDER_CONFIRMATION = "order_confirmation"
    SUPPORT_REQUEST = "support_request"
    MEETING_INVITATION = "meeting_invitation"
    NEWSLETTER = "newsletter"
    PROMOTIONAL = "promotional"
    INVOICE = "invoice"
    SHIPPING_NOTIFICATION = "shipping_notification"
    OTHER = "other"

class UrgencyLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ExtractedEntity(BaseModel):
    entity_type: str
    value: str
    confidence: float
```

## DSPy Signatures

### ClassifyEmail Signature
```python
class ClassifyEmail(dspy.Signature):
    """Classify the type and urgency of an email based on its content."""

    email_subject: str = dspy.InputField(desc="The subject line of the email")
    email_body: str = dspy.InputField(desc="The main content of the email")
    sender: str = dspy.InputField(desc="Email sender information")

    email_type: EmailType = dspy.OutputField(desc="The classified type of email")
    urgency: UrgencyLevel = dspy.OutputField(desc="The urgency level of the email")
    reasoning: str = dspy.OutputField(desc="Brief explanation of the classification")
```

### ExtractEntities Signature
```python
class ExtractEntities(dspy.Signature):
    """Extract key entities and information from email content."""

    email_content: str = dspy.InputField(desc="The full email content including subject and body")
    email_type: EmailType = dspy.InputField(desc="The classified type of email")

    key_entities: list[ExtractedEntity] = dspy.OutputField(desc="List of extracted entities with type, value, and confidence")
    financial_amount: Optional[float] = dspy.OutputField(desc="Any monetary amounts found (e.g., '$99.99')")
    important_dates: list[str] = dspy.OutputField(desc="List of important dates found in the email")
    contact_info: list[str] = dspy.OutputField(desc="Relevant contact information extracted")
```

### GenerateActionItems Signature
```python
class GenerateActionItems(dspy.Signature):
    """Determine what actions are needed based on the email content and extracted information."""

    email_type: EmailType = dspy.InputField()
    urgency: UrgencyLevel = dspy.InputField()
    email_summary: str = dspy.InputField(desc="Brief summary of the email content")
    extracted_entities: list[ExtractedEntity] = dspy.InputField(desc="Key entities found in the email")

    action_required: bool = dspy.OutputField(desc="Whether any action is required")
    action_items: list[str] = dspy.OutputField(desc="List of specific actions needed")
    deadline: Optional[str] = dspy.OutputField(desc="Deadline for action if applicable")
    priority_score: int = dspy.OutputField(desc="Priority score from 1-10")
```

### SummarizeEmail Signature
```python
class SummarizeEmail(dspy.Signature):
    """Create a concise summary of the email content."""

    email_subject: str = dspy.InputField()
    email_body: str = dspy.InputField()
    key_entities: list[ExtractedEntity] = dspy.InputField()

    summary: str = dspy.OutputField(desc="A 2-3 sentence summary of the email's main points")
```

## Email Processing Module

```python
class EmailProcessor(dspy.Module):
    """A comprehensive email processing system using DSPy."""

    def __init__(self):
        super().__init__()
        self.classifier = dspy.ChainOfThought(ClassifyEmail)
        self.entity_extractor = dspy.ChainOfThought(ExtractEntities)
        self.action_generator = dspy.ChainOfThought(GenerateActionItems)
        self.summarizer = dspy.ChainOfThought(SummarizeEmail)

    def forward(self, email_subject: str, email_body: str, sender: str = ""):
        """Process an email and extract structured information."""

        # Step 1: Classify the email
        classification = self.classifier(
            email_subject=email_subject,
            email_body=email_body,
            sender=sender
        )

        # Step 2: Extract entities
        full_content = f"Subject: {email_subject}\n\nFrom: {sender}\n\n{email_body}"
        entities = self.entity_extractor(
            email_content=full_content,
            email_type=classification.email_type
        )

        # Step 3: Generate summary
        summary = self.summarizer(
            email_subject=email_subject,
            email_body=email_body,
            key_entities=entities.key_entities
        )

        # Step 4: Determine actions
        actions = self.action_generator(
            email_type=classification.email_type,
            urgency=classification.urgency,
            email_summary=summary.summary,
            extracted_entities=entities.key_entities
        )

        # Step 5: Structure the results
        return dspy.Prediction(
            email_type=classification.email_type,
            urgency=classification.urgency,
            summary=summary.summary,
            key_entities=entities.key_entities,
            financial_amount=entities.financial_amount,
            important_dates=entities.important_dates,
            action_required=actions.action_required,
            action_items=actions.action_items,
            deadline=actions.deadline,
            priority_score=actions.priority_score,
            reasoning=classification.reasoning,
            contact_info=entities.contact_info
        )
```

## Implementation and Configuration

```python
import os

def run_email_processing_demo():
    """Demonstration of the email processing system."""

    # Configure DSPy
    lm = dspy.LM(model='openai/gpt-4o-mini')
    dspy.configure(lm=lm)
    os.environ["OPENAI_API_KEY"] = "<YOUR OPENAI KEY>"

    # Create processor
    processor = EmailProcessor()
```

## Test Dataset
Three sample emails demonstrate the system:

1. **Order Confirmation** - MacBook Pro purchase with amount, tracking number, and delivery date
2. **Support Request** - Server outage alert requiring urgent action
3. **Meeting Invitation** - Q4 planning session with scheduled date and deadline

## Results Summary
The system successfully:
- Classified emails into correct types
- Assigned appropriate urgency levels (low, critical, medium)
- Extracted financial amounts ($2,399.00)
- Identified key dates and deadlines
- Generated action items with priority scores
- Produced concise summaries capturing main points

## Optional Enhancements
The tutorial recommends expanding the system through:
- Additional email type classifications
- Integration with email providers (Gmail API, Outlook, IMAP)
- Different LLM experimentation and optimization strategies
- Multilingual support capabilities
- Performance optimization techniques

## MLflow Integration
The tutorial suggests optional MLflow setup for:
- Visualization of prompts and optimization progress
- Tracing DSPy behavior
- Experiment tracking and explainability
