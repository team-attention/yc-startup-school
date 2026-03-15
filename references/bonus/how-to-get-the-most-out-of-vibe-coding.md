---
title: "How To Get The Most Out Of Vibe Coding"
author: "Tom Blomfield"
slug: "MN-how-to-get-the-most-out-of-vibe-coding"
series: "Startup School"
youtube_id: "BJjsfNO5JTo"
youtube_url: "https://www.youtube.com/watch?v=BJjsfNO5JTo"
source_url: "https://www.ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding"
description: "From writing full-stack apps to debugging with a single paste of an error message, AI is becoming a legit collaborator in the dev process. This video is a playbook for anyone who wants to get the most out of vibe coding and build faster."
duration_seconds: 1000
created_at: "2025-04-25T14:00:15.000Z"
chapters:
  - time: 0
    title: "Intro"
  - time: 54
    title: "Some vibe coding tips from YC X25 founders"
  - time: 252
    title: "First, pick your tools and make a plan"
  - time: 387
    title: "Use version control"
  - time: 443
    title: "Write tests"
  - time: 494
    title: "Remember, LLM's aren't just for coding"
  - time: 537
    title: "Bug fixes"
  - time: 670
    title: "Documentation"
  - time: 723
    title: "Functionality"
  - time: 800
    title: "Choose the correct stack"
  - time: 908
    title: "Refactor frequently"
  - time: 940
    title: "Keep experimenting!"
  - time: 981
    title: "Outro"
has_transcript: true
---

# How To Get The Most Out Of Vibe Coding

