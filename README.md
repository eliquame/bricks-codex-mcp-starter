# Bricks + Codex MCP Starter

Reusable starter kit for **Bricks Builder + WordPress MCP + Codex** projects.

The goal is simple:

> Open an empty/site-specific Codex project, paste one starter prompt, and let Codex create the project files, connect the workflow, verify Bricks skills, and build the site knowledge base for you.

Bricks AI abilities are currently experimental. First-time setup and testing is safest on local/staging environments.

Official Bricks documentation:  
https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/

---

# Magyar

## Gyors kezdés

### 1. Nyiss egy külön Codex projectet az adott webhelyhez

Egy webhely = egy Codex project.

Nem kell előre kézzel létrehoznod:

- `AGENTS.md`
- `docs/bricks/`
- audit fájlokat
- template mappákat
- project dokumentációt

Ezeket a Codex hozza létre és tölti ki.

### 2. Másold ezt egy új Codex chatbe

```text
Bootstrap the CURRENT Codex project for a WordPress + Bricks Builder site using this starter repository:

https://github.com/eliquame/bricks-codex-mcp-starter

Read START-HERE.md from that repository and execute it completely.

Do the project initialization yourself. Do not ask me to manually create AGENTS.md, docs/bricks folders, starter files, or audit files.

Never ask me to paste WordPress Application Passwords, API keys, tokens, or other credentials into chat. Keep credential-bearing configuration local.

Pause only when I genuinely need to perform a WordPress admin UI action, paste a secret locally, authorize GitHub access, restart Codex, or grant a missing permission.
```

Ennyi a normál indulás.

A Codex ezután a repositoryból beolvassa a **[START-HERE.md](START-HERE.md)** folyamatot, és maga végzi el a lehető legtöbb lépést.

## Mit csinál meg helyetted?

A one-prompt bootstrap:

1. beolvassa ezt a starter repositoryt;
2. létrehozza vagy összevonja a projekt `AGENTS.md` fájlját;
3. létrehozza a `docs/bricks/` knowledge base alapját;
4. ellenőrzi, hogy a Bricks MCP kapcsolat már működik-e;
5. ha nem, végigvezet a Bricks admin szükséges lépésein;
6. megkeresi a Codex `config.toml` fájlját;
7. **nem kéri, hogy credentialt másolj a chatbe**;
8. ellenőrzi az MCP kapcsolatot read-only módon;
9. telepíti vagy ellenőrzi a Bricks skills csomagot;
10. ha új chat vagy restart kell, elmenti a bootstrap állapotát a projektbe, hogy onnan folytatható legyen;
11. azonosítja az adott site-ot és a hozzá tartozó MCP servert;
12. lefuttatja a teljes read-only bootstrap auditot;
13. feltölti a projekt dokumentációját valós site-adatokkal;
14. finomítja az `AGENTS.md` project profile-ját.

## Amit továbbra is neked kell megtenned

Biztonsági okból néhány lépést nem érdemes automatizálni.

A Codex megáll és pontosan megmondja, mit kell tenned, ha például:

- a WordPress adminban be kell kapcsolni a Bricks abilities funkciót;
- telepíteni/aktiválni kell a WordPress MCP Adaptert;
- Application Passwordöt kell generálni;
- a secretet tartalmazó Bricks config blokkot lokálisan kell beilleszteni;
- GitHub hozzáférést kell engedélyezni;
- új chat / Codex restart kell;
- hiányzik egy WordPress/Bricks jogosultság.

Ha új chat vagy restart kell, a folyamat előtte elmenti az állapotot a `docs/bricks/00-bootstrap-status.md` fájlba. Az új chatben elég ezt írni:

```text
Continue the Bricks/Codex bootstrap from docs/bricks/00-bootstrap-status.md
```

## Credentialek

A starter alapelve:

> **Secret ne kerüljön chatbe.**

A Bricks `Copy a prompt` opciója tartalmazhatja a WordPress usernevet és Application Passwordöt.

Ezért a starter alapértelmezett útja:

```text
Bricks → AI → Configuration → Codex → Paste config
```

A credentialt tartalmazó blokk a helyi Codex configba kerül.

Windows:

```text
%USERPROFILE%\.codex\config.toml
```

macOS / Linux:

```text
~/.codex/config.toml
```

A Codex segíthet megnyitni és helyesen merge-elni a fájlt, de a secretet nem kell elküldened neki chatüzenetben.

## Bricks skills

Ha még nincsenek telepítve, a bootstrap ezt is ellenőrzi és végigviszi.

WordPress:

```text
Bricks → AI → Skills
```

<img src="assets/bricks-ai-skills.webp" alt="Bricks AI Skills setup screen" width="820">

A Bricks skills kliensoldali munkafolyamat-utasítások. Nem adnak új WordPress jogosultságot.

Skills repository:  
https://github.com/codeerhq/bricks-skills

## Mit tanul meg a bootstrap audit?

A bootstrap audit nem csak a Bricks element tree-t nézi.

Feltérképezi, ahol releváns:

- Bricks Theme Styles;
- global classes;
- global variables;
- breakpoints;
- components;
- templates;
- pages;
- dynamic data;
- query-k;
- plugin architektúra;
- CPT-k és taxonómiák;
- ACF / JetEngine / ACPT / Meta Box és más adatforrások;
- WooCommerce;
- külső CSS/design frameworkök;
- publikus frontend;
- responsive viselkedés;
- vizuális layout- és designminták.

Ezekből helyi, site-specifikus knowledge base készül a Codex projectben.

## Meglévő site vagy szűz site?

