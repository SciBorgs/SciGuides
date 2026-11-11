# Contributing to SciGuides

SciGuides is a ***living document***. Both it and [our template repository](https://github.com/SciBorgs/JVRobotBase.git) should be updated yearly to reflect current team programming standards and all changes to WPILib, external docs, and vendor libs.

We welcome contributions and feedback from anyone. If you are in JV or just an interested reader, welcome! Make sure to see our [guide](#outside-contributions) for outside contributions.

## Getting Started

All of our guides here are written in markdown and then deployed to GitHub Pages through [mkdocs](https://www.mkdocs.org/). Make sure your .md file is in the docs directory, and update the mkdocs.yml nav section so that your page will appear on the sidebar. Before pushing your guide, you should run ```mkdocs build``` in the terminal so it will update the site.

### Proper Procedure

If you have changes you'd like to make, discuss with a mentor or programming leadership before making them. Make sure to follow the review process as listed below.

1. Please create your own branch and pull request (PR) to make changes from.
2. Request a review from relevant members of leadership, and respond.
3. Repeat step 2 until approval.

Do not open duplicate pull requests or issues; check that others have not already made or discussed your desired request.

## Creating content

See the [summary](#tldr-too-long-didnt-read) for quick reference.

### Guidelines

We hope to maintain a quality standard for our work, so all writing should roughly follow the below guidelines:

- Your guides should be professional
    - Check over your grammar
    - Keep everything updated 
    - Use ```code formatting```
    - Make sure your code actually works
    - Have someone (or yourself) follow the guide so you can check that every step works and flows
- Link to existing documentation (WPIlib, Photonvision, CTRE) whenever you can
    - We want our yearly maintenance work minimized. If we avoid re-writing what is already in these other sources, we can save ourselves a lot of time
- Practice project-based learning
    - People do not want to just sit and read what you've written; they want to make something
    - The best guides are ones that let people follow along while creating a project of their own
    - Avoid walls of text like the plague

#### Specifics

For GitHub & editor compability purposes, all comments should be formatted like so:
`[comment]: # (YOUR-COMMENT-HERE)`

#### AI Policy

AI can be very helpful when writing long articles, researching, correcting grammar, and much more. As you'll see in other [articles](./sheets/EnvironmentSetup.md/#a-secret), we do not discourage the use of AI. With that in mind, we still have guidelines concerning AI.

These guides are still considered your work, and anything AI writes should be reviewed and edited by you. You are accountable for...

  - Fixing mistakes the AI makes
  - Changing its tone to fit the style of our guides in general
  - Carefully considering whether to add or subtract from the content it chooses to include

Consider whether you have written a paragraph or simply approved what the AI wrote. Where necessary, indicate the use of AI like we did [here](#spacing-techniques).

In general, AI should not replace your thinking. We mantain that it is best used as a workhorse for writing tedious sections or used in an advisory role.

### Style & Writing Tips

There are a few boxes to check when writing engaging, cool pages, especially not having lengthy paragraphs of text!

#### Fundamentals

Prioritize readability.
- Break down complex paragraphs and explanations into smaller parts; use identation and [whitespace](#spacing-techniques) to your advantage.
- Use [GitHub markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) features to emphasize and guide certain parts of the doc. This includes headings, lists, separators, footnotes, etc.
- Be concise and to-the-point with your words.
- Avoid repetition unless it just makes sense.

Keep in mind your target audience; introduce complexity bit-by-bit for beginners, and relax for advanced students.

To the best of your ability, anticipate common learning mistakes or pitfalls and address them so that in-person mentors won't have to.

#### Spacing Techniques

A good idea is to put yourself in the shoes of a brand new robotics student learning the ropes. If you were them, would you rather read this...

---

*Java, the workhorse of enterprise software, often feels like a language stuck in the past despite its incremental improvements. Its verbose syntax can make even simple tasks feel like wading through boilerplate code, with developers writing lines upon lines just to declare objects or handle exceptions. The "write once, run anywhere" mantra sometimes translates to "debug everywhere," especially with JVM inconsistencies across environments. Performance, though respectable, often pales in comparison to more modern, lightweight languages, and its garbage collection, while helpful, can cause unpredictable hiccups. Java's ecosystem, though vast, can be overwhelming, with libraries and frameworks that vary wildly in quality. Despite all this, it remains entrenched, leaving developers with no choice but to navigate its quirks for the sake of legacy systems and industry demand.*
###### Generated by GPT-4o. Does not represent the opinions of the team nor any related individuals.

---

or this...?

---

*Java, the workhorse of enterprise software, often feels like a language stuck in the past despite its incremental improvements.*

*Its verbose syntax can make even simple tasks feel like wading through boilerplate code, with developers writing lines upon lines just to declare objects or handle exceptions. The "write once, run anywhere" mantra sometimes translates to "debug everywhere,"especially with JVM inconsistencies across environments.*

*Performance, though respectable, often pales in comparison to more modern, lightweight languages, and its garbage collection, while helpful, can cause unpredictable hiccups.*

Java's ecosystem, though vast, can be overwhelming, with libraries and frameworks that vary wildly in quality.*

*Despite all this, it remains entrenched, leaving developers with no choice but to navigate its quirks for the sake of legacy systems and industry demand.*
###### Generated by GPT-4o. Does not represent the opinions of the team nor any related individuals.

---

I'd like to bet you chose the second selection. And that's because you can easily pick out and read it! Each new topic is put on its own, allowing for simpler referencing and understanding.

So, if you find yourself writing something too long (which you should avoid regardless), space it out a bit! Especially for instructions.

## TL;DR (too long; didn't read):

- Create a branch and pull request of your own to add features. Your changes will be merged after looping through the review process.
  - Consult with leadership before making any changes; you wouldn't want to make unnecessary additions!
- Instead of wordily explaining concepts on your own, reference external docs and sources for **in-depth information**.
  - A good balance we follow is to introduce a concept / process with a few sentences before linking to more in-depth documentation.
- Keep your documents readable - no text walls (they hurt the eyes!)
  - Take advantage of text-spacing techniques with newlines, codeblocks, images, & other styling elements (like this list!)
- See the specific [style section](#style) above.

## Outside Contributions

In addition to the rest of this guide, we want to make sure outside contributors know how the review process works when you aren't part of our organization. We would love your contributions, but your project might already be in progress internally or we simply won't notice your PR. Please make sure to contact us before starting and either open an issue or address one that is already there. Our email is sciborgs-leadership@bxscience.edu.

Contributing to this repository (and other open source projects) requires making a [fork](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo). When you've made your guide following all the rules above, make a pull request from the forked repository instead and select the upstream repository to merge into. Then you can follow the review process outlined above.