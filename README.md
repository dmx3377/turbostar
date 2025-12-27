<picture id="banner">
  <source media="(prefers-color-scheme: dark)" srcset="https://cdn.dmx3377.uk/turbostar-banner-light.png">
  <source media="(prefers-color-scheme: light)" srcset="https://cdn.dmx3377.uk/turbostar-banner.png">
  <img alt="" src="https://cdn.dmx3377.uk/turbostar-banner.png">
</picture>

Turbostar is an asynchronous CLI tool designed to manage complex development environments where multiple languages (Python, JavaScript, Lua) must run in harmony. It handles process lifecycle, output aggregation, and dependency graphing.

## Features

* **Polyglot Support:** Run Python scripts, Node.js servers, and Lua logic simultaneously.
* **Dependency Graphing:** Configure services to wait for "Ready" signals from other services before starting.
* **Unified Output:** Aggregates `stdout` and `stderr` from all children into a single, color-coded terminal stream.

## Quick Start

### Prerequisites
* Python 3.8+
* Node.js (optional, for plugins)
* Lua (optional, for plugins)

### Installation
Clone the repository:
```bash
git clone https://github.com/dmx3377/turbostar.git
cd turbostar
```

## Usage
1. Define your processes in `manifest.json`:
```json
{
  "services": [
    {
      "name": "BACKEND",
      "command": "python backend.py",
      "ready_signal": "Server Running"
    },
    {
      "name": "FRONTEND",
      "command": "npm start",
      "depends_on": "BACKEND"
    }
  ]
}
```
2. Begin the script by running:
`python turbostar.py`

## Configuration
| Field        | Description                                                     |
|--------------|-----------------------------------------------------------------|
| `name`         | The display name in the logs.                                    |
| `command`      | The shell command to execute.                                    |
| `color`        | ANSI colour code for differentiating the logs.                          |
| `ready_signal` | String to look for in `stdout` to mark service as *READY*.            |
| `depends_on`   | Name of the service this process must wait for.             |

## License
This project is licensed under the BSD 3-Clause License, see the LICENSE file for further details.

