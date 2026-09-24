# Bricks MCP Setup

This guide intentionally avoids site-specific credentials.

## On the WordPress / Bricks site

1. Open **Bricks > AI**.
2. Enable **Bricks abilities**.
3. Install and activate the **WordPress MCP Adapter** when prompted.
4. Create a dedicated WordPress user for the AI client.
5. Assign only the Bricks / WordPress permissions required for the current workflow.
6. Generate a WordPress Application Password for that user.
7. Select **Codex** as the client and copy the generated MCP configuration block.

## In Codex on Windows

The global Codex configuration is normally located at:

```text
%USERPROFILE%\.codex\config.toml
```

Append the site's generated MCP block as a new section. Do not overwrite unrelated existing configuration.

Example shape only:

```toml
[mcp_servers.example-site]
command = "npx"
args = ["-y", "@automattic/mcp-wordpress-remote@latest"]

[mcp_servers.example-site.env]
WP_API_URL = "https://example.com/wp-json/mcp/mcp-adapter-default-server"
WP_API_USERNAME = "dedicated-ai-user"
WP_API_PASSWORD = "LOCAL-APPLICATION-PASSWORD"
```

Never commit a real configuration block containing credentials to Git.

## Verify

Restart Codex or open a fresh session as required, then perform read-only discovery.

Verify that Bricks tools / abilities are available before attempting any writes.

## Multiple sites

Codex can have multiple MCP server blocks in the same global `config.toml`.

Use a unique server name per site and add a project-level `AGENTS.md` rule that limits each project to its intended MCP server.
