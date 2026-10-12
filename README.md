# Commute Expense Tracker
A personal backend project that automates tracking daily commute expenses using ride receipts received in Gmail, Splitwise expense creation, and Samsung Notes-compatible text export.

## Problem Statement
Daily college commutes involve multiple rides and manual expense tracking. This project aims to reduce repetitive work by extracting ride details from Gmail receipts, allowing the user to review expenses, syncing approved expenses to Splitwise, and generating formatted text for Samsung Notes.

## Project Goals
- Retrieve ride receipts from Gmail.
- Extract the ride date, fare, and commute direction where possible.
- Let the user review and correct extracted details before syncing.
- Create expenses in the appropriate Splitwise group.
- Generate monthly commute expense text that can be copied into Samsung Notes for personal budgeting.
- Prevent duplicate receipts and duplicate Splitwise expenses.

## Planned Technology Stack
- **Language:** Python
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Database toolkit:** SQLAlchemy
- **Validation:** Pydantic
- **Authentication:** Google OAuth 2.0
- **Integrations:** Gmail API and Splitwise API
- **Testing:** Pytest
- **Version control:** Git and GitHub

## How the System Will Work
1. The backend retrieves authorized ride receipts from Gmail.
2. It extracts relevant details and saves them in PostgreSQL for review.
3. The user checks and validates the fare, date, and commute direction.
4. The backend creates the approved expense in Splitwise.
5. The backend generates monthly commute text for copying into Samsung Notes.

The backend communicates with Gmail and Splitwise through their APIs. Their mobile apps do not need to remain open, but a locally hosted backend must be running when it performs its work.

## Planned Architecture
Gmail API → FastAPI → PostgreSQL → Splitwise API

FastAPI also generates a separate text export for Samsung Notes.

## Current Status
**Stage:** Initial setup and project planning

- [ ] Set up the Python environment and FastAPI application
- [ ] Create the first health-check endpoint
- [ ] Connect PostgreSQL
- [ ] Implement trip storage and review
- [ ] Integrate Gmail OAuth and receipt retrieval
- [ ] Integrate Splitwise expense creation
- [ ] Generate monthly Samsung Notes text
- [ ] Add tests and error handling

## Learning Notes
This README will also document the concepts learned during development, why they are needed, how they are implemented, and any bugs and solutions discovered along the way.

## Security
API credentials, OAuth client secrets, refresh tokens, database passwords, and other private configuration must not be committed to GitHub.