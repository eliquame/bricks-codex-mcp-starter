# Security Guidance

## Principle of least privilege

Use a dedicated WordPress user for Codex / MCP access.

A bootstrap audit may temporarily require elevated privileges to inspect the full environment. After the audit, reduce the account to the minimum WordPress and Bricks capabilities required for normal work.

Do not use an administrator account for routine editing unless the task genuinely requires it.

## Credentials

Never store or commit:

- WordPress Application Passwords
- normal WordPress passwords
- API keys
- OAuth secrets
- Codex global `config.toml`
- MCP credentials
- hosting credentials
- database credentials

Credentials belong in the local Codex configuration or another appropriate secret store, not in this repository.

## Runtime trust model

Future project instructions should distinguish between:

- live MCP state;
- cached local documentation;
- rendered frontend state;
- inaccessible state caused by current permissions.

An inaccessible resource must not be treated as nonexistent.

## PHP and code execution

PHP execution must remain disabled unless explicitly required and authorized for a trusted development environment.

Do not enable elevated execution capabilities simply to make an audit easier.

## Destructive operations

Bootstrap audits are read-only for the remote WordPress / Bricks site.

Do not:

- delete pages, posts, templates, classes, variables, components, media, fields, CPTs, or taxonomies;
- install, update, activate, deactivate, or delete plugins;
- change WooCommerce products, orders, customers, stock, pricing, shipping, tax, or payment settings;
- modify plugin/theme/server files.

Local project documentation may be created and updated.
