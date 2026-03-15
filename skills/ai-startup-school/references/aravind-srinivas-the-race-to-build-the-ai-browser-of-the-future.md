---
title: "Aravind Srinivas: The Race to Build the AI Browser of the Future"
author: "Y Combinator"
slug: "Mg-aravind-srinivas-the-race-to-build-the-ai-browser-of-the-future"
series: "AI Startup School"
youtube_id: "2jOnoTEk-xA"
youtube_url: "https://www.youtube.com/watch?v=2jOnoTEk-xA"
source_url: "https://www.ycombinator.com/library/Mg-aravind-srinivas-the-race-to-build-the-ai-browser-of-the-future"
description: "Aravind Srinivas started Perplexity with one goal: to rethink how we search, browse, and interact with information online. In this fireside, he shares the journey from hacking together a natural-language-to-SQL search tool to building a product used by millions around the world."
duration_seconds: 2593
created_at: "2025-07-11T14:37:45.000Z"
chapters:
  - time: 48
    title: "Perplexity's Current Status and Challenges"
  - time: 76
    title: "The Browser Bet"
  - time: 198
    title: "Competition and Market Dynamics"
  - time: 283
    title: "The Importance of Speed and Innovation"
  - time: 351
    title: "Founding Perplexity: The Early Days"
  - time: 558
    title: "Product Evolution and User Experience"
  - time: 1184
    title: "Running the Company and Future Outlook"
  - time: 1215
    title: "AI Tools in Software Engineering"
  - time: 1231
    title: "Adoption and Implementation of AI Coding Tools"
  - time: 1271
    title: "Challenges and Benefits of AI in Development"
  - time: 1355
    title: "Brand Value and Competition"
  - time: 1436
    title: "Network Effects and Integrations"
  - time: 1660
    title: "Business Model and Revenue Streams"
  - time: 1794
    title: "Advice for Founders"
  - time: 1893
    title: "Audience Q&A"
has_transcript: true
---

# Aravind Srinivas: The Race to Build the AI Browser of the Future

