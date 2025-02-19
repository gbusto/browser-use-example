# Overview

Simple script to use `browser-use` which is an open source version of OpenAI's operator.

It's currently setup to use Gemini 2.0 flash which is probably the best blend of intelligence, speed, and low cost. But you can use GPT 4o mini or something else too.

## Setup and use

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
export $(cat .env)
```

Then edit the `.env` file with your Google API key (or OpenAI API key).

Then edit the `task` in `quickstart.py`, and run the script:

```bash
python quickstart.py
```

`agent.run()` returns an `AgentHistoryList` object. Read the implementation [here](https://github.com/browser-use/browser-use/blob/main/browser_use/agent/views.py#L180).

That should be it!
