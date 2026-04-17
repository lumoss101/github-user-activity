# GitHub Activity Viewer

A simple command-line tool to display the latest public GitHub activity for any user, with emoji icons and color-coded output powered by [`rich`](https://github.com/Textualize/rich).

## Features

- Fetches up to 20 recent public events for any GitHub user
- Displays activity with descriptive emoji icons per event type
- Color-highlighted output using `rich`
- Graceful error handling for network issues, timeouts, and HTTP errors

## Requirements

- Python 3.7+
- [`requests`](https://pypi.org/project/requests/)
- [`rich`](https://pypi.org/project/rich/)

## Installation

1. **Clone or download** this repository.

2. **Install dependencies:**

   ```bash
   pip install requests rich
   ```

## Usage

```bash
python script.py <github-username>
```

**Example:**

```bash
python script.py torvalds
```

**Sample output:**

```
Latest events for torvalds:
1. 🚀 pushed to torvalds/linux
2. 🐛 created issue #1234
3. 💬 commented on issue #1230
4. ⭐ starred git/git
```

## Supported Event Types

| Icon | Event |
|------|-------|
| 💬 | Issue comment |
| 🚀 | Push |
| 🐛 | Issue opened |
| ⭐ | Repository starred |
| 🔀 | Pull request |
| 👀 | Pull request review |
| 🗨️ | Pull request review comment |
| ✨ | Branch or tag created |

## Notes

- Uses the [GitHub Events API](https://docs.github.com/en/rest/activity/events), which only returns **public** events.
- The API returns a maximum of **300 events** and up to **90 days** of history. This script fetches the most recent 20.
- No authentication is required, but unauthenticated requests are limited to **60 requests per hour** by GitHub.

## License

MIT
