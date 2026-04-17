import sys
import requests
from rich import print as rich_print

EVENT_ICONS = {
    'IssueCommentEvent': ':speech_balloon:',
    'PushEvent': ':rocket:',
    'IssuesEvent': ':bug:',
    'WatchEvent': ':star:',
    'PullRequestEvent': ':twisted_rightwards_arrows:',
    'PullRequestReviewEvent': ':eyes:',
    'PullRequestReviewCommentEvent': ':left_speech_bubble:',
    'CreateEvent': ':sparkles:',
}

def get_latest_events(username, limit=20):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        rich_print("[red]Network error. Check your connection.[/red]")
        return
    except requests.exceptions.Timeout:
        rich_print("[red]Request timed out.[/red]")
        return
    except requests.exceptions.HTTPError as e:
        rich_print(f"[red]HTTP error: {e}[/red]")
        return

    events = response.json()[:limit]
    rich_print(f"Latest events for [bold green]{username}[/bold green]:")

    for i, event in enumerate(events, start=1):
        icon = EVENT_ICONS.get(event['type'], ':smiley:')
        payload = event.get('payload', {})

        if event['type'] == 'IssueCommentEvent':
            rich_print(f"{i}. {icon} commented on issue #{payload['issue']['number']}")
        elif event['type'] == 'PushEvent':
            rich_print(f"{i}. {icon} pushed to {event['repo']['name']}")
        elif event['type'] == 'IssuesEvent':
            rich_print(f"{i}. {icon} created issue #{payload['issue']['number']}")
        elif event['type'] == 'WatchEvent':
            rich_print(f"{i}. {icon} starred {event['repo']['name']}")
        elif event['type'] == 'PullRequestEvent':
            rich_print(f"{i}. {icon} created PR #{payload['pull_request']['number']}")
        elif event['type'] == 'PullRequestReviewEvent':
            rich_print(f"{i}. {icon} reviewed PR #{payload['pull_request']['number']}")
        elif event['type'] == 'PullRequestReviewCommentEvent':
            rich_print(f"{i}. {icon} commented on PR #{payload['pull_request']['number']}")
        elif event['type'] == 'CreateEvent':
            ref = payload.get('ref') or '(default branch)'
            rich_print(f"{i}. {icon} created {payload['ref_type']} {ref}")
        else:
            rich_print(f"{i}. {icon} {event['type']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_latest_events(sys.argv[1])
    else:
        rich_print("Type: python script.py <github-username>")