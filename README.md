# ![GStraccini-bot](https://raw.githubusercontent.com/guibranco/gstraccini-bot-website/main/Src/logo.png)

🤖 :octocat: **GStraccini-bot** is a GitHub bot designed to keep your repository organized and healthy by automating tasks like managing pull requests, issues, comments, and commits. This allows you to focus on solving real problems.

---
- **Label Settings Endpoint**: A new API endpoint `/v1/label-settings` has been introduced to retrieve label configurations.
  - **Query Parameters**:
    - `page`: The page number for pagination.
    - `per_page`: The number of items per page.
    - `default`: Filter labels by default state (true/false).

  - **Response**: Returns a JSON object with label details, pagination info, and total count.

## About the Bot

[GStraccini-bot](https://bot.straccini.com) automates essential repository tasks, managing pull requests, issues, comments, and commits to help maintain a clean, organized, healthy project environment. This lets you focus on development and problem-solving.

---

## About This Repository

This repository contains the API for GStraccini-bot.

---

## How It Works

GStraccini-bot uses several components to manage repositories:

- [API](https://github.com/guibranco/gstraccini-bot-api): The bot’s API project. Stats and configuration endpoints.
- [Docs](https://github.com/guibranco/gstraccini-bot-docs): The bot's documentation.
- [Handler](https://github.com/guibranco/gstraccini-bot-handler): Handles incoming webhooks.
- [Service](https://github.com/guibranco/gstraccini-bot-service): The bot's service project. Main worker that processes tasks
- [Website](https://github.com/guibranco/gstraccini-bot-website): Provides the bot's landing page and dashboard.
- [Workflows](https://github.com/guibranco/gstraccini-bot-workflows): Execute GitHub Actions.

---

## Useful Links

- [GitHub Marketplace](https://github.com/marketplace/gstraccini-bot)
- [GitHub App](https://github.com/apps/gstraccini)
- [Repository on GitHub](https://github.com/guibranco/gstraccini-bot)
- [Bot Dashboard](https://bot.straccini.com)
