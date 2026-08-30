# Collaborative questions, answer routing, and user synthesis

Questions stay in chat; only a requested [user export](user-export.md) may copy the current unanswered question/suggestion set, never a Q&A history. Ask whenever a premise, relation, definition, scope, qualification, judgement, conclusion, synthesis, transition, heading, function, or meaning-changing order is missing; never ask about Human-preserving operations.

For each question:

- give only the established material, exact gap, and consequence needed to decide;
- use plain language, full source names, readable descriptions, and affected wording—never filenames, timestamps, codes, IDs, tracker/workflow labels, or internal status;
- summarise enough backend content that the user need not open a file;
- ask one concrete question and give exactly one concise suggestion with origin, Human-word percentage, and full-name/user-wording bases.

For a substantive change, also show the current point, proposed change, reason, and affected article/process parts before asking; store only the resolved direction. For unclear metatheory fit, ask how the ideas connect in ordinary article language. For unclear source role, describe the passage, ask article/framework/both, and suggest the narrowest established function.

Build the suggestion in this order:

1. Complete eligible Human wording and relations: use [reductive synthesis](reductive-synthesis.md).
2. Otherwise rescan relevant originals and record sources, locators, and coverage; return to Step 1 if new Human material closes the gap.
3. If that coverage contains no support: offer one linear **AI gap suggestion** for the readable paragraph location, role, boundary, starting point, and intended conclusion; name partial/inaccessible sources. Show **Origin: AI gap suggestion, not source-supported synthesis · Human wording: P% · Sources checked: full names and coverage · Human words retained: exact phrase → full source name or user wording | none**. Keep framework/use details internal.
4. If the rescan or coverage record is missing: suggest leaving the point unresolved and give an empty frame labelled **Process suggestion: AI · Human wording: 0% · not article wording · Basis: missing rescan or coverage**.

A decision suggestion first reduces exact Human criteria; if they do not decide it, label the recommendation **Process suggestion: AI**. Reserve **AI gap suggestion** for article wording under Step 3. For role, contradiction, or structure, recommend one answer with its basis. Predraft selection and draft placement remain separate.

## Route the answer

Route each function once under [file-output-standard.md](file-output-standard.md); if indivisible, keep it in its primary home and reference it elsewhere. Exclude acknowledgements, navigation, grammar choices, milestones, questions, and temporary organisation. Structure belongs in the arc and workflow state in the tracker. If an answer contradicts thesis/vision, show both formulations and ask which governs before saving content.

## User synthesis file

Create `{project}-user-synthesis-YYYY-MM-DD-HHMMSS.md` only for the user's article wording, supplementary ideas, or synthesis outside thesis/durable guidance. Keep active wording once with Human-preserving corrections; omit discussion, approvals, placement, organisation, and superseded content. Cite only user-named sources. Ask about conflict with operative metatheory; never manufacture fit.

    # User synthesis

    [Lean process header]

    **Content authorship:** Human · Human wording: 100% · Method: user wording · Basis/Use: supplied by each heading

    ## Readable topic
    Exact user synthesis.

    **Basis:** exact user exchange and user-named source material

    Stamp only Mixed/AI exceptions locally.

Human wording is wording-cleared, not predraft-selected. Exact selection leaves its original use unchanged and gives only the predraft copy **Use: Predraft raw material**. Use [migration](migration-to-v6.md) for v5 Q&A/records.
