# Reverse-engineering

- Work through one chunk at a time.

1. Locate the chunk in the actual source by file and line range. Give only enough
   surrounding segment context to show why it exists. Show the relevant code
   once when useful; label pseudocode and proposed alternatives distinctly.
2. State its purpose and relevant contract, then explain its mechanism in
   execution order. Match the agreed explanation depth without unrelated lessons.
3. Inspect dependency implementations or authoritative API documentation when
   their behaviour affects the explanation. Names alone are not evidence.
   Distinguish verified contracts from assumptions and unresolved behaviour.
4. Summarise understandable fragments by contract. Expand hidden mechanisms
   when blocking, state changes, ownership, errors, or other consequential
   behaviour would otherwise remain unexplained. Do not chase every call.
5. Separate current behaviour from design assessment. Identify material code
   patterns relevant to the goal, explain their concrete costs, and describe
   simpler alternatives where justified. Do not turn a walkthrough into an
   unrelated whole-project review.
6. Stop after the chunk and wait for the user's direction before continuing.
