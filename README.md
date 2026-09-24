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
- tartós, site-specifikus tudásbázist épít, és a projekt gyökerében lévő alapértelmezett `AGENTS.md`-t ellenőrzött site-specifikus adatokkal egészíti ki.

### Fontos elv

Ez a repository **nem egy konkrét webhely dokumentációja**. A benne lévő promptok és starter fájlok site-agnosztikusak.

A **kanonikus kezdő AGENTS fájl** a `project-starter/AGENTS.md`. Ezt kell minden új site projekt gyökerébe bemásolni. A `templates/` mappa dokumentációs sablonokat tartalmaz; nem ott van az aktív projektutasítás.

### Webhely-érettségi módok

A bootstrap audit nem feltételezi, hogy a webhely már kész vagy publikus. Először besorolja a projektet:

- **ESTABLISHED** — működő, tartalmilag és vizuálisan kialakult webhely. A teljes publikus frontend- és vizuális audit kötelező.
- **PARTIAL / IN PROGRESS** — vannak használható oldalak vagy designminták, de a rendszer még nem teljes. A Codex csak a ténylegesen megfigyelt mintákat tekintheti szabálynak.
- **GREENFIELD** — szűz vagy lényegében üres WordPress / Bricks projekt. Ilyenkor nincs értelme nem létező vizuális szabályokat „kitalálni” a bootstrap auditban; a vizuális audit korlátozott vagy N/A, és a design system létrehozása külön, jóváhagyott munkafolyamat.

### Design system forrása és tulajdonjoga

A design system nem feltétlenül Bricks Theme Stylesból származik. A bootstrap auditnak meg kell állapítania, hogy a rendszer:

- **BRICKS NATIVE**
- **EXTERNAL FRAMEWORK**
- **HYBRID**
- **CUSTOM CODE DRIVEN**
- **UNDEFINED / PARTIAL**

Például ha egy CSS framework plugin — például Core Framework vagy más hasonló rendszer — adja a tokeneket, global classokat és variable-öket, akkor ezeket framework-owned erőforrásként kell dokumentálni. A Codex ne hozzon létre Bricksben felesleges duplikátumokat, és ne kezelje a framework által birtokolt erőforrásokat Bricks-native elemként.

### Design system változások

Theme Styles, global classok, variable-ök vagy külső framework tokenek módosítása **globális hatású változásnak** számít. Ilyenkor célzott impact audit szükséges:

1. aktuális állapot és ownership ellenőrzése;
2. érintett oldalak/template-ek azonosítása;
3. módosítás;
4. persisted state visszaolvasása;
5. reprezentatív frontend/regression ellenőrzés több viewporton;
6. site dokumentáció és snapshotok frissítése.

A részletes szabályokat a `docs/design-system-lifecycle.md`, a végrehajtási promptot pedig a `prompts/02-design-system-change-workflow.md` tartalmazza.

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
├── project-starter/
│   ├── AGENTS.md
│   ├── README.md
│   └── docs/bricks/README.md
├── prompts/
│   ├── 00-full-site-bootstrap-audit.md
│   ├── 02-design-system-change-workflow.md
│   └── 90-agents-maintenance-and-sync.md
├── templates/
│   ├── audit-progress.template.md
│   └── documentation-structure.md
└── docs/
    ├── setup-bricks-mcp.md
    ├── setup-codex.md
    ├── security.md
    ├── workflow.md
    └── design-system-lifecycle.md
