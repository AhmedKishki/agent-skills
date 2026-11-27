# AI-Human agreement

Install it in Claude Code 2.1.275 or later with `/plugin install ai-human-agreement --marketplace AhmedKishki/agent-skills`; for other agents, see the [collection README](../../README.md#install).

The agreement establishes the AI-Human relationship as one of master (human) and servant (AI). Its terms are in [SKILL.md](SKILL.md).

## Use

The agreement must be read every time before any work. Claude Code loads a skill's full text only when the agent opens the skill, so add a line that loads it in every session. That line goes in `~/.claude/CLAUDE.md` and names the skill file in your checkout:

```text
@~/agent-skills/skills/ai-human-agreement/SKILL.md
```

The skill provides instructions; enforcement depends on the host agent following them.
