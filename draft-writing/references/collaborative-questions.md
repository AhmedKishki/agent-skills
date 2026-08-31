# Collaborative questions, answer routing, and user synthesis

Questions stay in chat. Record only the current unresolved question or decision in the [activity tracker](activity-tracker.md), with enough self-contained context to resume; never create or export Q&A history. Ask whenever a premise, relation, definition, scope, qualification, judgement, conclusion, synthesis, transition, heading, function, or meaning-changing order is missing. Before complete-predraft approval, do not ask about non-removal Human-preserving corrections; after a predraft-report finding, every proposed correction requires explicit approval. State only the net-new delta and minimum established context. If a user addition is already represented with the same meaning, function, scope, qualification, authority, and use, say so and save no duplicate; ask only when its intended function, provenance, or use differs.

For each question:

- give only the established material, exact gap, and consequence needed to decide;
- use plain language, full source names, readable descriptions, and affected wording—never filenames, timestamps, codes, IDs, tracker/workflow labels, or internal status;
- summarise enough backend content that the user need not open a file;
- ask one concrete question and give exactly one concise suggestion with origin, Human-word percentage, and full-name/user-wording bases, except that a first-turn synthesis gap uses only the unresolved process suggestion required below.

For a substantive change, also show the current point, proposed net-new change, reason, any exact removal impact, and affected article/process parts before asking; store only the resolved direction. Follow the removal-impact protocol even when the change appears to be simple cleanup. For unclear metatheory fit, ask how the ideas connect in ordinary article language. For unclear source role, describe the passage, ask article/framework/both, and suggest the narrowest established function.

Build the suggestion in this order, including for a predraft-report finding:

1. Before global draft production, attempt eligible Human wording and relations with [white box synthesis](white-box-synthesis.md). If draft production exposed the gap, first reopen the predraft report and affected arc or predraft owner.
2. If the attempt exposes a gap, issue its gap alert, keep the point unresolved, and stop that turn. The sole suggestion is to leave it unresolved pending a rescan or the user's wording: **Process suggestion: AI · Human wording: 0% · not article wording · Basis: reported synthesis gap**.
3. In a later turn, rescan relevant originals and record sources, locators, and coverage; return to Step 1 if new Human material closes the gap.
4. If that coverage contains no support, alert the user that the gap remains. Only then offer one linear **AI gap suggestion** for the readable paragraph location, role, boundary, starting point, and intended conclusion; name partial/inaccessible sources. Show **Origin: AI gap suggestion, not source-supported synthesis · Human wording: P% · Sources checked: full names and coverage · Human words retained: exact phrase → full source name or user wording | none**. Keep framework/use details internal and the gap unresolved until the user responds.
5. If the rescan or coverage record is missing, suggest leaving the point unresolved and give an empty frame labelled **Process suggestion: AI · Human wording: 0% · not article wording · Basis: missing rescan or coverage**.

A decision suggestion first reduces exact Human criteria; if they do not decide it, label the recommendation **Process suggestion: AI**. Reserve **AI gap suggestion** for article wording under Step 4. For role, contradiction, structure, emphasis, repetition home, or global treatment, recommend one answer with its basis. Predraft selection, report-treatment/exception approval, and draft use remain separate.

## Route the answer

Route each function once under [file-output-standard.md](file-output-standard.md); if indivisible, keep it in its primary home and reference it elsewhere. Exclude acknowledgements, navigation, milestones, questions, rejected fixes, and temporary organisation. Wording/raw-material fixes belong in predraft; structure, sequence, placement, emphasis, and sole homes belong in the arc; approved execution-level adjacency/combination/cut/consolidation treatments within those arc decisions and permitted diagnostic exceptions belong in the predraft report; workflow state belongs in the tracker. If an answer contradicts thesis/vision, show both formulations and ask which governs before saving content.

## User synthesis file

Create `{project}-user-synthesis-YYYY-MM-DD-HHMMSS.md` only for the user's article wording, supplementary ideas, or synthesis outside thesis/durable guidance. Keep active wording once with Human-preserving corrections; omit discussion, approvals, placement, organisation, and superseded content. Cite only user-named sources. Ask about conflict with operative metatheory; never manufacture fit.

    # User synthesis

    [Lean process header]

    **Content authorship:** Human · Human wording: 100% · Method: user wording · Basis/Use: supplied by each heading

    ## Readable topic
    Exact user synthesis.

    **Basis:** exact user exchange and user-named source material

    Stamp only Mixed/AI exceptions locally.

Human wording is wording-cleared, not predraft-selected. Exact selection leaves its original use unchanged and gives only the predraft copy **Use: Predraft raw material**. Use [migration](migration-to-v7.md) for schema-v6 Q&A/records.
