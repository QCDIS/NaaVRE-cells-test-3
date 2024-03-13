# NaaVRE-cells

## Setup

### Cells repository

Repositories using this template publish cells to the Github image registry (ghcr.io) by default, using built-in authentication.

To use another registry, the following following actions secrets and variables must be set in the repository settings:

- variable `REGISTRY_NAME` (eg. `https://index.docker.io/v1/` for Docker Hub)
- secret `REGISTRY_PASSWORD`
- secret `REGISTRY_USERNAME`

If using self-hosted runners, the following variables must be set (see [QCDIS/choose-action-runner](https://github.com/QCDIS/choose-action-runner)):

- variable `PREFERRED_ACTIONS_RUNNER`
- secret `RUNNER_ACCESS_TOKEN`

### NaaVRE deployment

Set the following environment variables in the NaaVRE deployment:

- `CELL_GITHUB=https://github.com/this-user/this-repo`
- `CELL_GITHUB_TOKEN=github_pat_...` (Permissions: read access metadata; read
  and write access actions and code on the current repo)

If using another image image registry (e.g. Docker Hub):

- `REGISTRY_URL=https://hub.docker.com/u/my-user`

