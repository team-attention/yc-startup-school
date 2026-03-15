---
title: "Michael Truell: Building Cursor at 23, Taking on GitHub Copilot, and Advice to Engineering Students"
author: "Y Combinator"
slug: "Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students"
series: "AI Startup School"
youtube_id: "TrXi3naD6Og"
youtube_url: "https://www.youtube.com/watch?v=TrXi3naD6Og"
source_url: "https://www.ycombinator.com/library/Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students"
description: "In this fireside chat with YC General Partner Diana Hu, he shares the lessons that came from years of failed projects with his co-founders, why he believes programming is still essential even as AI changes how we code, and how Cursor is taking on GitHub Copilot with the conviction that all of software development will flow through models."
duration_seconds: 1676
created_at: "2025-09-03T14:00:50.000Z"
chapters:
  - time: 38
    title: "– PG essays & first code"
  - time: 156
    title: "– Games, robots, and hacking ML as a teenager"
  - time: 414
    title: "– From Hemisphere to Cursor: first startup attempts"
  - time: 594
    title: "– Pivoting hard when nothing was working"
  - time: 724
    title: "– Taking on GitHub Copilot"
  - time: 790
    title: "– Shipping the first Cursor editor"
  - time: 924
    title: "– Early lessons: features, feedback, and VS Code shift"
  - time: 986
    title: "– Codex, custom models, and pragmatic bets"
  - time: 1078
    title: "– Wandering in 2023"
  - time: 1200
    title: "– Breakthrough: $1M → $100M in a year"
  - time: 1366
    title: "– Word of mouth and wildfire growth"
  - time: 1524
    title: "– The future of coding and advice for students"
has_transcript: true
---

# Michael Truell: Building Cursor at 23, Taking on GitHub Copilot, and Advice to Engineering Students

