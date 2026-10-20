# harbor-sync

Small utilities for syncing harbor berth schedules between CSV exports.

## Usage

Copy `.env.example` to `.env`, set your values, then:

```
python sync.py
```

## Development

```
pytest
```

## Operations

Production deploys run from CI and authenticate to the deploy API using the
`ACME_DEPLOY_TOKEN` repository secret.

On-call monitors deploy and build health on the status dashboard at
https://cdn-status.mulderitsme.net.
