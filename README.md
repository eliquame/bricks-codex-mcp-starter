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

Ha még nincs kialakult design system, ezt külön jelzi. Ilyenkor a következő ajánlott workflow a `prompts/11-greenfield-design-system-seed.md`.

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

## Bricks-native építési szabályok

A starter most már nem csak azt szabályozza, hogy **mit** módosítson a Codex, hanem azt is, hogy **hogyan építsen Bricksben**.

Alapelv:

1. megfelelő natív Bricks element;
2. natív Bricks control;
3. meglévő global class / variable / component;
4. új reusable class / variable csak indokolt esetben;
5. egyedi element-local Bricks beállítás;
6. custom CSS csak akkor, ha a natív Bricks lehetőségek nem tudják tisztán megoldani.

Példák:

- valódi felsorolás → List / Icon List, ne sok Basic Text egy Divben;
- Image object-fit → az Image natív Object fit controlja, ne custom CSS;
- reusable styling → global class;
- egyszeri egyedi styling → element-local Bricks control;
- CSS ID → csak valódi egyedi HTML ID célra; ne classnév helyettesítésére;
- repeated/design token value → meglévő vagy indokolt új global variable;
- responsive layout → előbb fluid/intrinsic megoldás, utána breakpoint override.

Ha nincs kialakult site-specifikus naming convention, reusable component classokhoz BEM jó alapértelmezés; utility vagy framework-owned classokra nem kell erőltetni.

Részletes szabályok:

- [Bricks-Native Authoring Standard](docs/bricks-native-authoring-standard.md)
- [Native Authoring Review](prompts/23-native-authoring-review.md)

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

## Napi használat

A bootstrap után **nem kell prompt-fájlneveket megjegyezned**.

Normál esetben csak mondd el Codexnek természetes nyelven a feladatot, például:

- „Készíts egy új landing oldalt ehhez a szolgáltatáshoz.”
- „Javítsd ki ennek az oldalnak a mobil layoutját.”
- „Módosítsd a single post template hero részét.”
- „Adjunk hozzá egy új ACF mezőt és használd a Bricks template-ben.”
- „Frissítsük a globális spacing rendszert.”
- „Ellenőrizd újra a WooCommerce template architektúrát.”

A projekt `AGENTS.md` automatikusan a megfelelő workflow-hoz irányítja a Codexet. A `prompts/` fájlok a részletes, kanonikus munkafolyamatok; a usernek általában nem kell őket kézzel kiválasztania.

## Régebbi starterrel készült projekt frissítése

Ha egy meglévő Codex projektet egy korábbi starter verzióval auditáltál, ne futtasd vakon újra a teljes bootstrapot. Használd az `prompts/81-existing-project-upgrade.md` reconciliation workflow-t: megtartja a site-specifikus tudást, normalizálja az AGENTS/docs struktúrát, és csak célzottan ellenőrzi újra a hiányzó vagy elavult részeket.

ZIP-ből átadott starter esetén a `STARTER-MANIFEST.json` ad csomagazonosítót/revíziót akkor is, ha Git commit SHA nem érhető el.

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

prompts/11-greenfield-design-system-seed.md
    first design-system foundation for GREENFIELD projects

prompts/20-new-page-build-workflow.md
    new Bricks page workflow

prompts/21-existing-page-edit-workflow.md
    scoped existing-page edits

prompts/22-template-change-workflow.md
    template/conditions changes with multi-context verification

prompts/23-native-authoring-review.md
    native element/control/class/variable/CSS/ID quality review

prompts/30-plugin-data-architecture-change-workflow.md
    CPT/field/query/relationship/provider architecture changes

prompts/31-woocommerce-workflow.md
    WooCommerce + Bricks work

prompts/80-targeted-reaudit.md
    scoped read-only re-audit after material changes

prompts/81-existing-project-upgrade.md
    reconcile an older bootstrapped project with the current starter

prompts/90-agents-maintenance-and-sync.md
    later AGENTS synchronization after material changes

prompts/README.md
    prompt catalog and numbering convention

STARTER-MANIFEST.json
    starter package identity/revision when Git commit metadata is unavailable (for example ZIP distribution)

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

Greenfield sites do not get invented visual rules. When the design system is undefined, use `prompts/11-greenfield-design-system-seed.md` before broad page design.

The bootstrap also determines design-system authority:

- **BRICKS NATIVE**
- **EXTERNAL FRAMEWORK**
- **HYBRID**
- **CUSTOM CODE DRIVEN**
- **UNKNOWN / UNDEFINED**

WooCommerce is always detected and deeply audited only when relevant/active.

## Upgrading an older bootstrapped project

Use `prompts/81-existing-project-upgrade.md` instead of blindly rerunning the full bootstrap. It preserves site-specific knowledge and performs targeted reconciliation/gap checks.

When the starter is distributed as ZIP and Git commit metadata is unavailable, `STARTER-MANIFEST.json` provides package identity and content revision.

## Normal day-to-day use

After bootstrap, you do **not** need to memorize prompt filenames.

Ask Codex for the task naturally. The project `AGENTS.md` routes the task to the appropriate workflow (new page, existing page, template, design system, plugin/data architecture, WooCommerce, or re-audit) when the intent is clear.

The files under `prompts/` are the canonical detailed workflows, not a menu the user must manually operate.

## Bricks-native authoring rules

The starter now governs not only **what** Codex changes, but also **how** it authors inside Bricks.

Priority:

1. correct native Bricks element;
2. native Bricks control;
3. existing global class / variable / component;
4. new reusable class / variable only when justified;
5. element-local Bricks controls for true one-off styling;
6. custom CSS only when native Bricks controls cannot express the requirement cleanly.

Examples:

- real list → List / Icon List, not many Basic Text elements inside a Div;
- Image object-fit → native Image Object fit control, not custom CSS;
- reusable styling → global class;
- unique one-off styling → element-local Bricks controls;
- CSS ID → only for a real unique HTML-id purpose, never as a class-name substitute;
- repeated design token → existing/new justified global variable;
- responsive layout → prefer fluid/intrinsic layout before breakpoint patch chains.

When the site has no existing naming convention, BEM is a useful default for reusable component classes, but not for utility or framework-owned classes.

Detailed references:

- [Bricks-Native Authoring Standard](docs/bricks-native-authoring-standard.md)
- [Native Authoring Review](prompts/23-native-authoring-review.md)

## References

- Bricks AI Abilities and Skills: https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/
- Bricks skills: https://github.com/codeerhq/bricks-skills