**Y Combinator**
[YouTube](https://www.youtube.com/watch?v=TrXi3naD6Og) | [YC Library](https://www.ycombinator.com/library/Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students)

## Transcript

Host: We realized we were really inherently excited about the future of coding. And I think we took a step back and realized that if we were being really consistent with our beliefs, there was going to be an opportunity for all of coding to change in the next 5 years and for all of software development to flow through models. It felt like no one working on the space at the time was really taking that seriously. It felt like they had great products and they were making them a bit better, but they weren't really aiming for a world where, you know, all of coding as we know it today gets automated and building software ends up looking very, very different. Then with that in mind, we set out to work on that.

Host: Let's start this talk with sort of the origin story of your journey as a founder. You kind of have to go way back to middle school when you were reading the essays from PG, right?

Michael Truell: So early on I think, you know, I had been interested in starting a company for a long time. Had been interested in a bunch of other things too. I think actually originally got into programming being interested in starting something kind of commercial where the first time that I ever saw code. It was over some winter break and my brother and I we wanted to create a hit mobile game. We didn't really know how to do that. We looked on Google how do you create a game? We heard that you need to download this application called Xcode. We did that and we were hit with these weird colorful esoteric symbols which were Objective C which, you know, is still around but maybe a little bit less popular than it was then for good reasons. And I stared at this kind of impenetrable wall of Objective C and my brother promptly ejected. Didn't move on with programming. He now is on a very different career path. He's kind of trying to paint or something like that. But I yeah kept going and I bought a book on Objective C and then eventually started working on mobile games. That was the genesis of me getting into programming. And then along the way, also yes, was a big fan of PG's essays and Sam's essays too, also and a bunch of the folks in YC and that was definitely a big inspiration even from the very early stages of high school.

Host: I think the wildest thing about Cursor is that right now you're just 24 and you've built this monster of a company in a really short amount of time. To a lot of people it could seem that it's a bit out of nowhere, but this was really in the making for more than a decade. You've been working and shipping a lot of different projects, right? And you were working in AI even when you were in high school, right? Tell us a bit about the projects and how you got started with that.

Michael Truell: Was lucky enough to find programming early on. Was also lucky enough to be interested in AI early on and have some great collaborators to work on AI projects with soon after kind of the foray into mobile games which also turned into, I wasn't very good at mobile games, so one of the things that I built and actually one of the things that got most popular which was kind of the technically easiest thing to build which was maybe a lesson in startups of, you know, the code isn't everything, was this mobile app where you could spoof high scores in things like Piano Tiles and Flappy and then send them to your friends. And that was kind of the thing that went viral. It wasn't the, you know, painstakingly handcrafting the game engine yourself thing. But yeah, no, soon after that I got interested with a friend in the idea of building a robotic dog where we thought it would be really great to have a robot that you could teach to do things without programming it. Instead you could give it positive and negative feedback like you give a dog. So you could give it a treat if it does something good. You could say bad if it does something bad. And then maybe you could teach it to play fetch and things like that. That idea really animated us. But we had no idea how to build it. And so again, you know, started the place where one would start which is Google and kind of went down a lot of rabbit holes and took us into a place of learning about genetic algorithms and maybe that was going to be helpful for building this robot dog that we wanted to build. And then we eventually learned about this neural network stuff because some people were playing with taking genetic algorithms and using them to evolve neural networks at the time, you know, with work like NEAT. And then eventually it took us to RL, reinforcement learning, which was, you know, even back in 2015, people had been working on it for a long time. In the end my friend and I we did eventually build a couple of robots. We didn't do any sort of substantial work that really lasted but we did work that was interesting at the time in taking reinforcement learning algorithms and making them more data efficient, you know, making them better at learning from very, very few data points, you know, order of tens of data points and also from noisy data, you know, data that a human's giving. It wasn't exactly a dog, but we built a couple of robots where one of them was this many-axis robot arm that could kind of swing a paddle and play ping pong and if you put the right sensor on it and then you gave it the right sort of positive and negative feedback, you could teach it to swing when it sees a ball. And then we had this Kiwi drive robot that we would teach to follow a line. To do that. It was actually kind of this great education in ML. Partially because of our dumb naiveté where we didn't really know that there were things like Torch and TensorFlow and kind of other, you know, lots of building blocks we could use, or maybe we weren't good enough at Googling.

Host: So you like implemented your own neural network from scratch.

Michael Truell: Yeah. So—

Host: When you were like, I don't know, 16, 17?

Michael Truell: The constraints of the problem were we were dealing with robots and so we were dealing with microcontrollers. And so microcontrollers have very little memory and they couldn't really fit any of the normal standard ML libraries. So as part of our bike shedding trying to build a robot dog, we implemented our own tiny neural network library and I have memories of us not really understanding any of the internals of how these things worked or not really understanding calculus but kind of fumbling our way through reimplementing some important ideas from neural networks. I think it taught us a lot. I think there were a lot of gaps in the fundamentals that it took many years to fill in later.

Host: Then fast forward to the founding of Anyphere. It's an interesting name because Cursor is not what it is. When you guys started, you had just graduated MIT, right? That was back in 2022.

Michael Truell: What were the first ideas that all four of you started working on back in 2022?

Host: Yeah. So the genesis of Cursor was in 2021. My co-founders and I, we had been interested in AI for a long time. Each of us kind of had our own little robot dog moment where one of my co-founders he worked on trying to build a competitor at Google actually using LLMs in 2021 and training his own contrastive models. One of my co-founders worked on computer vision in academia and, you know, some of us also worked on recommendation systems at companies like Google. But we were really interested in AI. In 2021 we were trying to figure out what to do with that interest. Do we go and work on AI in academia or, you know, do we go join a big existing AI effort or do we start our own thing? And there were two moments that really got us excited. One was seeing the first AI product start to come out, you know, GitHub Copilot was really the canonical example for us. The other was seeing work about how it looked like AI was going to predictably get better in the future as you scale up these models. At the very beginning of 2022, me and my co-founders, we went on like a month-long hackathon basically and we started hacking on ideas related to kind of picking an area of knowledge work and building what it looks like as AI gets more and more mature.

Host: You guys have collected a lot of data for that first idea, right?

Michael Truell: Yeah. So the first real idea that we worked on for a long time was in mechanical engineering. We were trying to build a co-pilot for mechanical engineers and trying to train models to kind of predict what you would do in a CAD system like Solidworks or Fusion 360, which is where mechanics model out parts in 3D on a computer. We picked it because we thought it would be boring and sleepy and uncompetitive and we were kind of doing an armchair MBA thing even though it was a horrible choice from the get-go because none of us were really mechanical engineers and also the science wasn't really ready for that area.

Host: But you guys kept working at it for a number of months, right? And you crawled and got all these CAD files and actually got something working with auto-completion, right? That was like the first version of it working.

Michael Truell: Yes. A bunch of the work was in data scraping. Honestly, it was trying to get all the CAD models on the internet. There are also all these different file formats and trying to convert them all into something that's canonical because CAD is this weird software market where there are all these different systems that are pretty popular. It's very fragmented. There are also cloud CAD systems that don't have easily exportable files and they don't want you to scrape their stuff and so there was a bunch of work there. Also the training infrastructure for doing any kind of modeling work back then was pretty rudimentary and so there was a lot of work on the infra side there and just a lot of experimenting with models and a lot of experimenting with how you even jerry-rig an extension into these CAD systems because these applications aren't really extensible at all. There were actually also other projects that we were working on at the time. So two of my co-founders they were working on an end-to-end encrypted messaging system because one of them has a background in security research and the idea there was apps like Signal and WhatsApp, they encrypt the body of the messages but they don't hide who's talking to who at what time which is actually really crucial information if you don't want to trust the messaging app provider. So, you know, if a journalist is talking to some informant in the government, just knowing that they're communicating at all is a really big piece of information.

Host: So that was in the middle of 2022. So you guys were working for about a good 6 months on this idea.

Michael Truell: Yes.

Host: And how many users were you getting at that point? So you shipped the product.

Michael Truell: All of these projects were elevated and it had basically no users.

Host: At what point did you realize that the idea was not working? It's like, oh no, we're all working on this. We're trying to do the startup. It's not working. And what was that moment like?

Michael Truell: I think it was a bit different for each of the projects. I think for the messaging system that two of my co-founders worked on, it was really technically impressive, but it had these bad trade-offs where it wasn't very scalable. And I think they tried to give it to people and it didn't really work. And then they tried to sell it B2B and then it didn't really work. And I think it was after a couple of months of trying to get traction for the CAD idea. It was, yeah, many months of trying to get the models to really be useful for end users and then also reckoning around, are we really interested in these areas or is there something else that we're inherently much more excited about?

Host: So there was a moment that you decided okay, these ideas are not working. We have to pivot again.

Michael Truell: Yes.

Host: You turned through three ideas, three, four, five ideas before landing into code completion.

Michael Truell: Yeah. I think that we had been inspired by tools like Copilot really early on and we had avoided working on AI and coding because we thought it was too competitive. Competitive then, still is competitive now.

Host: So 2022, GitHub Copilot was making already about 100 million in revenue?

Michael Truell: I think or more—

Host: Potentially more.

Michael Truell: Yeah.

Host: And you guys are like, "Oh, we could still do a better job than GitHub Copilot because people thought the game was done." It's like, "Hey, GitHub."

Michael Truell: Well, I mean, we didn't think we could at the start. And then I think, you know, it was the desperation of having worked on ideas for a while and not really being excited about them after a while and them not really working out. And that kind of shapes, I think, what you care about and what you're aiming for. And we realized we were really inherently excited about the future of coding. I think also we got to see how some of the other people in the space were, you know, working on their products. We got to see how the tech was developing. And I think we took a step back and realized that if we were being really consistent with our beliefs, you know, there was going to be an opportunity for all of coding to change in the next 5 years and for all of software development to flow through models. And it felt like no one working on the space at the time was really taking that seriously. It felt like they had great products and they were making them a bit better but they weren't really aiming for a world where, you know, all of coding as we know it today gets automated and building software ends up looking very, very different. Then with that in mind we set out to work on that.

Host: That was a bold move because you said okay, we're going to stop working on all these other ideas that we didn't have as much of a background in and you were excited about programming even though you had this big Goliath in the room with GitHub Copilot. You decided to go and let's just solve this problem.

Michael Truell: It didn't really feel bold or like a move at the time because it's like, you know, a bunch of people sitting around in their living room on laptops. It's not like, you know, pivoting some giant company but yeah, no, we did and, you know, initially we kind of waded into it where we were thinking, well, you know, maybe we do this kind of very niche tool for basically security reviews, you know, trying to detect future CVEs in your code or maybe we build something that's just for this one niche area of software. You know, we thought about building for quants and actually, you know, prototyped things just for quantitative researchers. But yeah, in doing that we were just brimming with ideas for what Cursor could be if it were just about trying to be the best way to code with AI in general. And then I think that we just had a ton of conviction about that and we had a ton of excitement about that and so at some point we just decided to go for it.

Host: Yeah.

Michael Truell: And that was end of 2022, right? When you decided to make that move and how quickly did you ship the first product and what did the first product look like? And that was around you shipped it a couple weeks later and what was that look like?

Host: Um

Michael Truell: It did take us a little bit of time to ship something publicly.

Host: Mhm.

Michael Truell: It took us roughly, I think, three months from first line of code to open it up and get it. Originally, what we did is we built our own editor, quote unquote, from scratch.

Host: Oh my god.

Michael Truell: Still, it was still using a bunch of open source building blocks. There are a lot of great primitives like CodeMirror, and you know, the language servers, and there's a lot of open source tech that can help you build an editor, but, uh, yeah, no, it was called together from scratch. And there was our own version of remote SSH, our own Copilot integration at the time because we didn't have anything like autocomplete. You know, you have to build your own P-E-N system. You have to build all your own language server integrations. There's just a lot that ends up going into something as developed as, you know, the code editor market—you know, making something that can actually be competitive and service someone's daily driver. But it was, I think, four weeks until we built something that we could use as our daily driver. It was maybe four weeks later where we gave it to the first beta testers, and then there was another four weeks, and then we got it. And it was still very, very crude at the time. It didn't feel like a big thing to just open it up to the public.

Host: What did you learn in that first version? Because you built a code editor from scratch. You guys haven't done the whole forking yet.

Michael Truell: Yeah. And we had the fear of God in us. I mean, we had people hadn't really liked some of the things we built for a while. So I think that, you know, we were kind of all in on it and very focused. But what did we learn from that? Um, I think that we learned the first initial set of AI features where, you know, when we started, I think that there was just one key command and it pulled up this like universal remote in the editor, and then you asked it to do something. And then entirely the AI would just figure out, "Oh, do you—what, what, what exactly do you want it to do?" You know, do you want something back that's like a chat response, or do you want a code suggestion that you can then take, or do you want it to go search around your codebase and answer a question, or do you want it to go spin for a really long time or a short time? And there wasn't a lot of control. And I think that we learned, you know, given the tech of the time—um, at the end of 2022—that actually the form factor has to look a bit different. And so we learned the first early AI features that then became part of the core of Cursor from iterating both for ourselves and also giving it to people. I think another thing we learned was, you know, we were very rapidly building a feature version of what we want in a normal code editor plus then some AI stuff that we thought was great. But then, you know, a feature-complete code editor for the world is going to be a way, way, way longer road. We thought that, you know, VS Code had been developed over the course of 12 years, was one of the earliest TypeScript projects, had lots of people on it. Thought, "Oh yeah, of course, you can kind of spin something up that's just equivalent for the world in a few months." And I think that we learned very rapidly that that wasn't the reality, and our time was going to be best spent just focused on the AI stuff. And so, similar to how browsers often base themselves off of Chromium's rendering engine, we then switched to being based off of VS Code.

Host: The other thing is you guys had also implemented your own models too. Like, back then you got a lot of inspiration from Codex, right?

Michael Truell: Mhm. Yes. So when we were setting out to work on, you know, our first idea that we really spent a bunch of time on—which was trying to help mechanical engineers be more productive using AI—um, one of the things when we raised our first round of funding because we actually kind of needed money from the get-go to do a little bit of model training because you couldn't bootstrap it with the models that existed off the shelves. They weren't good enough at that task. One of the papers that we would tout around is actually the original Codex paper, um, because by our calculations, Codex—which was the first autocomplete model behind GitHub Copilot—it didn't really cost that much money to train. Even though, even back then, at kind of the beginning and middle of 2022, people were talking about how expensive AI models were to train, I think it cost—uh, my math might be wrong—but I think it was about 100K in training costs. And then, you know, during this foray into mechanical engineering, we had done our own training. And then when we set off on Cursor, I think we were a little bit burned by that. And so we wanted to be as pragmatic as possible, not to reinvent the wheel. And so we started by doing none of that. And then over the course of 2023, you know, in dialing in the product, that ended up being a really important product lever, especially as we got to scale and we got a bunch of people using the product. And then that also gives you the ability to use product data to make the product better. And so that actually has been a really important muscle to build in the company.

Host: What happened then in 2023 was when you were still not sure about whether Cursor was going to be a thing, right? You were still debating with your co-founders whether you should still pivot. It's like, "Oh, is this idea still going to work?" And you were still trying to grow it, right? Because it took a long time to get to revenue, right?

Michael Truell: Yeah. I think that over 2023, it was growing. The numbers were kind of small, and I think that also we were working on something where there wasn't always a clear next step. Um, I think that there are probably some markets where you're really well served by going immediately, talking to a bunch of people, listing down their problems really rigorously, or you know, really kind of systematically and exhaustively thinking through each problem, what would kind of be the direct solution, and then prioritizing them and then going from there. Um, but I think that we were and are in a space that's a bit different than that. You know, we're this end-user application that doesn't have much of a complexity budget. We are trying to build the best way to code with AI. And so a lot of that is figuring out, you know, given the tools that you have today, what can you actually do? There's a lot of things that you could write down that would be useful if you could build them, but then, you know, figuring out how to build them and all the details, it's not entirely clear how to move forward on that. And so yeah, there were a lot of times over the course of 2023—and then, you know, actually also to add to this—of our early user base, if you just kind of followed the gradient of exactly what they wanted, you would get pulled in slightly different directions than we ended up in. You know, we had a really loud segment of users that didn't know how to code at all, and we talked about, you know, should we focus on those folks? We had a really loud segment of users that wanted us to do things that were very tech-stack specific. Um, you know, just building for one technology and making it much less of a horizontal tool, and we resisted doing that too. There was a lot of early prototyping and, uh, kind of wandering the desert in 2023. And then, you know, figuring out things around, you know, where does it make sense to not just build the software but also build our own models to improve the API models or replace them in places like, you know, for instance, with our Tab—you know, our next edit prediction—and then how exactly to do that.

Host: You went from zero to 1 million around 2023, right? And it was, uh, it took a lot to get there, right? Um, yeah, it was a bit more than that, but sort of roughly that.

Host: And then 2024 was a crazy year. You guys went from one to 100 million in one year. Tell us about this, uh, loss of, uh, compounding power because you kept that growing 10% week over week. How did that happen?

Michael Truell: So the numbers felt small early on, then the compounding kind of kept going. I think that there were a couple of things that really drove our growth. Um, we're in this market where if you make the product better, you kind of see it in the numbers immediately. Where, you know, things start to grow more. And so we felt it around, you know, when we first started to make Cursor codebase-aware, when we first started to, you know, be able to predict your next action, when we made that then more accurate, then when we made that faster, then when we made that more ambitious—um, you know, it could predict sequences of changes—and then when we let the AI model start to take more action within your codebase and then do that really fast, you know, speeding that up. And so all along the way, um, you know, I think we kind of just focused on making the product better. The compounding continued. Um, and I don't think that this is true of all markets, but I think we're in a market where end-user preferences matter a lot. And if you make the best thing, people hear about it and talk about it. And that kept going for, you know, a long time. I think one of the funny things that has happened around that time—we did see a big shift in the YC companies as they were going through the batch. Because we would ask what kind of tech stack you use to build your applications, and it was night and day from one batch to the other. I remember in 2023, I think it was maybe single-digit percentage of the batch would use Cursor. Then 2024, it was like 80%. It just spread like wildfire. Like, the best builders were using it.

Host: Got onto their Twitter feed. Yeah.

Michael Truell: The Twitter feed. Was that where a lot of adoption? How did all the growth come from? So the very early stages when we were first launching the editor, we, uh, tried to kind of evangelize it on social networks. And actually, one of my co-founders—when kind of the dopamine hit keeping him going in 2022 when we were working on some of these ill-fated ideas—started posting on the internet and kind of explicitly set out to try to gain a lot of followers, not by doing kind of normal social media things, but by talking about AI. Actually, it was kind of surprising, you know, the degree to which someone could actually just read kind of all the papers, think kind of deeply about what was going on at the time, talk about that publicly, and then get recognized by influential people in the space. And so there was like this particular open-source model, FLAN-T5 at the time, that multiple AI efforts that ended up using that model—they found out about, you know, kind of the benefits of that model directly from my co-founder, just because he was posting on Twitter and doing that kind of consistently. But he became like sort of niche—very niche, like sort of niche, niche, niche of SF micro-celebrity. He would actually kind of evangelize the product early on. And so we had this kind of very movie magic demo, um, you know, when we first launched and when we first did a waitlist to just get our initial batch of users. I think that that was helpful getting, you know, us kick-started. But then after that, we kind of stepped away from that and we kind of lived like monks in 2023 and just focused on the product. And it really just spread from word of mouth. I remember there were a couple of times during that year where there were members of the team that would say things like, "Guys, the product's already good enough. Like, let's put it aside. Let's just focus on growth engineering." And, um, then there would be like a two-month sprint on, you know, doing some version of that. Uh, and it just never—it kind of washed away compared to the other stuff that we worked on that year.

Host: And by that time, um, in 2024, how big was Cursor? How many—how big was the company at that point?

Michael Truell: Uh, it was pretty small. In 2023, my co-founders are fantastic engineers, and so—and there were four of us—so we could go pretty far without hiring anyone. We also had our own, you know, set of missteps and figuring out the first set of people to hire and how exactly to do that. And, um, so we're both very patient early on and also, you know, focused on hiring a lot less than we probably should have early on. Um, I think we ended 2023 at only single-digit people. Like, we were less than 10 still.

Host: Yeah.

Michael Truell: Amazing. So, so—

Host: No, I guess one curious, uh, now shifting gears a little bit—about what are your thoughts in terms of how the future's going to look with, uh, coding?

Michael Truell: We were kind of this, this maybe middle road bet from the start. Where when we set out to work on the company and we were kind of hiring our first people, we would get these weird looks around, you know, "Why are you?"—I mean, at the end of 2022, it wasn't really like this, right? Because kind of ChatGPT happened, and then the whole world woke up to things, you know, beginning of 2023. But especially during 2022, when we were working on the CAD stuff and then the early code stuff, um, people thought working on AI was—it was kind of weird to do. People were not entirely convinced that it was a good use of time and that there were going to be lots of great applications to fall out of AI. And then even the people who were interested in AI, there was—in our space, you know, a bunch of people that were just focused on optimizing kind of the form factor that existed already and just making those products a little bit better. And then at the same time, you know, in our social circles and professional circles, there's a bunch of people that, you know, we're thinking, "Oh, why would you work on anything other than AGI?" And, you know, all of the work that you're doing right now, in one or two years, you know, circa 2022, is going to go away. And yeah, I think that we've always had this view that there's going to be lots and lots of incredibly valuable things to build over the next couple decades. AI is going to be this transformative technology, uh, maybe more so than, you know, any revolution in recent technological revolution in recent centuries. But it's going to take a couple of decades. And it's going to be this industry-wide effort where there are all of these independent capabilities that each need to fall to really get to, you know, a place where you can entirely get to the end state of transforming building software on computers or kind of the other areas of knowledge work that might be transformed by AI. And yeah, I think concretely, kind of in the near term, um, we think that for professional engineers, which is the end user we serve—uh, the market that we serve—um, you know, code is still really important, and uh, there will be this long messy middle where, um, you will be working with the AI more and more. It will become like a colleague more and more. It may also become like a, you know, a very advanced compiler that can start to—

Michael Truell: Hide some of the code for you. You're going to have to read the logic and, um, yeah, and review it and edit it.

Host: What do you think are the skills that are still going to matter? What should everyone still be studying or stop studying?

Michael Truell: I mean, I think that programming, like math, is kind of just a good general education.

Host: Um, and I don't think that goes away.

Michael Truell: And I think that there's also lots of practical skills that comes from studying computer science right now. I mean, often when people are kind of entering dynamic industries, the specific stuff that they study in school isn't super crucial. It's more the kind of learning that they get along the way. I don't think that's changed with AI.

Host: What advice do you have for the audience? If you have, like, a young Michael Truell—maybe not just three years ago—they want to be like you three years ago before they start Cursor. What should they be doing right now?

Michael Truell: I think just working on things that you're interested in and doing it with people both that you enjoy being around but that you respect a ton. And taking that really seriously. Yeah, I think that for a lot of people that are in school, there's so many things that pull you toward, um, more checking boxes and less, you know, focusing on building something up over time. And really focusing on something that you're interested in.

Host: All right, let's give it a round of applause to Michael.

Michael Truell: Thank you so much.

Host: Yeah, of course. Thank you for having me.
