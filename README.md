# Bricks + Codex MCP Starter

## Magyar

Ez a privát repository egy újrahasználható kezdőcsomag **Bricks Builder + WordPress MCP + Codex** projektekhez.

A célja, hogy egy új Bricks webhely Codexhez kapcsolása után ne minden projektben nulláról kelljen kialakítani a munkafolyamatot. A repository általános bootstrap promptokat, audit-szabályokat, `AGENTS.md` mintákat, biztonsági elveket és dokumentációs struktúrát tartalmaz.

### Mire szolgál?

A starter segítségével a Codex egy új webhelyen:

- feltérképezi a WordPress / Bricks architektúrát;
- ellenőrzi a releváns plugin- és integrációs környezetet;
- feltérképezi az adatmodellt (CPT-k, taxonómiák, mezők, kapcsolatok, query-k);
- dokumentálja a Bricks design systemet, theme style-okat, classokat, változókat és breakpointokat;
- végigvizsgálja az oldalakat és template-eket;
- böngészőben is ellenőrzi a publikus frontend tényleges vizuális megjelenését és reszponzív működését;
- külön vizsgálja a WooCommerce-t, ha telepítve és aktív;
- tartós, site-specifikus tudásbázist és `AGENTS.md`-t hoz létre a konkrét Codex projektben.

### Fontos elv

Ez a repository **nem egy konkrét webhely dokumentációja**. A benne lévő promptok és template-ek site-agnosztikusak.

Minden konkrét webhely külön Codex projektet kap, például:

```text
Projects/
├── client-a-bricks/
│   ├── AGENTS.md
│   └── docs/bricks/
├── client-b-bricks/
│   ├── AGENTS.md
│   └── docs/bricks/
└── ...
```

### Repository struktúra

```text
bricks-codex-mcp-starter/
├── README.md
├── CHANGELOG.md
├── .gitignore
├── prompts/
│   ├── 00-full-site-bootstrap-audit.md
│   └── 01-agents-md-refresh.md
├── templates/
│   ├── AGENTS.template.md
│   └── audit-progress.template.md
└── docs/
    ├── setup-bricks-mcp.md
    ├── setup-codex.md
    ├── security.md
    └── workflow.md
```

### Kezdés

1. Kösd össze az adott WordPress / Bricks webhelyet a Codexszel MCP-n keresztül.
2. Telepítsd a Bricks skills csomagot a Codexhez.
3. Hozz létre külön helyi Codex projektmappát a webhelynek.
4. Futtasd a `prompts/00-full-site-bootstrap-audit.md` promptot egy új Codex threadben.
5. Az audit után csökkentsd az MCP user jogosultságait a napi munkához szükséges minimumra.
6. A későbbi threadek mindig a létrehozott `AGENTS.md` és `docs/bricks/` tudásbázisból induljanak, de írás előtt ellenőrizzék újra az érintett live állapotot.

### Biztonság

**Soha ne commitolj WordPress Application Passwordöt, Codex `config.toml` fájlt, API kulcsot, jelszót vagy más credentialt ebbe a repositoryba.**

A repository privát státusza nem helyettesíti a secret hygiene-t.

---

## English

This private repository is a reusable starter kit for **Bricks Builder + WordPress MCP + Codex** projects.

Its purpose is to avoid rebuilding the same workflow from scratch for every Bricks site. It contains generic bootstrap prompts, audit rules, `AGENTS.md` templates, security guidance, and a durable documentation structure.

### What does it do?

With this starter, Codex can:

- map the WordPress / Bricks architecture;
- inspect the relevant plugin and integration ecosystem;
- map the data model (CPTs, taxonomies, fields, relationships, queries);
- document the Bricks design system, theme styles, classes, variables, and breakpoints;
- inspect pages and templates;
- inspect the rendered public frontend in a browser to understand real visual composition and responsive behavior;
- audit WooCommerce when it is installed and active;
- create a durable site-specific knowledge base and project `AGENTS.md`.

### Core principle

This repository is **not site-specific documentation**. All prompts and templates here are site-agnostic.

Each real website should have its own separate Codex project containing its generated `AGENTS.md` and `docs/bricks/` knowledge base.

### Repository structure

```text
bricks-codex-mcp-starter/
├── README.md
├── CHANGELOG.md
├── .gitignore
├── prompts/
│   ├── 00-full-site-bootstrap-audit.md
│   └── 01-agents-md-refresh.md
├── templates/
│   ├── AGENTS.template.md
│   └── audit-progress.template.md
└── docs/
    ├── setup-bricks-mcp.md
    ├── setup-codex.md
    ├── security.md
    └── workflow.md
```

### Getting started

1. Connect the target WordPress / Bricks site to Codex through MCP.
2. Install the Bricks skills for Codex.
3. Create a dedicated local Codex project folder for the target site.
4. Run `prompts/00-full-site-bootstrap-audit.md` in a new Codex thread.
5. After the bootstrap audit, reduce the MCP user's permissions to the minimum required for normal work.
6. Future threads should use the generated `AGENTS.md` and `docs/bricks/` knowledge base, while re-reading affected live resources before writes.

### Security

**Never commit WordPress Application Passwords, Codex `config.toml`, API keys, passwords, tokens, or other credentials to this repository.**

Private repository visibility is not a substitute for proper secret hygiene.

---

Status: early working draft / evolving workflow.
