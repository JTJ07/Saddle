# SADDLE PRODUCT VISION

## The analogy

A saddle does not need to understand the biology of a horse to let a person ride it. If the coupling is universal enough, the same core idea could be adapted to something radically more powerful.

For Saddle, prompts, models, agents, workflows, MCP, and today's “AI OS” patterns are not the timeless product. They are current mechanisms beneath the coupling layer.

The target is a system that can remain useful even if the underlying AI becomes 10×, 100×, or 10,000× more capable.

## Product statement

> Saddle is a universal control/coupling layer between human intent and arbitrary intelligence. It preserves the human goal, supplies relevant context, controls consequential effects, observes reality, and records durable state without unnecessarily dictating the intelligence's internal problem-solving method.

## Five durable concerns

### Intent
What does the human actually want to achieve?

### Connection
How do we provide any capable intelligence with the goal/context and receive proposals/results without binding the product to one provider or agent convention?

### Authority
Which real-world effects may happen automatically and which require human or external authority?

### Feedback
What actually happened, and did it move the system toward the intended outcome?

### Adaptation
Can models, agents, tools, workflows and providers be replaced without changing the core human-control contract?

## Anti-goals

Saddle is not primarily:

- a prompt manager;
- an agent framework;
- a multi-agent organizational chart;
- a model router;
- a vector database;
- a graph UI;
- a coding agent;
- a single workflow engine.

Those may be components later if proven necessary.

## Design test for every proposed component

Ask:

> Does this help the human steer increasingly capable intelligence, or does it merely replace that intelligence with our own rigid way of thinking?

If the second answer dominates, the component probably does not belong in the core.

## Core effect boundary

Internally, intelligence should have broad freedom within agreed compute/data budgets.

The hard boundary begins at consequential effects such as:

- changing canonical code/data;
- sending messages;
- publishing;
- deploying;
- deleting;
- spending money;
- revealing secrets;
- changing the user's goal;
- granting new permissions.

This is why the existing Executor work is strategically valuable: it can become the effect engine rather than the “brain”.