**Tom Blomfield**
[YouTube](https://www.youtube.com/watch?v=BJjsfNO5JTo) | [YC Library](https://www.ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding)

## Transcript

Tom: Hi, I'm Tom and I'm a partner here at YC. For the last month, I've been experimenting with vibe coding on a couple of side projects and I found not only is it remarkably good, but it's also a practice you can get measurably better at if you're open to tinkering and picking up best practices. In this video, I want to share some ways you can get great results when vibe coding.

Tom: It's kind of like prompt engineering from a year or two ago. People were discovering new stuff every week and posting about it on social media. The best techniques are the same techniques that a professional software engineer might use. And some people like, "Well, that's not vibe coding, is it? You're now just software engineering." I kind of think that's beside the point. We're trying to use these tools to get the best results.

Tom: And the YC Spring Batch just kicked off a couple of weeks ago. And before I give you my advice for vibe coding, let's hear from the founders on the tips they're using to get the best out of the AI tools today.

Founder 1: If you get stuck in a place where the AI IDE can't implement or can't debug something and it's just stuck in a loop, sometimes going to the LLM's website—like literally to the UI and just pasting in your code and asking the same question—can get you a result that for whatever reason the IDE like couldn't get to, and you can solve your problem that way.

Founder 2: So I'd say like just load up both Cursor and Windsurf on the same project. Um, Cursor it's a bit faster, so you can do a lot of like the front end, like a little more like full stacky, like link the front end to the back end. Windsurf thinks for a bit longer. I used to just be like scrolling on my phone while I type, "Build this agent" or like, you know, "Modify this prompt," and I'll just like scroll, fix, scroll, or like, you know, paste an error. Now while I'm waiting for Windsurf to think, I can go on Cursor and like, you know, start updating the front end.

Founder 2: Uh, sometimes I'll load up both at the same time and like have like the same context. Maybe if I'm trying to update the front end, I'll give it like, style it in like the style of that file, and then I'll just press enter for both and then they'll both basically give me like slightly different iterations of the same front end and I'll just pick which one I like better.

Founder 3: My advice would be to uh think of the AI as a different kind of programming language and vibe coding as being a different, um, a new type of programming language. And so instead of programming with code, you're programming with language. And uh, because of that you kind of have to provide a lot of the necessary context and uh information in a very detailed way if you want to get good results.

Founder 4: I usually start vibe coding in the reverse direction. That is, first starting from the test cases. I handcraft my test cases. I don't use any LLMs to write my test cases. And once it is done, I have strong guard rules that my LLMs can uh can follow for generating the code, right? And then they can freely generate the code that they want to generate. And once I see those green flags on my test cases, the job is done. I don't need to micromanage my code bases. I just, I just uh take overview about the modularity of the code. Other than that, it's fine.

Founder 5: Yeah, I think it's very important to first spend like an unreasonable amount of time uh in like a pure LLM to build out like the scope and the actual architecture of what you're trying to build before offloading that to Cursor or any other kind of coding tool uh and let it just like free run in the codebase, just random making up stuff that doesn't really work. Um, so make sure you understand what the actual goal of what you're building is.

Founder 6: My advice would be to really monitor whether the LLM is falling into a rabbit hole when it's answering your question. And if you notice that it just keeps regenerating code and it looks kind of funky, it's not really able to figure it out. If you're having to find yourself copy and pasting error messages all the time, it probably means something's gone awry and you should take a step back. Even prompt the LLM and say, "Hey, you know, let's take a step back and try to examine basically why it's failing. Is it, you know, is it because you haven't provided enough context for the LLM to be able to figure it out? Or have you just gotten unlucky and it's unable to do your request?"

Tom: The overarching theme here is to make the LLM follow the processes that a good professional software developer would use. So let's dive in and explore some of the best vibe coding advice I've seen. First, where to start. If you've never written any code before, I would probably go for a tool like Replit or Lovable. They give you an easy to use visual interface and it's a great way to try out new UIs directly in code. Many product managers and designers are actually going straight to implementation of a new idea in code rather than designing mock-ups in something like Figma, just because it's so quick.

Tom: But when I tried this, I was impressed with the UIs. But tools like Lovable started to struggle when I wanted to more precisely modify backend logic rather than just pure UI changes. I'd change a button over here and the backend logic would bizarrely change. So if you've written code before, even if you're a little bit rusty like me, you can probably leap straight to tools like Windsurf, Cursor, or Claude Code.

Tom: Once you've picked the tool you want to use, the first step is not to dive in and write code. Instead, I would work with the LLM to write a comprehensive plan. Put that in a markdown file inside your project folder and keep referring back to it. This is a plan that you develop with the AI and you sort of step through while you're implementing the project rather than trying to oneshot the whole thing.

Tom: And so what I'd do after you've created the first draft of this plan, go through it, delete or remove things that you don't like. You might mark certain features explicitly as "won't do—too complicated." And you might also like to keep a section of ideas for later, you know, to tell the LLM, "Look, I considered this, but it's out of scope for now."

Tom: Once you've got that plan, work with the LLM to implement it section by section and explicitly say, "Let's just do section two right now." Then you check that it works. You run your tests and you get a commit. Then have the AI go back to your plan and mark section two as complete. I probably wouldn't expect the models to oneshot entire products yet, especially if they're complicated. I prefer to do this piece by piece and make sure I have a working implementation of each step and crucially commit it to Git so that you can revert if things go wrong on the next step.

Tom: But honestly, this advice might change in the next two or three months. The models are getting better so quickly that it's hard to say where we're going to be in the near future. My next tip is to use version control. Version control is your friend. Use Git religiously. I know the tools have these kind of revert sort of functionality. I don't trust them yet. So I always make sure I'm starting with a kind of a clean Git state before I start a new feature so that I can revert to a known working version if the AI goes off on a vision quest.

Tom: So don't be afraid to `git reset head hard` if it's not working and just roll the dice again. I found I had bad results if I'm like prompting the AI multiple times to try to get something working. It tends to accumulate layers and layers and layers of bad code rather than like really understanding the root cause. You might go and try four, five, six different prompts and you finally get the solution. I'd actually just take that solution, `git reset`, and then feed that solution into the AI on a clean codebase so you can implement that clean solution without layers and layers of craft.

Tom: The next thing you should do is write tests, or get your LLM to write tests for you. They're pretty good at this. Although they often default to writing very low-level like unit tests, I prefer to keep these tests super high level. Basically you want to simulate someone clicking through the site or the app and ensure that the features are working end to end rather than testing uh functions on a kind of unit basis. And so make sure you write high-level integration tests before you move on to the next feature.

Tom: LLMs have a bad habit of making unnecessary changes to unrelated logic. So you tell it to fix this thing over there and it just changes some logic over here for really no reason at all. And so having these test suites in place, catch these regressions early will identify when the LLM has gone off and made unnecessary changes so that you can `git reset` and start again.

Tom: Keep in mind LLMs aren't just for coding. I use them for a lot of non-coding work when I'm building these kind of side projects. For example, I had Claude Sonnet 3.7 configure my DNS servers, which is always a task I hated, and set up Heroku hosting via a command line tool. It was a DevOps engineer for me and accelerated my progress like ten times. I also used ChatGPT to create an image for my site's favicon—that little icon that appears at the top of the browser window. And then Claude took that image and wrote a quick throwaway script to resize it into the six different sizes and formats I needed for favicons across all different platforms. So the AI is now my designer as well.

Tom: Okay, so now let's look at bug fixes. The first thing I do when I encounter any bug is just copy paste the error message straight back into the LLM. It might be from your server log files or the JavaScript console in the browser. Often this error message is enough for the AI to identify and fix a problem. You don't even need to explain what's going wrong or what you think's going wrong. Simply the error message is enough. It's so powerful that pretty soon I actually expect all the major coding tools to be able to ingest these errors without humans having to copy paste.

Tom: If you think about it, our value being the copy-paste machine is kind of weird, right? We're like, we're leaving the thinking to LLM. But I think that copy-pasting is going to go out the window and these LLM tools are going to be able to tail logs or, you know, um, spin up a headless browser and inspect the kind of JavaScript errors.

Tom: With more complex bugs, you can ask the LLM to think through three or four possible causes before writing any code. After each failed attempt at fixing the bug, I would `git reset` and start again. So you're not accumulating layers and layers of crust. Don't make multiple attempts at bug fixes without resetting because the LLM just adds more layers of crap. `Git reset`, start again, and add logging. Logging is your friend.

Tom: If in doubt, if it's not working, switch models. Maybe it's Claude Sonnet 3.7, maybe it's one of the OpenAI models, maybe it's Gemini. I often find that um different models succeed where the others fail. And if you do eventually find the source of a gnarly bug, I would just reset all of the changes and then um give the LLM very specific instructions on how to fix that precise bug on a clean code base to avoid this, like, layers and layers of junk code accumulating.

Tom: Next tip is to write instructions for the LLM. Put these instructions in whether it's Cursor rules, Windsurf rules, or a claw markdown file. Each tool has a slightly different naming convention. But I know founders who've written hundreds of lines of instructions for uh their AI coding agent and it makes them way, way, way more effective. There's tons of advice online about what to put in these instruction files. I'll let you go and find that on your own.

Tom: Okay, let's talk about documentation. I still find that pointing these agents at online web documentation is a little bit patchy still. I mean, some people are suggesting uh using an MCP server to access this documentation, which works for some people. Uh seems like overkill to me. So I'll often just download all of the documentation for a given set of APIs and put them in a subdirectory of my working folder so the LLM can access them locally. And then in my instructions, I'll say go and read the docs before you implement this thing. And it's often much more accurate.

Tom: A side note to remember, you can use the LLM as a teacher, especially for people who are less familiar with the coding language. You might implement something and then get the AI to walk through that implementation line by line and explain it to you. It's a great way to learn new technologies. It's much better than scrolling Stack Overflow like uh we all used to do.

Tom: Now, let's look at more complex functionality. If you're working on a new piece of functionality, a new feature that's more complex than you'd normally trust the AI to implement, I would do it as a standalone project in a totally clean codebase. Get a small reference implementation working without the the complication of your existing project, or even download a reference implementation if someone's written one and posted on GitHub. Then you point your LLM at the implementation and tell it to follow that while reimplementing it inside your larger codebase. It actually works surprisingly well.

Tom: Remember, small files and modularity are your friend. This is true for human coders as well. I think we might see a shift towards more modular or service-based architecture where the LLM has clear API boundaries that it can work within while maintaining a consistent external interface, rather than these huge monolithic repos with massive interdependencies. These are hard for both humans and LLMs. It's just not clear if a change in one place is going to impact another part of the codebase. And so having this this modern architecture with a consistent external API means you can change the internals as long as the external interface and the tests still pass, you're probably good.

Tom: Now a note on choosing the right tech stack. I chose to build my project partially in Ruby on Rails mostly because I was familiar with it from when I used to um be a professional developer. But I was blown away by the AI's performance, especially when it was writing uh Ruby on Rails code. And I think this is because Rails is a twenty-year-old framework with a ton of well-established conventions. A lot of Rails code bases look very, very similar and it's obvious to an experienced Ruby on Rails developer where a specific piece of functionality should live or the right Rails way of achieving a certain outcome. That means there's a ton of pretty consistent, high-quality training data for Rails code bases online.

Tom: I've had other friends have less success with languages like Rust or Elixir where there's just not as much training data online, but who knows? That might change very soon.

Tom: Okay, next bit of advice: use screenshots. You can copy and paste screenshots into most coding agents these days and it's very useful either to demonstrate a bug in the UI implementation that you can see or to pull in design uh inspiration from another site that you might want to use in your project.

Tom: Voice is another really cool way to interact with these tools. I use Aqua, a YC company, and basically I can just talk at my computer and Aqua transcribes whatever I'm saying into the tool I'm using. I'm switching a lot between Windsurf and Claude Code at the moment, but with Aqua, I can effectively input instructions at one hundred forty words per minute, which is about double what I can type. And the AI is so tolerant of minor grammar and punctuation mistakes that it honestly doesn't matter if the transcription's not perfect. I actually wrote this entire talk with Aqua.

Tom: Next, make sure to refactor frequently. When you've got the code working and crucially the tests implemented, you can refactor at will, knowing that your tests are going to catch any regressions. You can even ask the LLM to identify parts of your codebase that seem repetitive or might be good candidates for refactoring. And again, this is just a tip that any professional software developer would follow. You don't have um files that are thousands of lines long. You keep them small and

Tom: Modular. It makes it much easier for both humans and LLMs to understand what's going on. Finally, keep experimenting. It seems like the state-of-the-art of this stuff changes week by week. I try every new model release to see which performs better in each different scenario. Some are better at debugging or long-term planning or implementing features or refactoring. For example, at the moment, Gemini seems best for whole codebase indexing and coming up with implementation plans, while Sonnet 3.7, to me at least, seems like the leading contender to actually implement the code changes. I tried GPT 4.1 just a couple of days ago, and honestly, I wasn't yet as impressed. It just came back with me with too many questions and actually got the implementation wrong too many times. But I'll try it again next week and I'm sure things will have changed again. Thanks for watching and I'd love it if you have tips or tricks for getting the most out of these models. Please share them in the comments below.