```

### Kezdés

1. Kösd össze az adott WordPress / Bricks webhelyet a Codexszel MCP-n keresztül.
2. Telepítsd a Bricks skills csomagot a Codexhez.
3. Hozz létre külön helyi Codex projektmappát a webhelynek.
4. **Még az első thread előtt** másold a `project-starter/` tartalmát a projekt gyökerébe. Így a Codex már az első feladattól egy részletes, általános `AGENTS.md` szabályrendszerrel indul.
5. Futtasd a `prompts/00-full-site-bootstrap-audit.md` promptot egy új Codex threadben. Az audit nem nulláról ír új AGENTS fájlt: kitölti/refine-olja a projektprofilt és létrehozza a site-specifikus `docs/bricks/` tudásbázist.
6. Az audit után csökkentsd az MCP user jogosultságait a napi munkához szükséges minimumra.
7. A későbbi threadek mindig az aktív projektgyökér `AGENTS.md` és `docs/bricks/` tudásbázisból induljanak, de írás előtt ellenőrizzék újra az érintett live állapotot.
8. Az `AGENTS.md` későbbi karbantartására a `prompts/90-agents-maintenance-and-sync.md` használható.

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
- create a durable site-specific knowledge base and refine the default project-root `AGENTS.md` with verified site-specific facts.

### Core principle

This repository is **not site-specific documentation**. All prompts and starter files here are site-agnostic.

The **canonical starting AGENTS file** is `project-starter/AGENTS.md`. Copy it to the root of every new site project. The `templates/` directory is for documentation templates; it is not the active project instruction location.

### Site maturity modes

The bootstrap audit does not assume that the site is already complete or publicly established. It first classifies the project:

- **ESTABLISHED** — a functioning site with meaningful content and visual patterns. Full public frontend and visual auditing is required.
- **PARTIAL / IN PROGRESS** — some usable pages or design patterns exist, but the system is incomplete. Codex may only promote actually observed patterns to rules.
- **GREENFIELD** — a blank or effectively empty WordPress / Bricks project. The bootstrap audit must not invent visual rules from missing evidence; frontend visual auditing is limited or N/A, and design-system creation becomes a separate approved workflow.

### Design-system source and ownership

The design system does not have to originate from Bricks Theme Styles. The bootstrap audit must determine whether the project is:

- **BRICKS NATIVE**
- **EXTERNAL FRAMEWORK**
- **HYBRID**
- **CUSTOM CODE DRIVEN**
- **UNDEFINED / PARTIAL**

If a CSS framework plugin — for example Core Framework or an equivalent system — owns tokens, global classes, and variables, those resources must be documented as framework-owned. Codex should not create redundant Bricks-native duplicates or treat provider-owned resources as if Bricks owned them.

### Design-system changes

Changes to Theme Styles, global classes, global variables, or external framework tokens are **global-impact changes**. They require a targeted impact workflow:

1. verify the current state and ownership;
2. identify dependent pages/templates;
3. apply the change;
4. re-read persisted state;
5. perform representative frontend regression checks at relevant viewports;
6. refresh project documentation and snapshots.

See `docs/design-system-lifecycle.md` and `prompts/02-design-system-change-workflow.md`.

Each real website should have its own separate Codex project containing its generated `AGENTS.md` and `docs/bricks/` knowledge base.

### Repository structure

```text
bricks-codex-mcp-starter/
├── README.md
├── CHANGELOG.md
├── .gitignore
├── project-starter/
│   ├── AGENTS.md
│   ├── README.md
│   └── docs/bricks/README.md
├── prompts/
│   ├── 00-full-site-bootstrap-audit.md
│   ├── 02-design-system-change-workflow.md
│   └── 90-agents-maintenance-and-sync.md
├── templates/
│   ├── audit-progress.template.md
│   └── documentation-structure.md
└── docs/
    ├── setup-bricks-mcp.md
    ├── setup-codex.md
    ├── security.md
    ├── workflow.md
    └── design-system-lifecycle.md
```

### Getting started

1. Connect the target WordPress / Bricks site to Codex through MCP.
2. Install the Bricks skills for Codex.
3. Create a dedicated local Codex project folder for the target site.
4. **Before the first thread**, copy the contents of `project-starter/` into the project root. This gives Codex the full baseline `AGENTS.md` policy from the first task.
5. Run `prompts/00-full-site-bootstrap-audit.md` in a new Codex thread. The audit refines the existing AGENTS project profile and builds the site-specific `docs/bricks/` knowledge base.
6. After the bootstrap audit, reduce the MCP user's permissions to the minimum required for normal work.
7. Future threads should use the active project-root `AGENTS.md` and `docs/bricks/` knowledge base, while re-reading affected live resources before writes.
8. Use `prompts/90-agents-maintenance-and-sync.md` later when the active AGENTS file needs synchronization after material project changes.

### Security

**Never commit WordPress Application Passwords, Codex `config.toml`, API keys, passwords, tokens, or other credentials to this repository.**

Private repository visibility is not a substitute for proper secret hygiene.

---

Status: early working draft / evolving workflow.
