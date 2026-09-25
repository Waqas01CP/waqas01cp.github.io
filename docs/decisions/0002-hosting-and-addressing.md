---
status: accepted
topic: hosting
description: Where the site lives and how it is reached. User site at waqas01cp.github.io, public repository, no custom domain yet, email contact, freelance and contract openness stated. Read before any hosting, URL or contact work.
date: 2026-09-23
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0002: Public user site at waqas01cp.github.io, no custom domain yet

## Context and Problem Statement

The site needs an address, a host and a contact route before any code exists,
and each choice constrains the others.

GitHub Pages is available in public repositories with GitHub Free and GitHub
Free for organizations, and in public and private repositories with GitHub
Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
Read from GitHub's own documentation 2026-09-23. A private repository plus
Pages therefore means paying for Pro, against the standing free-by-default
constraint.

A repository is public or private as a whole. One file cannot be private
inside a public one, and the architecture chat's ledger names the operator's
blockers and the chat's own errors.

GitHub Pages offers one user site per account, from a repository that must be
named `<owner>.github.io` and served at the domain root. A project site is
served from a subpath instead. The root slot at `waqas01cp.github.io`
returned HTTP 404 on 2026-09-23, so it is unused.

A custom domain is the only element of the site with no free option, and it
recurs yearly.

The operator is seeking employment and is also open to freelance and contract
work. GitHub's usage limits state that Pages is not intended for or allowed
to be used as a free web-hosting service to run your online business,
e-commerce site, or any other website that is primarily directed at either
facilitating commercial transactions or providing commercial software as a
service.

## Decision Drivers

- Free by default. Any spend is discussed before it is committed. Standing
  constraint, Tooling and Cost Constraints.
- A public repository of decision records and research is itself verifiable
  evidence of the engineering practice the site claims. Marlow and Dabbish,
  CSCW 2013: hiring readers trust signals they can verify cheaply.
- The operator stated the ledger must stay private. Stated 2026-09-22.
- A later move to a custom domain must not require rewriting links.

## Assumptions

- A1. The `waqas01cp.github.io` root slot is unused. **Measured**: the URL
  returned HTTP 404 on 2026-09-23.
- A2. Pages from a private repository requires a paid plan. **Sourced**:
  GitHub Docs, "What is GitHub Pages?" and "GitHub Pages limits", read
  2026-09-23.
- A3. Stating openness to freelance and contract work does not breach the
  Pages usage limits, because the site introduces the operator and does not
  take payment, quote prices or transact. **Stated** by the operator
  2026-09-23, against the quoted term above. Not tested against GitHub
  Support.

## Considered Options

- Public user site at `waqas01cp.github.io`, free
- Public project site at `waqas01cp.github.io/portfolio`, free
- Private repository with GitHub Pro, paid
- A custom domain now, on any of the above

## Decision Outcome

Chosen option: "Public user site at `waqas01cp.github.io`, free".

We will host the site on GitHub Pages from a public repository named
`waqas01cp.github.io`, serving at the domain root.
We will never commit `CHAT_STATE.md`, enforced by a gate on the path, not by
convention alone.
We will not buy a custom domain now, and any future purchase is a separate
decision with its price checked from the registrar first.
We will write every internal link as root-relative and hardcode no absolute
origin anywhere, so a later custom domain needs a DNS change and a CNAME file
and no content change.
We will offer contact by email link only, with no form and no third-party
form service.
We will state openness to remote employment, freelance and contract work,
without prices, quotes, invoicing or any payment mechanism.

### Consequences

- Positive: hosting costs nothing, and the yearly domain cost is deferred
  without foreclosing it.
- Positive: serving at the root, rather than a subpath, is what makes the
  later domain move a DNS change instead of a link rewrite.
- Positive: `docs/decisions/` and `docs/research/` being public is evidence
  of practice, not just a side effect of the free tier.
- Negative: a reader can see the site was designed around how hiring readers
  and their AI tools read material. Some will read that as rigour, some as
  calculation. Keeping the ledger out of the repository removes the sharpest
  part of that exposure, not all of it.
- Negative: the ledger gains no version history, because it is never
  committed.
- Negative: a `mailto:` address in the page source is scrapable. Accepted;
  the same address is already public in the profile README and on the CV.
- Negative: the free tier's limits are GitHub's to change.
- Neutral: the folder was renamed from `portfolio-site` to
  `waqas01cp.github.io` on 2026-09-23 to match.

### Confirmation

- The repository name is `waqas01cp.github.io` and the site resolves at that
  root.
- A gate blocks any commit that stages `CHAT_STATE.md`. Proven by attempting
  to stage it and observing the block; a gate that lets it through fails.
- A grep of the built output finds no occurrence of `waqas01cp.github.io` or
  `https://` pointing at the site's own origin. A single hardcoded absolute
  self-link fails this check.
- The recorded Pages limits are re-read from GitHub's documentation before
  any decision depends on them again.

## Pros and Cons of the Options

### Public user site at waqas01cp.github.io

- Good: free, root-served, and the domain move stays cheap.
- Good: the records and research become verifiable evidence.
- Bad: everything except the ignored ledger is permanently public, and a
  public repository's history cannot be deleted.

### Public project site at waqas01cp.github.io/portfolio

- Good: leaves the root slot for something else.
- Bad: every internal link carries a base path, so a later custom domain
  means a rewrite. This is the reason it loses.

### Private repository with GitHub Pro

- Good: the ledger could be committed with history, and nothing is exposed.
- Bad: a recurring fee for a portfolio whose content is meant to be read.
- Bad: loses the evidentiary value of public records.

### A custom domain now

- Good: a custom domain in a CV header reads better than a `github.io`
  subdomain, and it survives a change of host.
- Bad: the only recurring cost on the whole project, incurred before the site
  exists.

## More Information

- Usage limits recorded 2026-09-23 from GitHub's documentation, to be
  re-checked before anything depends on them: source repositories have a
  recommended limit of 1 GB; published sites may be no larger than 1 GB;
  deployments time out after 10 minutes; a soft bandwidth limit of 100 GB per
  month; a soft limit of 10 builds per hour, which does not apply when
  building with a custom GitHub Actions workflow.
- The Rahzaan case study stays at `waqas01cp.github.io/Rahzaan` as a project
  site from its own repository, unaffected by this record.
- The profile README repository is unaffected by this record.
- Revisit the domain if the site is being put on a printed CV or a
  conference badge, or if hosting moves away from GitHub.
- Revisit the contact route if email proves unusable, not before.

## Changes
