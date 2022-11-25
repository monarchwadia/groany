# Python Coding Assignment - Dad Joke CLI

## Overview
Build a Python CLI that prints “dad jokes”.

## What we’re looking for
- Clear and approachable end user documentation
- Effective project communication
- Readable code, even for an inexperienced Python developer
- Unit tests that exercise the core functionality
- Code organization
- Following common Python conventions

## Expectations
- 2-4 hours of effort
- $300 paid upon completion via PayPal, Venmo, or ACH

## Communication and submission process
The GitHub Issue you’re reading now is our primary communication channel for this project. However, if you have questions or comments that make more sense in the context of a specific commit or pull request, please comment in that commit/PR and mention @adamlogic so I see it.

Since this project is building a package from scratch, you do **not** need to submit your code as a single PR. Please push directly to `main`. If it’s helpful for you to create pull requests along the way for your own organizational purposes, please do so. You do not need my approval to merge those PRs.

Try to keep your commits focused on a single objective. A single commit that implements the entire project is not ideal. “WIP” and “oops” commits are fine in branches, but not in `main`.

When you are done with the project, close this issue and mention @adamlogic to let me know.

**If you have questions along the way, please ask!**

## The assignment
I want to install a package from [TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/) that exposes a CLI for printing dad jokes.

- The CLI should fetch dad jokes from [icanhazdadjoke](https://icanhazdadjoke.com/api#fetch-a-dad-joke-as-an-image).
- The CLI should should ask “What kind of dad joke are you in the mood for?”
	- Entering any text should search for dad jokes containing that text.
	- Entering no text should find a random dad joke.
	- Entering “funny” exits the program.
- Print the dad joke, then ask the same question again.
- I should never see the same dad joke twice, even between multiple invocations of the CLI on the same machine.
- Name your package something unique to you. **Do not** include “judoscale” or “dad-jokes” in the package name since it might conflict with assignments from other candidates.
- Include a README that explains how to install and use the package, **and** how to contribute to the package (running the code locally and running tests).


## TODO

[x] CLI asks what kind of dad joke are you in the mood for, takes a prompt, and loops until "funny" is put in
[x] Dad jokes never repeat, even between invocations
[] Unit tests
[] Publish to TestPyPI
[] Works as expected via TestPyPI
[] Clean code
[] Include a README as per specs