**Y Combinator**
[YouTube](https://www.youtube.com/watch?v=2jOnoTEk-xA) | [YC Library](https://www.ycombinator.com/library/Mg-aravind-srinivas-the-race-to-build-the-ai-browser-of-the-future)

## Transcript

Host: YC's next batch is now taking applications. Got a startup in you? Apply at y combinator.com/apply. It's never too early and filling out the app will level up your idea. Now, on to the video.

Host: You have to innovate. You have to move faster than everybody else. And it's like running a marathon but at an extremely high velocity. Right. The only mode you have is speed. I read all the Twitter comments every time. Google IO last year was AI overview and Perplexity is dead. This year was AI mode and Perplexity is dead and I read all of that too and it's it's always fun. I love it actually. Aravind, I see you every I don't know two or three months and you give me an update on the latest on Perplexity. Why don't you just tell these folks where you're at? How are things going? Do people use Perplexity?

Host: Do you guys use Perplexity?

Aravind Srinivas: Well, whether you believe it or not, like I have infra issues every day. So there are a lot of people using it and this usage is actually growing to the extent that we don't actually know how to deal with it. We have to rebuild the infra to scale the next ten X. So definitely a lot of people in the world using it. Thanks to all of you as well. What is next for us? The browser. That's the big bet we're making as far as the future of the company goes. Everyone here is like why should I use Perplexity when there's search and other AI apps? Of course ChatGPT has a bigger distribution than us. Every other AI app is trying to put search as a layer in it. All of them support citations. A lot of them support some of the verticals we put work into, yes. Like we're always going to continue to remain better than others in that category, but I think the browser and agents are truly the next bet that we want to make. We think about it as an assistant rather than a complete autonomous agent, but one omni box where you can navigate, you can ask informational queries and you can give agentic tasks and your AI with you on your new tab page, on your site card, as an assistant on any web page you are, makes the browser feel like more like a cognitive operating system rather than just yet another browser. And we hope to make it like a cloud where you launch several tasks in parallel that are running asynchronously.

Aravind Srinivas: Okay. And pulling all your personal contacts, your email, your calendar, your Amazon, your, you know, all sorts of social media accounts that you have and you go and do research on real estate, the markets, and these are all like just processes running on your browser. That's never been possible before. And Chrome was exciting when each tab was its own process. You think about each query or each prompt could be that.

Host: And that will be your new browser, Comet. So we're putting all our energy into that.

Host: This was going to be the hard question I saved for the end, but since you queued it up, I'll do it right now. Um, I think if Sam Altman were still on the stage today, he would say, "Oh yeah, that's what we're doing." Um, and I think Sundar at Google probably would say that's the direction we're headed as well. So it feels like there are a bunch of players now, many of them very well funded, going in generally the same direction. How do you see the world? Like do you think that it's going to play out where there's actually like a bunch of different use cases and you can own a very important one that others won't want to own or are we in for like a major competitive battle?

Aravind Srinivas: Look, if something is really worth doing, it's only natural that people with a lot of funding will go and do it. Um people said Perplexity is a great product. Now everyone is trying to do something that can answer any question with sources. Cursor was a great product. Now OpenAI is trying to buy Cursor's competitor. Anthropic launched Code Expert. Uh, like Claude Code. Google has its own like rival tool. So it's only natural that when there's a lot of money to be made in a certain sector, people are going to try to copy it. And there's only a limited amount of things you can be world class at, whether it's being building great models or building one or two really good products. So you're obviously not going to win on everything. For us, this is the only thing we care about: accuracy at the level of answers, accuracy at the level of tasks, orchestrating all these different tools. The browser is much harder to copy than like yet another chat tool. That said, I'm fully working with the assumption that OpenAI will also build its own browser. Anthropic will also try to build its own browser. Google already has one called Chrome. So it's completely reasonable to expect them to do it. And the only mode you have is speed. You have to innovate. You have to move faster than everybody else. And it's like running a marathon but at an extremely high velocity, right?

Host: Yes. Yeah. I I really agree with your statement that like you can only focus on one thing and be world class at one thing. And just to give you guys like a little glimpse into it, we were backstage before this talk and he was showing me some of the new stuff that they're working on and there was like a bug, right? And he stopped everything he was doing to like figure out what was wrong with this bug. Why was it not doing the right thing? And if you think about like what would the CEO of a large company do in that situation? Probably they would like hand it off to somebody else on their team. So that's like a good piece of evidence that you actually mean what you say.

Aravind Srinivas: Yeah. I I love triaging and fixing bugs. I know it sounds trivial. Like is that the best use of the time of a CEO? There are a lot of people who would think otherwise. Recently people are like uh oh, like, there I hope this behavior is rubbing off on others. Like I've noticed even Sundar is doing bug support on X right now. So.

Host: I'm happy that like you know that that's setting a good example.

Host: Great. Okay, let's go back to the beginning. Like most of the folks in the audience here are either students or recent grads or grad students. Um and I think hearing your story of like how you started Perplexity would be really interesting to them because it's probably exactly the world that they're in now.

Aravind Srinivas: Yeah.

Host: Tell us how you got started.

Aravind Srinivas: We started the company without actually having a clear idea of what to build, which is the opposite of what YC advises, which is start from a project and turn it into a company. I really think at this point in time when AI is improving so fast, you don't have to rigidly stick to any one idea when you're getting started, but the most important thing is you don't change the idea every week. Like that you shouldn't do either. So start with something like brainstorm, think about it and then try to immediately build it and get it in the hands of people. Uh one tool that we were building was natural language SQL, which we actually thought about it as a search tool searching over relational databases. I allowed Twitter search, but it never, like, like the original version of Facebook Graph Search. I allowed that when I was much younger. So I wanted to like rebuild that but using language models. Um and I love Twitter as a platform. So there's no good way to search over Twitter. There still is no good way to search over Twitter. But at least at the time, we organized the entire Twitter's data in the form of like relational tables and just converted every user's query into a SQL query and ran it against the database and it was really, really good. And um that's what got us started. But at some point we figured it's better to like scale this across the web and we cannot make every website in the form of tables and neither is it actually easy to answer all sorts of questions. So we bet on the fact that language models can do all the reasoning and parsing and like structuring later, but the more important thing is to start with something more unstructured and that ended up becoming Perplexity.

Host: Got it. Um and maybe one step before you actually left to go start the company, like how did you find your co-founders? How did you decide that machine learning and AI was like the area you wanted to focus on?

Aravind Srinivas: Cuz that was the only thing I was good at. I was not good at anything else.

Host: Okay.

Aravind Srinivas: So what's the point in starting a company? I cannot start a delivery company or a social media company. Like I'm not I'm not the right fit, right? Uh the only thing I knew was AI and machine learning. In fact, it's funny. We started an AI company, uh but we're not made fun of like not even training our own models. Like most, but only the foundation models are stuff we don't train. We train so many different models, but uh that's the extent to which you need to have the intellectual humility to know like what you're good at, what is actually doable for you within with the resources that you have access to. And the co-founders are like people I like, like I knew from grad school, so we had been talking and discussing ideas for a long time. And um I think grad school is a great way to like uh you know like like identify your co-founders. You don't talk to them with the you know with the long-term calculation of like oh this could be my co-founder of my future company. You talk to them because they're interesting people. And I think that's essentially the value of the Y Combinator network. So even if your first startup year fails, you get access to a lot of amazing people and maybe they could be your future co-founders. So that's essentially what grad school was for me.

Host: Yeah, that's awesome. Um, okay. So you launched this first version of Perplexity, which is largely to like do Twitter search effectively. Um.

Host: At what point did it like start to work and you maybe internally felt like, oh, we should keep working on this. This is going to be something to explore.

Aravind Srinivas: Yeah. So whoever we gave early access to, they were all very excited about it. They kept using it repeatedly. I think there's a phenomenon in products where there's an initial wow factor.

Host: Yep.

Aravind Srinivas: And then mostly either drops completely. That means you never had real retention, or it it definitely drops but there's sustained usage. So when we saw that for the relational database searches like Twitter, LinkedIn, GitHub, we knew that we had like there was something magical about combining large language models in search. But then what we did is like we dreamt bigger and said what if we just give answers and cite the relevant sources. We launched that as a Discord bot and that was also continually being used. It was not like a one-day usage and people started ignoring it. So that's when we decided we had the courage to launch it. We launched it seven days after the ChatGPT launch, especially at a time when ChatGPT did not have web, right, web search. So that was a good moment. And I think like many of the successful AI products that people speak about today, Cursor included, all were like 2022 launches or like like early 2023 or late 2022 launches. So they're all like old people, you know, in the in the in this AI time scale.

Host: Yes.

Aravind Srinivas: For me, the aha moment was like New Year's Eve. There was like close to 700,000 queries. And I was like, okay, this has the crappiest name for a consumer product. It's called Perplexity. Very hard. Nobody even knows how to share it. And then it was so slow. Took seven seconds to answer for a query at the time. And um it was making a lot of mistakes, hallucinations, and like a no-name company, no-name founder, very one or two million dollars in seed funding. Despite that, people were caring enough to sharing screenshots and like and a New Year's Eve and you could be, you know, watching Netflix, right? So uh that's when I knew there was something real here and I started like optimizing for like, you know, committing to this vision.

Host: Okay. And at that point, like on that New Year's Eve, did you in your head think I'm building a thing that could really compete with Google and like take over a market as big as what Google offers or was it just a toy for you?

Aravind Srinivas: The first time the thought occurred to me was when um Google wrote a blog post. Sundar wrote a blog post about Bard.

Host: Like that was around the time when we were raising Series A funding and everybody said, "Okay, Bard is going to do whatever you're doing." And it's like why do I have to build Bard? Like why not just do it on Google, right, where you you have all the distribution in the world? So why do you have to build a separate product? Like just just update your core main.

Host: The best possible asset to do this.

Aravind Srinivas: Exactly. And I kept thinking it was pretty obvious. You cannot, like, if if people can get answers to best hotels to stay in San Francisco with a view of the Golden Gate Bridge or like Bay Bridge or like where can I stay in New York like next to the Central Park with good amenities or like which flight is the best thing for me to take to fly from SF to London. If you get direct answers to these questions with booking links right there, how are you going to mint money from Booking and Expedia and Kayak and like, you know, or like same thing for shopping. How are you going to take money from um Amazon and like Walmart for the same ad where they're all bidding against each other? It's not in their incentive to give you good answers at all. So that's when I realized that they have to build a separate product, but they can never capitalize on their core distribution. And 2024, 2023 especially, and a large part of 2024 too, Google had like maybe the fourth or fifth best models at any moment. So as a startup outside Google, you had access to AI that was better than what Google internally had, which was unprecedented, right? Until then, if you had to compete with Google and you had to build something that needed a lot of AI in it, good luck, right? Like cuz you never have an AI outside Google that's even equal, leave alone being better. But now it's a completely reversal of the situation thanks to OpenAI or Anthropic or open source models. So that plus innovator's dilemma plus the fact that we could make a lot of mistakes and it's fine, whereas for Google, one mistake tanks their stock. Like you remember the live demo of Bard where it failed and the stock went down six percent.

Host: Yep.

Aravind Srinivas: So we knew that there was a lot of advantages for us.

Host: Yeah. And I heard you talk about this recently, but you know Google specifically has been trying to build Perplexity-like experiences and you know you.

Aravind Srinivas: AI mode.

Host: Yeah. They just like change the name of it each Google IO and then not really.

Aravind Srinivas: True. I'm not I'm not like saying something wrong.

Host: Yes. Right. So it's like I I.

Aravind Srinivas: Look, it might sound a little um cocky to say that, but it's true. Um the same feature is being launched year after year after year with a different name, with a different VP, with a different group of people, but it's the same thing, except maybe it's getting better, but it's never getting launched to everybody.

Host: One of the things I I've come to admire about you is you really have a focus on the user experience and and you told me how you kind of learned that from Larry Page. Yeah. By reading the book about uh Google. Um why do you think Google has lost that ability?

Aravind Srinivas: Well, it's a much bigger business, right? And it's not founder anymore. Uh it's hard to take risks. Um I think they have great people. Nobody, like, no one in this audience would think Google has incompetent people. I think they're like really great engineers. It's largely the incentive structure. It's hard to like you know take a hit on your own stock and do the thing that's long-term correct. So.

Aravind Srinivas: You know, honestly, I'm happy that that sort of dilemma exists because otherwise where is the opening for startups, right? And if startups can succeed, then it's going to be monopolies getting bigger and bigger, and that's not great for the world. I actually am very happy that we are able to win and they're also able to ship new products, and people are like first time comparing, right? Earlier, for access to information, you would never even bother to compare an alternative to Google.

Host: It's true.

Aravind Srinivas: Like that was considered a waste of time, a joke. Now at least you're like, "Oh, I'll first go ask this app. Like, I'll ask Google or I'll ask ChatGPT or I'll ask Perplexity or ask Gemini," and then maybe you don't even ask Google anymore. You just ask the AI apps. And there are a bunch of AI assistants, and the phone makers will start offering all of them as alternatives. It's not going to be like a locked-in default search option. So I'm really happy that they're competing in a world where a monopoly hopefully doesn't exist and that creates a more fair ground for everybody.

Host: Yeah, yeah. You were also telling me backstage about, um, you know, you are facing this increased competition from a variety of folks, but if you look at your numbers, you haven't really seen an effect.

Aravind Srinivas: You know, I read all the Twitter comments every time at Google I/O. Exactly the same set of comments repeated this year. Google I/O last year was "AI Overview" and "Perplexity is dead." This year was "AI Mode" and "Perplexity is dead." And I read all of that too, and it's always fun. I love it, actually. Um, because they know that they're thinking like, "I don't even expect these things," or the people in the company are thinking "Google wouldn't build this," or something like that. But the reality is like nobody actually gets exposed to those features. But competition is real. Okay, let's assume—let's accept that OpenAI is extremely well-funded, doesn't have all these innovative DMA problems, wants to actually ship search on ChatGPT. ChatGPT is the most successful consumer AI product out there. And so competing against it is very difficult, which is why I really want to push the company more on the browser side. And I think Comet, the browser, will be an abstraction layer above chatbots. You could even imagine like, if you permit Comet, all your ChatGPT chats can be fed into that AI, and like you don't even have to worry about memory or personalization or any of these things. And it'll do a lot of new things that a chatbot cannot do: like accessing other tabs, accessing your browsing history, going and completing forms for you, like paying your credit cards, buying stuff for you, um, and being your scout, you know, going and doing all the research for you. That sort of thing—like periodic recurring tasks. I think that's the magic that the browser enables for you. And putting it into like mobile, like building mobile versions of this browser, is going to be very hard. Like, just engineering-wise, it's going to take many months. So I'm not really worried about like someone else trying to copy this. It's going to take time for anybody.

Host: Switching to a different browser is like a pretty big decision for a user. What do you think will be the very short-term things that your browser will do so much better than what I can get today in Chrome that will make me want to switch?

Aravind Srinivas: The perfect blend of AI, navigation, and agents is what we're going to offer. And um, might sound like a boring answer, but no one's done that. And there are like hundreds of millions, probably close to a billion people using AI these days. So the market's already pretty big.

Host: What's like a specific example of how I would do that, you know, if I had access to it tomorrow?

Aravind Srinivas: You can schedule your meetings. Uh, you can reply to some of your emails that you don't even want to read. You can, like, for example, let's say you're hosting a Y Combinator event and you say, "I only want to accept Stanford dropouts," and it can go through the entire list of people who applied and just filter based on who, you know, scrape their LinkedIn URLs.

Host: Filter based on whether they were Stanford and whether they dropped out or not, and then accept. Like, that level of multi-step reasoning.

Aravind Srinivas: Is something you can uniquely do. By the way, I'm not saying that's a good filter. Uh, I wouldn't get in otherwise. And so hopefully you don't. You're more open.

Host: Yeah, we look for Deep Mind researchers also.

Aravind Srinivas: Yeah, yeah. Don't worry. Um, okay, cool. Let's talk a little bit about how you run the company now, right? I don't know if you wanted to say how many employees you have.

Host: Yeah, we have about 200.

Aravind Srinivas: Okay, so the company's getting bigger. Um, you now have access to code-writing AI tools. Um, are you guys just like all in on that stuff? Are you vibe coding everything? How what does it look like?

Aravind Srinivas: I mean, you don't want to vibe code everything, right? Like, we frequently run into infra issues and you don't want a vibe coder right there fixing it on live things on production. Like, I do want like people well-trained in regular software engineering, infrastructure, distributed systems. Like, you don't want to replace these skills. But yeah, front-end design—that's where we are seeing tremendous adoption. Like, Cursor is being used by everybody. Uh, we made it mandatory to use at least one AI coding tool, and internally at Perplexity it happens to be Cursor and like a mix of Cursor and GitHub Copilot. But yeah, we definitely made it compulsory. And so the way machine learning people are doing it, AI people are like, sometimes they read a paper and they can just upload a screenshot of the pseudo code and uh ask Cursor to like just edit the files to implement this new algorithm. And then it's able to like uh write it on unit tests and then uh run an experiment pretty quickly. That uh is reducing the experimentation time from like three or four days to like literally one hour. Or like, there are people who don't know design. And so sometimes I just give them feedback where I take a screenshot of my iOS app and I say, "This button needs to move here," with an arrow, and they upload my screenshot to Cursor and then ask it to like write a change to the SwiftUI file. So that level of change is incredible. Like, the speed at which you can fix bugs and ship to production is crazy.

Host: The more bugs there are, as long as you can fix them fast.

Aravind Srinivas: Yeah, bugs are always ahead of like how fast people can write code, though.

Host: But just to be clear, I'm a big fan of all these tools, but it is also introducing new bugs, and many people don't know how to fix them. And they don't even know how the bug got introduced, and they have to go find it again. So it's not perfect. And I actually like the newer tools. Like, Claude Code seems to be far smarter than like what Cursor is able to do. So I'm actually like really positive that this is the right future, but there are issues right now.

Host: Yeah.

Aravind Srinivas: Yeah. Um, in talking to a lot of the folks here, one of the major questions that I've heard is um, as these coding tools get better and better and better, what is the like actual enduring value of a company like yours if increasingly it's easy to replicate what you have done using these tools? What's your take on that general type of question?

Aravind Srinivas: I mean, brand definitely has a big value, right? Like, there are Cursor competitors, Perplexity competitors. Like, OpenAI will have their own Cursor. OpenAI has Perplexity within ChatGPT. That did not kill any of these companies. So there is a certain brand value that, once you acquire at the scale of like several millions of users, paying users, you don't actually die that fast. You earn the right to survive and keep building. Uh, so brand is important. Uh, narrative is very important to the brand. Like, you have to communicate to people why do you even need to exist? For us, it's the focus on accuracy. Okay, let there exist 100 chatbots, but we are the most focused on getting as many answers right as possible. We focus on speed, time to first token on app or web. Like, we're still the fastest despite doing search. Uh, we focus a lot on like how we present the answer. So there are some things you are obsessed about because you care about it, and that becomes your narrative and your brand identity. And if you manage to get reasonable amount of distribution—not saying 100 million users, but tens of millions—then you earn the right to keep playing the game no matter what other people ship. Until then, it's definitely a challenge. You have to worry about it. Even now, we worry about it, and the only solution is to move fast and keep shipping.

Host: Beyond brand, like, do you think about any network effect types of things emerging with Perplexity?

Aravind Srinivas: I mean, brand has network effects, right? Like, people tell each other about the brand. But no AI product has within-app network effect. Like, it's not like WhatsApp where if you build a WhatsApp rival, Meta has a definitely like a questionable brand, right? Like, people don't necessarily trust Meta's products. They think like these are ad products. Despite that, nobody's able to switch off WhatsApp that easily because all your contacts, your groups, everything is there. AI doesn't quite have that yet. Uh, mainly because you can easily export your ChatGPT history, upload it somewhere else or uh things like that. I think the browser will definitely be one play to like, you know, figure this out because as your browsing history, and like, which again you can still export but not the same as just getting a dump, a CSV dump. Uh, and your passwords, your wallet, your agent remembers you. There's a lot of tasks that are running on the browser that you rely on your day-to-day life and work. That's one way to like get the product a lot more sticky and like create more network effects, especially if multiple people rely on the same set of tasks you're sharing it with them. That's one way to get all this into like the next level.

Host: It also sounds like a lot of the stuff that you aspire to solve for users requires integrations or partnerships or something with a bunch of other companies in the world. Yeah. And if you can get those to be good, then there is somewhat of a network effect in the sense that your product will be good, and some competitor would have to build the same integration or same deal with these providers.

Aravind Srinivas: What does that look like, do you think, in the future? Like, does Perplexity do deals with all the airlines in the world and all the hotels and all the e-commerce providers?

Host: So we already work with Seelbooking. Uh, they power all the hotel bookings natively done on Perplexity. We work with TripAdvisor to surface all the reviews of hotels and different, you know, places. We have like collaborations for the maps. We work with Yelp. Uh, we also, like, you know, for shopping, we have a lot of merchants who are directly selling on us. Uh, and then we work with Firmly to like support the bookings—like native purchases. So there's already a lot of partnerships. Shopify is one of our partners. On finance, we work with FMP. Sports, we work with like uh Stats Perform. So there's a lot of data providers already working with us on these verticals, and we just think it's going to expand further as agents start to do things. Different people are okay with like becoming MCP servers. Some people are not. Some people just want to like preserve their websites. The browser agent will be generic enough that it'll respect whatever the third party wants because, at the end of the day, the agent is the one that's being permitted by the user to act on their behalf. And um, if there is no MCP server, it's still fine. You can just use these tabs as if the user would have done it. And uh, that's the key advantage of the browser that you do not have if you commit entirely to just the MCP vision. If you commit entirely to MCP vision, you require these third-party MCP servers to work reliably. Uh, the data that they send you with the MCP protocol has to be perfect. Your chatbot has to like, you know, deal with all these issues that exist. On the other hand, if you just ground-up design it as the way a human would use that website, you have full control over like how to do it. You don't have to rely on someone else doing the engineering well on their end.

Host: Um, let's talk next about business model. Your main competitor, Google, their business model, as you've talked about, is selling ads. Um, and you think that prevents them from being really good at what you're doing. So what will your business model be and how will you get it to be on the order of magnitude of Google's?

Aravind Srinivas: I don't know if you'll ever get order of magnitude profits as Google. Uh, just to be clear, and I don't think that's needed. No one in the history, even Google themselves, never has had another business that had the margins that Google has. So it's completely reasonable to get something far, far better than any public company out there right now and still be way below Google. Number two, I think the subscription revenue is like really encouraging. We never expected to get this far, and then we think like we can grow at least, you know, a few billions a year in just subs, which is a great business. Usage-based pricing, where people are paying an agent for completing a task or people have recurring tasks, and they pay based on, you know, every single use of the task, and they normalize this system based on like how much it would take to hire a person to do that for them, uh, is going to be a thing. I don't exactly know how it's going to play out, what are the margins going to be on that? Potentially, it's going to be way better than um subscriptions in terms of volume of people who would pay for it, but it might be lower margins because it's usage-based. So you're still going to be spending on all those queries. Someone might be paying a subscription to like one of these AI apps and might not have used it for an entire month. And so that's good margins on that user, right? So I don't actually have a clear sense of how this is all going to like evolve. But all I know is subscriptions and usage-based pricing are going to be a thing. Transactions, you know, uh, if people start buying more through AIs, taking a cut out of the transactions is good. It's going to be CPAs. Have historically been way lower margins than CPCs, which is why Google never became a transaction platform. Which is why I said like you're going to make a lot of money here. You may never make as much money as Google.

Host: Yeah, Google's business model is potentially the best business model ever. Ever. So, yeah, it's fair to not. Maybe it was so good that you needed AI to kill it basically.

Aravind Srinivas: All right, let's, we're going to do some audience Q&A in a little bit, but um, before we get there, I kind of wanted to understand your advice for the folks in this room, right? Like, if you were in their position back, whatever it was, four years ago, what would you advise they do?

Aravind Srinivas: I would say uh, work incredibly hard. There is no substitute for it. Don't think like you're very smart, like strategizing the right way to build a company despite all like what big model labs are doing. You should assume that if you have a big hit, if your company is something that can make revenue on the scale of hundreds of millions of dollars or potentially billions of dollars, you should always assume that a model company will copy it. Mainly because they are really looking for revenue. They raise like tens of billions or close to fifty billion, and they need to justify all that capex spend, and they need to.

Aravind Srinivas: to keep searching for new ways to make money. So they will copy anything that's good. I think you got to live with that fear. You have to embrace it and realize that like your moat comes from moving fast and building your own identity around what you're doing because users at the end care. Like when you're trying to get like a specific person for your house help, you are searching for that specific person, and you're not like going for a general agency that handles all of it. So I think there's like real benefit from embracing that fear and like sleeping with that fear and waking up every day and like feeling excited about what you're going to build because that's the only thing that'll keep you going.

Host: Well, you guys are the perfect example of how it's possible to go up against somebody as big as Google. That's great.

Host: All right, let's do some Q&A. We'll start on the left side here. Go for it.

Audience Member: Hi, my name is Sammy and I just want to personally thank you for helping me get a 100 in my theory of knowledge course. I would not have been able to do it without you. No shame. Um, quick question for you. You know, with your recent partnership with Nvidia to ship AI models across Europe, there's been talks about Perplexity being installed on all Samsung phones or pre-installed. And that could lift your valuation towards 14 billion according to sources like Bloomberg. It's a heavy responsibility being the default search engine for you know the mainstream population. What do you think are the most important factors at Perplexity to prevent hallucinations or incorrect data from you know being given to the masses? Thank you so much.

Aravind Srinivas: Thank you. Hallucinations is something we really care about. We're building benchmarks internally to keep up to date with that. The only way there is to keep building a better search index. Keep capturing better snippets of all the web pages. And then like these models, you know, are getting fast enough that you can have them reason multistep for every query without incurring too much cost, and so that's another way to reduce hallucinations.

Host: I want to ask you about like the innovator's dilemma. So if you were in Sund's shoes or in like the Google co-founder's shoes, like what would you do and how would you kind of come up with maybe changing their business model even if it's a worse model?

Host: So if you were running Google competing against yourself, what would you do?

Aravind Srinivas: I don't envy that job at all. I nobody in the world wants that job. It's a very difficult job.

Host: Would you sacrifice the business model in order to get like a new product or would you ship it as a separate product? Like if you're Google, would you just build a separate thing that is the Perplexity competitor and sacrifice the distribution advantage that you have in the short run?

Aravind Srinivas: Yeah, I genuinely don't know. I think I can say all what I want but they have more data on like what their users are doing and there are a lot of people in the world who hate AI by the way. So I think just throwing AI down people's throats on such a massive distribution area is not easy. What I would do, I definitely don't know and I don't want to be in that position also by the way. If ads are part of every AI answer you're going to hate it too. And so it's good that there's alternatives like us.

Host: All right.

Audience Member: Hey Arvin, my name is Akshad. So in a recent interview with Nikhil Kamath, he asked you for an internship at Perplexity. So I was just wondering how that arrangement is going.

Aravind Srinivas: He came to the office. He spent a couple of days. I mean he hasn't posted about it. So I'll let him post about it. But we did spend time with him. It was not a proper internship but we did speak to him for a while.

Audience Member: I want to start by saying thank you very much for your very candid answers. I really appreciated that. So a lot of startups they find some like cool application of foundation models and then they'll like build something off of that. But then if it does gain traction then the foundation models will consolidate that into their own infrastructure. And Perplexity sort of has that issue too with like a lot of LLMs adding search like ChatGPT, Gemini, companies like Cohere. So I was just wondering like how would you approach something like that? Would you try to pivot or just get better at what you do?

Aravind Srinivas: I think I would say pick something you want to like be known for. Yes there are other people integrating search but we still want to be the fastest and most accurate and obviously I cannot just say that and then stop. We need to figure out a new strategy too and build new products that don't exist yet. Our browser will be that bet for us. And browser and search are not two distinctive products. They're actually like the browser is a natural graduation step from search just like how Google graduated from Google search to Chrome. And Chrome is the main reason they got billions of daily queries from hundreds of millions. So when Google IPO'd they had no browser and they had like maybe a hundred million queries. Now you know, it's like ten billion or something. So the browser is an important part of that. And that's why we are making a massive bet on that. And agents can only be built with a browser. I'm very like convinced about that vision. That if you want to have a mobile agent that you can actually build and implement without being restricted by whatever OS rules that Apple or Google sets in terms of not being able to call third party apps, expecting every mobile app to have MCP servers and then like connecting all their data to your thing is not going to be that straightforward. Like nobody wants to be disintermediated by an AI that quickly. So the browser will be a great way to build all these things. Thank you.

Host: So as a lot of us here have done, we've tried, we've failed at our startups. You know, some of us have been more successful than others. Some like me have failed. When you're in that moment failing over and over again, what do you tell yourself as CEO or as an entrepreneur to win? To teach yourself to win?

Aravind Srinivas: What do I tell myself when I feel like I might fail?

Host: Yeah, or when you're in that very specific moment of failing where you feel like everything's crashing down on you or this feature isn't working or this bug has popped up. How do you get through that and what do you think your biggest motivational factor is in that realm?

Host: Or maybe like at the beginning before it started to take off, what gave you the hope to keep working on it versus just go back to OpenAI and get your job?

Aravind Srinivas: I just watched Elon Musk videos on YouTube. No, I'm serious. I can tell you which video. There's a video where there's like a third failure in a row and like what do you think? And he's like I don't ever give up. I would have to be dead or incapacitated.

Host: So you'd say you're also never going to give up?

Aravind Srinivas: Yeah, I hope to, I hope to like stay that way. It's not easy. I think he's done it for way longer and that's why you all like respect him. But that's, you know, there are examples of great entrepreneurs who have done this despite all the odds stacked against them. So what do you have to lose? Just keep going.

Host: Thank you.

Host: Yeah.

Audience Member: Yeah, my question is about kind of the sustainability of Perplexity, not in terms of the business model but just in terms of the web in general. You know, a lot of studies have come out recently showing that AI search engines like Perplexity drive a lot less traffic to websites. So I'm curious, what do you think like the web will look like in five to ten years when a lot of these websites, you know, they're not getting as much traffic and so they have to kind of cease their operations and like the web will just be a lot quieter of a place for content creation. How do you think Perplexity fits into that? And what do you think the web will look like in that era?

Aravind Srinivas: I think that there are going to be, you know, the web is already pretty long tail and there's a massive power loss. So I feel like the parallel is going to get even more skewed. That is very obvious. There are going to be certain brands that are well known and they're going to preserve direct organic visits. But those who are trying to game the SEO system and trying to get traffic, I think they're definitely going to have a harder time.

Host: Okay, yeah.

Audience Member: Hi Reyan, good afternoon. Firstly, where do you place the line between summarization and plagiarism in report generation? And how do you avoid IP violations in your product? And secondly, how do you deal with political bias and personal interest in news articles and other human written sources?

Aravind Srinivas: Yeah, I think there are cases where you actually have objective truth, right? Like what was the score in the NBA game? What is the live weather right now in San Francisco? Where you don't want to be wrong ever on those queries and people know what is true. But even there you're trusting, right? Like you're trusting some data provider who's tracking the live game, the TV that's showing you the number or Apple or Google's like acute weather. All these things. So at some point it all relies on trust and trust is built over time based on being accurate reliably. And so trying to surface the right data from the right people who have earned the right to like be surfaced in AI is is how we think about it for accuracy. Now there are things that don't have one clear accurate answer. I think there the best thing we can do is offer all the perspectives and not really take a clear opinion on like what is right and wrong when there's no clear answer to that question.

Host: Do you measure how accurate you are at that job by user feedback in some way?

Aravind Srinivas: We don't actually measure it today. We should, an eval set should be built for that. Like questions where there is no one objective answer. The problem with building an automated eval for that type of thing is what is the right answer? It's subjective, right? Like if there are questions about the origins of COVID and there's so many different opinions of that, relying a lot on Wikipedia as a source and you know you can say maybe for a human rater you're like okay, saying all the things Wikipedia said it's a good answer. But maybe what you want is to say stuff that is not there in Wikipedia and that relies on like having a much better human evaluators pool, much smarter people who are supposed to rate these things and they're not like available for like scale AI style evaluations, right?

Host: Right, okay. I think we have time for one final question. You got it?

Audience Member: Awesome. Hi, my name is Angela. Thank you so much for talking to us. I have a question about your go-to-market strategy. You had a great campaign for students. That's how I and assume many college students learn about you guys. But then also you had a collaboration with Costco which is a little bit different audience. So I'm just trying to understand how do you decide which audience you're trying to get?

Aravind Srinivas: I think like one perspective here is trying to get into distributions of users that you don't typically have access to on your traditional marketing channels. You know, there are a lot of people who don't use Twitter or LinkedIn and they all exist in the world. We just are living in a bubble here. And there are some other businesses that have good access to them. Like you know, traditional businesses, like like you could imagine the kind of people who use Costco regularly may not even be using AI on a regular basis. And so if that's the kind of people you're going for then it makes sense to change your strategy to reach them. But also remember that it's good to grow with adjacencies. Like you do want to have some overlapping sets of people who would be the word of mouth carriers as they help you expand to more you know, non-overlapping circles. So I think that's how I think about it. Like there should be some overlap, but your distribution should keep evolving over time. Thank you.

Host: All right, Arvin, thanks for joining us.

Aravind Srinivas: Thank you everybody.
