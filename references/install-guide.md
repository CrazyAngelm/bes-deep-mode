# BES Deep Mode install guide

Use this reference when installing the `bes-deep-mode` skill on another device, profile, or containerized tenant.

## Install path

Main profile:

```bash
mkdir -p ~/.agent/skills/autonomous-ai-agents/bes-deep-mode
nano ~/.agent/skills/autonomous-ai-agents/bes-deep-mode/SKILL.md
```

Named profile:

```bash
mkdir -p ~/.agent/profiles/<profile-name>/skills/autonomous-ai-agents/bes-deep-mode
nano ~/.agent/profiles/<profile-name>/skills/autonomous-ai-agents/bes-deep-mode/SKILL.md
```

Container tenant with `AGENT_HOME=/opt/data` mounted from `/srv/agent/<tenant>`:

```bash
mkdir -p /srv/agent/<tenant>/skills/autonomous-ai-agents/bes-deep-mode
nano /srv/agent/<tenant>/skills/autonomous-ai-agents/bes-deep-mode/SKILL.md
docker compose up -d --force-recreate
```

## Verify

```bash
agent skills list | grep -i bes-deep-mode
agent chat -q "Use deep mode and produce a concise installation-check plan for the BES skill."
```

For a profile:

```bash
agent -p <profile-name> skills list | grep -i bes-deep-mode
```

## Deployment note

For reusable B2B/B2C agent images, seed the skill into a tenant volume on first start rather than overwriting customer skill directories. Keep it versioned and avoid enabling BES for every simple task.

Recommended progression:

1. MVP: this skill.
2. Better: a local `bes_runner` tool that generates candidates and evaluates them with deterministic structure.
3. Production: a BES service before the agent worker:

```text
user task -> classifier -> simple -> normal agent path
                    \\-> complex -> BES planner -> agent worker
```
