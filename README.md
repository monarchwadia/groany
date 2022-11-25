# Groany 😩

A painfully interactive CLI you can use for inspiration when torturing the spouse and kids.

> I like telling Dad jokes ... sometimes he laughs. 

## Installation

You can install Groany using pip.

```
pip install --index-url https://test.pypi.org/simple/ groany
```

And then, you can use it by typing `groany`. This will drop you into an interactive shell where you can find jokes from the [icanhazdadjoke.com](https://icanhazdadjoke.com/) API.

## How to use

Inside `groany`, you gain access to the following commands.

* `<entering a search term>` - You can input a subject as a search term. Groany will scour the icanhazdadjoke API for matching dad jokes. Pretty simple, but very deadly.
* `<no term entered, just press enter>` - If you input a blank search term, Groany will give you a random joke from the icanhazdadjoke API. Great for when inspiration has run dry.
* `funny` - If you type this, you'll exit out of groany. But why would you ever want to?

## Sample Usage

```
$> groany
Welcome to groany. You can use this to get dad jokes. Type help or ? to list commands.
What kind of dad joke are you in the mood for?
(groany)> odd
Why do valley girls hang out in odd numbered groups? Because they can't even.
What kind of dad joke are you in the mood for?
(groany)> thesaurus
My new thesaurus is terrible. In fact, it's so bad, I'd say it's terrible.
What kind of dad joke are you in the mood for?
(groany)>
What is a tornado's favorite game to play? Twister!
What kind of dad joke are you in the mood for?
(groany)> funny
What kind of dad joke are you in the mood for?
Goodbye!
```

## Configuration and joke deduplication

Groany saves its configuration files inside your user's home directory, in a folder named `.groany`. Currently, there is only one such configuration file: `.groany/groany.json`. This file keeps track of jokes you've seen in the past, and stops duplicate jokes from appearing in your terminal.

However, this DOES mean that Groany will frequently run out of jokes to tell you. If you want to reset Groany, simply delete the `.groany` folder and Groany won't even know what hit it.

# Contributing

Want to get involved? That's awesome. We're always looking for new contributors to help make Groany even better! Here's how to get started.

## Dev workflow

First, fork and clone down this repo. 

Then, do `pip install` for development purposes, like so:

```
pip install -e .[dev]
```

Now, you want to link your local copy of groany into your binary PATH. `pip` makes this super easy to do with the following command. After this, invoking `groany` from the CLI will run your project in the terminal. Changes in your source code should automatically propagate globally.

```
pip uninstall groany; # in case there's an older version installed
pip install --editable .
```

Cool! You're all set up! To contribute back, simply open a PR from your repo to our `main` branch.

## Testing

You can test the project using the following command from the root directory of the project.

```
./test.sh
```

## Publishing

Publishing is usually done by the core team. Here are the steps we take in order to publish the repo, from the root directory of the project.

```
./build.sh;
./publish.sh;
```

When prompted for your username and your password, use `__token__` as the username. For password, just use your API token from PyPI.