A bootstrap automatikusan besorolja:

- **ESTABLISHED**
- **PARTIAL / IN PROGRESS**
- **GREENFIELD**

### Meglévő site

A Codex böngészőben is feltérképezi a valódi publikus oldalakat, így nem csak azt tudja, milyen classok vannak, hanem azt is, hogyan néz ki ténylegesen a site.

### Szűz site

Nem talál ki nem létező vizuális szabályokat.

Ha még nincs kialakult design system, ezt külön jelzi, és a későbbi design-system creation/seed feladatból indulunk.

## Design system ownership

A design system forrása lehet:

- **BRICKS NATIVE**
- **EXTERNAL FRAMEWORK**
- **HYBRID**
- **CUSTOM CODE DRIVEN**
- **UNKNOWN / UNDEFINED**

Ez fontos például Core Framework vagy más teljes CSS framework esetén.

A Codexnek meg kell értenie, hogy egy class vagy variable:

- Bricks-owned;
- framework/plugin-owned;
- theme-owned;
- custom-code-owned;
- vagy page-local.

Így nem hoz létre felesleges Bricks duplikátumokat egy külső framework mellé.

## WooCommerce

A WooCommerce státuszát minden bootstrap audit ellenőrzi.

Ha nincs telepítve, nincs mély Woo audit.

Ha aktív, kötelezően bekerül az architektúra és frontend vizsgálatába.

Privát order/customer adat nem kerülhet a project dokumentációba.

## Több site

Egy globális Codex `config.toml` több MCP servert is tartalmazhat.

Minden site-hoz ajánlott:

- külön MCP server név;
- külön Codex project;
- külön `AGENTS.md`;
- külön `docs/bricks/` knowledge base.

A project `AGENTS.md` rögzíti, melyik MCP server használható az adott projectben.

## Ha kézzel akarod beállítani

A manuális dokumentáció megmarad referenciának:

- [Bricks MCP setup](docs/setup-bricks-mcp.md)
- [Codex project setup](docs/setup-codex.md)
- [Security](docs/security.md)
- [Workflow](docs/workflow.md)
- [Design-system lifecycle](docs/design-system-lifecycle.md)

## Repository térkép

```text
START-HERE.md
    one-prompt project initialization + MCP + skills + bootstrap orchestration

project-starter/AGENTS.md
    canonical default project policy used by Codex

prompts/00-full-site-bootstrap-audit.md
    full read-only site discovery and documentation

prompts/10-design-system-change-workflow.md
    controlled global design-system changes

prompts/90-agents-maintenance-and-sync.md
    later AGENTS synchronization after material changes

templates/documentation-structure.md
    reference for the generated knowledge base
```

---

# English

## Quick start

### 1. Open one Codex project for the target site

One website = one Codex project.

You do **not** need to manually create `AGENTS.md`, `docs/bricks/`, audit files, or starter folders.

Codex initializes them for you.

### 2. Paste this into a new Codex chat

```text
Bootstrap the CURRENT Codex project for a WordPress + Bricks Builder site using this starter repository:

https://github.com/eliquame/bricks-codex-mcp-starter

Read START-HERE.md from that repository and execute it completely.

Do the project initialization yourself. Do not ask me to manually create AGENTS.md, docs/bricks folders, starter files, or audit files.

Never ask me to paste WordPress Application Passwords, API keys, tokens, or other credentials into chat. Keep credential-bearing configuration local.

Pause only when I genuinely need to perform a WordPress admin UI action, paste a secret locally, authorize GitHub access, restart Codex, or grant a missing permission.
```

Codex then reads **[START-HERE.md](START-HERE.md)** and performs the workflow itself as far as its local tools allow.

## What the bootstrap handles

It can:

- initialize/merge project-root `AGENTS.md`;
- initialize `docs/bricks/`;
- detect an existing Bricks MCP connection;
- guide the WordPress-side MCP setup when needed;
- locate Codex `config.toml`;
- keep secrets out of chat;
- verify Bricks MCP read-only diagnostics;
- install/verify Bricks skills;
- identify the site's assigned MCP server;
- run the full read-only site bootstrap audit;
- build the site-specific local knowledge base.

## Manual actions are only requested when necessary

Codex may pause for:

- WordPress admin UI actions;
- generating an Application Password;
- pasting credential-bearing config locally;
- GitHub authorization;
- Codex restart/new chat;
- missing WordPress/Bricks permissions.

If a new chat or restart is required, the workflow first saves progress to `docs/bricks/00-bootstrap-status.md`. In the new chat, simply say:

```text
Continue the Bricks/Codex bootstrap from docs/bricks/00-bootstrap-status.md
```

## Security model

Do not paste or commit:

- WordPress Application Passwords;
- normal WordPress passwords;
- Codex `config.toml`;
- API keys/tokens;
- hosting/database credentials.

Prefer Bricks **Paste config** over **Copy a prompt** so credential-bearing configuration stays local.

## Site discovery

The bootstrap classifies the project as:

- **ESTABLISHED**
- **PARTIAL / IN PROGRESS**
- **GREENFIELD**

Established sites receive browser/frontend visual auditing.

Greenfield sites do not get invented visual rules.

The bootstrap also determines design-system authority:

- **BRICKS NATIVE**
- **EXTERNAL FRAMEWORK**
- **HYBRID**
- **CUSTOM CODE DRIVEN**
- **UNKNOWN / UNDEFINED**

WooCommerce is always detected and deeply audited only when relevant/active.

## References

- Bricks AI Abilities and Skills: https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/
- Bricks skills: https://github.com/codeerhq/bricks-skills

