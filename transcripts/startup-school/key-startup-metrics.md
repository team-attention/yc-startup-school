---
title: "Key Startup Metrics"
author: "Tom Blomfield"
slug: "KR-key-startup-metrics"
series: "Startup School"
youtube_id: "_mKeVGSqQac"
youtube_url: "https://www.youtube.com/watch?v=_mKeVGSqQac"
source_url: "https://www.ycombinator.com/library/KR-key-startup-metrics"
description: "YC Group Partner Tom Blomfield discusses one of the most important elements of running any startup: metrics! Tom shares what key metrics to track and how to use them to make the best decisions for your company."
duration_seconds: 1427
created_at: "2023-12-15T18:15:30.000Z"
chapters:
  - time: 0
    title: "Intro"
  - time: 21
    title: "Importance of Metrics"
  - time: 76
    title: "Pre-launch Metrics"
  - time: 143
    title: "Metric Overload Caution"
  - time: 197
    title: "Key Metrics Selection"
  - time: 294
    title: "Consistency in Metrics"
  - time: 433
    title: "Investor Update Metrics"
  - time: 557
    title: "Retention's Significance"
  - time: 793
    title: "B2B SaaS: Net Dollar Retention"
  - time: 1010
    title: "Cruciality of Gross Margin"
  - time: 1270
    title: "Challenges of Negative Margin Scaling"
  - time: 1338
    title: "Metrics Recap"
  - time: 1362
    title: "Final Thoughts"
  - time: 1404
    title: "Outro"
has_transcript: true
---

# Key Startup Metrics

**Tom Blomfield**
[YouTube](https://www.youtube.com/watch?v=_mKeVGSqQac) | [YC Library](https://www.ycombinator.com/library/KR-key-startup-metrics)

## Transcript

Tom Blumfield: Hi there, my name is Tom Blumfield. I'm a group partner at Y Combinator, and today we're going to be talking about one of my favorite topics: metrics and why they're so useful for startups.

So why are metrics important? First of all, it's pretty obvious that with better metrics you'll make better decisions. It's like flying an airplane with no instruments. You're flying blind. You don't know what's happening to the aircraft, and you're not in control. Having great metrics is like having great instruments in an aircraft. It lets you tweak and iterate and make sure you're really in control of your startup.

We often see, and I've seen in even in the last two or three weeks, founders who've had these great launches. They've launched on Hacker News, on Product Hunt, and they've had hundreds of people come and use their service day after day. But they have no idea how many of those new users are new users or returning users. They don't know if they're daily active or weekly active. They could be churning off all of their users instantly, and they don't know at all.

So the first thing they do after launching blind is to go back and build metrics in. We would advise you: don't do that. You should build basic metrics into a product before you launch.

And as an investor, it's really easy to tell founders who are in command of their metrics versus founders who aren't. And it's really impressive when founders can talk about what percentage of signups are DAU or WAU, or what the annual revenue per user is. And we'll go into some of these in detail, but it's a big differentiator when a founder can talk so fluently about these metrics.

Before we dive in, I want to give a couple of warnings. The other extreme is also bad. So it's a founder who, even before they launched, has a dashboard with perhaps 500 metrics. Maybe they've been a product manager at a big tech company or they've just watched too many YouTube videos. But they want to make every decision in their startup with metrics. And when you have only a few hundred or a few thousand users, that's basically impossible.

You know, they want to split test everything. Should this button be blue or green? And frankly, it doesn't matter. And you don't have the volume of users or data to make those kinds of split tests sensibly.

So what you should do is certainly split test the really important decisions. You know, should the cost per user be $80 per year or $200 per year? That's a really good experiment to split test. But you know, making buttons red or green—that's not really something you have the scale to split test until you're really at the size of Google or Facebook.

A final warning: don't hide behind your metrics. You've still got to get out of the building and talk to customers. Brian from Airbnb still hosts Airbnb users in his home. It's an obsession with staying close to customers. So you can't let metrics get in the way of that.

So let's get started. You're planning a product launch in perhaps a week or two, and maybe you've not got any metrics in place yet. What do you do?

The first thing is to pick four or five key metrics to track accurately—not 30 or 50. Four or five is fine. This number will grow over time. We'll talk about what those key metrics should be in a little bit.

You should pick the most straightforward analytics solution you can operate. It might just be your SQL database, making simple SQL queries to count the number of signups. PostHog, from Winter 2020, has a great SQL analytics tool you can use on top of pretty much any SQL database. So you should check that out.

You should also agree the definitions of these four or five key metrics and stick with them. So it might not be the absolute perfect definition of an active user, but constant arguments about what your key metrics are are even worse than having no metrics at all.

So your whole team has to come together and agree that an active user is someone who uses the product every day or at least once a week or at least five times a week. It honestly matters less what the precise definition is than you actually all agree with it.

I remember so many disagreements where the marketing team said, "You know, we've sent you 2,500 new leads this month," and the sales team says, "No, no, no, they weren't qualified leads. They don't meet our definitions." And this disagreement internally just destroys the productivity of meetings where metrics are involved.

So you really have to have centralized definitions of metrics that are written down, and everyone agrees on.

So say you launched, and perhaps the metrics aren't quite what you hoped. The weekly active users aren't quite as high as you originally wanted. In that situation, founders are often tempted to pick a different metric or change the definition of those metrics. So instead of weekly active, let's go for monthly active. The number looks a bit better.

Honestly, you're only fooling yourself. In this situation, it's really, really important that you keep the definition of your metric consistent over time to see if you're improving or not.

That's why it's so hard to compare metrics between different companies—definitions just vary. So a weekly active user at my company, Monzo, was someone who transacted, who made a financial transaction at least once a week. An active user at some of our competitors used different definitions—maybe it was every two weeks or eight weeks. And so this active user account between companies just became totally meaningless.

It's important that you keep it internally consistent so you're keeping a good track of it.

So now let's talk about what those key metrics are—those four or five you should really start tracking from early on. It will vary from every company. Back in the early days of the internet, companies like to use metrics like page views or unique visitors or something like that, because they're really, really big numbers, and startup founders love to report really big numbers.

You've probably heard the term "vanity metrics." These are numbers that seem really, really big, and perhaps they keep increasing. They're not actually tied to the success of your company.

More recently, common vanity metrics are things like GMV, or gross merchandise value. That's the total dollar value of goods that are sold on eBay, rather than eBay's revenue itself. Or gross transaction value for a fintech like Monzo. You could report, "We're transacting $50 billion a year." It sounds like a really, really big number. But the revenue that the company makes can be very, very different.

And so almost always, especially for B2B companies, your key metric should be revenue. If you pick another number—take gross transaction value—you'll find that your employees and eventually you might start optimizing for that number.

I worked with a neo-bank a couple of batches ago in the Middle East, and they were reporting gross transaction value. And they're very, very happy. They came to every group office hours, and their gross transaction value was growing 50% every two weeks. It looked really great, and we scratched beneath the surface a little bit. And it turned out that they were signing up much, much bigger customers who had higher transaction value, but giving them massive cashback, massive rebates to transact on the platform.

So whilst gross transaction value was rising every two weeks, revenue actually was pretty flat for about the last two months. The founders were tricking themselves. They were fooling themselves into thinking their company was succeeding when in fact it was pretty flat in revenue terms.

So revenue is the key metric I would suggest for most B2B companies. And don't hide. If your revenue isn't good, one of the most impressive founders I've ever worked with sent ten successive monthly investor update emails with zero—with a big zero—as the main metric at the top of the email. She kept herself honest. She was honest with investors, and it became clear what they needed to focus on to fix the company.

So if you're ashamed of this number, you hide it away. It's easy to kid yourself. But I think if you put it up front and central and pay attention to it, it's the right thing to focus on.

So two other key metrics, especially for investor updates: alongside your revenue, please include burn rate. That should be net. What that means is monthly costs minus your revenues. If you're loss-making—which most early startups are—it's the amount by which your bank balance decreases every month. That is your burn rate.

And your runway is a function of that. So say you have a million dollars in the bank and your burn rate is $100,000 a month. That means you have ten months' runway. That means in ten months, you're going to run out of money, and the startup will be bankrupt.

Those three numbers—revenue, burn rate, and runway—are absolutely crucial to include. And if they're not at the top of your investor updates, honestly, I always assume this founder has something to hide.

For consumer companies, we have a separate video diving deep into the metrics that are important for those kinds of startups. And often revenue is very important. But for the earliest days of consumer companies, often you're trying to get some kind of critical mass or network effect. And so growing the active user base in the early days for a consumer company might, in some cases, be more important than revenue.

So we've talked about the main three metrics that should be at the top of every investor update: that's revenue, burn rate, and runway. Now we're going to dive a little bit deeper.

One of the most important metrics for all startups, really, is retention. This is the idea that if you sign up a hundred paying customers—say you sign them up in January—how many are still paying you in February, March, and April? Two months, three months, four months later? That's your retention rate. So it might be 80% or 70%. It's a sign that people love your product, they keep coming back, and they keep paying for it.

So you can measure it for all customers who signed up in January and the subsequent months, and that's your January cohort. And then you measure the same for all of the customers who signed up in February—that's your February cohort. And you can stack these cohorts on top of each other.

And there are a number of different ways of graphing this. You might have a heat map, and some analytics tools do this really nicely. You might have a curve that sort of decays over time. Those are two pretty common ways of graphing it. And we'll show some examples. But I'd like to suggest a third way.

This is when it really clicked for me. I'd heard everyone tell me that revenue was really, really important, but it only really clicked for me after I worked at a dating startup that actually had very bad retention and ultimately failed, sadly. But it clicked when I stacked these cohorts on top of each other.

So you see the January cohort at the bottom, and then the February cohort, and then the March cohort, and the April cohort. And what happens if you have sticky cohorts? If your retention is really high—you know, 80%, 90%, 100%—is you cohorts stay really fat over time, and you build up this layer cake.

So you can imagine what happens two or three years later if you have dozens of these monthly cohorts stacked on top of each other. They're all paying you money. They're all contributing to your revenue every single month, even three years later. And if you're in a low-churn business, it adds up to a layer cake that looks something like this.

So this is an eighteen-month graph of monthly cohorts. Each month you're adding a new layer on, and after eighteen months you've got eighteen cohorts still paying you. This was like my first company, GoCardless. It was a recurring payments company, very similar to Stripe. And with those kinds of companies, people implement a payment solution once. They don't really like to change it every month—there's a lot of effort. So the customers are very, very sticky.

And you can imagine the team at GoCardless goes on holiday, you know, for a month after eighteen months, and the revenue stays pretty consistent. The beauty is actually expanding revenue. So if those customers you signed up in January launch and grow with the company—they're using GoCardless or Stripe as a payment processor—they're transacting more volume in year two and year three. They're growing their business. The revenue for Stripe or GoCardless actually increases as well.

So the team perhaps goes on holiday or signs up no new customers. The business still grows revenue. That's the beauty of this high-retention business. It's sort of growing constantly underneath you. You're adding these layers and layers and layers of revenue, and eventually become unstoppable.

But that only happens if your retention flattens out at some point. If these decay curves flatten out at some point, and it almost matters that they flatten out at any point as opposed to a high point. You know, I take a 20% retention that flattens out over a higher retention initially that goes to zero.

Because if you sign up a hundred people in January and by month three or month six they've all churned off—they've all stopped paying you—you get a very different layer cake. That lovely flat layer cake that builds up and up over time, if your customers all churn out, looks like this.

So you can see customers you sign up in month one, by month three have more or less gone. And let's fast forward to month six—they've all gone. By month nine or month ten, and so rather than building up secure and steadfast layers month after month, you're actually scrambling to fill up a leaky bucket. You're pouring water into the top of the bucket, and it's leaking out of the bucket just as fast as you can fill it up.

You can imagine this is an impossible task. And so if your business has customers that don't retain—where retention goes to zero—you'll reach some natural plateau where you're working as hard as you can to fill up the customers who simply churned out last month. And it's very, very hard to build a big business like that. It's a futile endeavor.

So we talked about overall retention. For B2B startups, people often talk about net dollar retention. This is just a fancy way of calculating retention mostly used in B2B SaaS companies.

So let's take an example. We've started an AI customer service chatbot—very in vogue at the moment—and say we sign up ten paying customers in January in the first month, and they're each paying $10,000 a month. So 10K each. You're at $100K of monthly recurring revenue. Feels pretty good, right?

Let's fast forward a year, and in each of those subsequent months you'll have signed up more customers. Let's ignore them for now. Focus on those ten initial customers you signed up in January. But fast forward twelve months. Perhaps two of those customers have canceled their contracts at some point in the year, so we're down to $80,000 of monthly revenue from that cohort.

But you've also upsold three customers. Perhaps you've introduced some new functionality, or they're using it more, and instead of paying $10,000, they're each paying $20,000. Perhaps you do phone chat as well as text chat. So that's $30,000 of additional revenue.

So we've lost $20,000 but gained $30,000. So that's net $10,000 plus. So $110,000 of monthly revenue from that January cohort. That's why it's called net dollar retention. It's the amount you've gained that's netted off against the amount you've lost.

So that cohort that was making $100,000 at the start—in January of year one—a year later, January of year two, is making $110,000. That's equivalent to 110% net dollar retention.

So a net dollar retention above 100% means your cohorts are growing over time. If your net dollar retention is below 100%, they're shrinking over time. You've got to pour more water into the funnel to fill up the leaky buckets we talked about.

And that's what gives very sticky businesses like Stripe, like GoCardless, like PayPal this exponential growth. It's adding new customers every month, but having existing customers grow underneath them as well. And that gives you this exponential growth curve that's very, very impressive.

The final thing: as a benchmark, any early-stage B2B SaaS company should be looking at net dollar retention well above 100%. This is for several reasons.

First of all, you've probably underpriced your product with your initial launch. So you might charge $10,000 a month for your initial customers. You realize pretty quickly that the product could be sold for $20,000 or $30,000.

Secondly, you're adding features all the time, presumably. You're improving your product. And so that makes it more appealing, and customers are willing to pay more money.

Thirdly, you should be getting it better.

Speaker: At sales and upselling over time as well. It'd be weird if you weren't getting better at that. And so those three reasons, net dollar retention for early stage B2B startup should be 125% to 150%. That would be great, even higher than that. For mature companies in the same range, 110% to 120% is pretty good. Net dollar retention—if your net dollar retention is below 100%, especially for Enterprise B2B SaaS, something is wrong. You are churning off customers. They don't love the product. And I would invest in fixing that, talking to customers and figuring out why they're turning off, rather than trying to shove more customers in the top of the funnel by investing in sales and marketing, for example. Net dollar retention is absolutely crucial for B2B SaaS companies.

Speaker: Okay, the second deep dive we're going to do on B2B metrics—and this is applicable to consumer companies as well—is gross margin. Gross margin is your revenue, the money you get from customers, minus the cost of goods sold. So you can imagine that if you're a grocery store, that's most obvious. You're selling sandwiches, for example. The cost of goods sold is the cost of the bread and the cost of the butter and the filling that goes in the sandwich. That's cost of goods sold. For a software company, it's any cost that varies per customer or for each incremental customer you incur more cost.

Speaker: So let's go back to example we had earlier. We were running an AI customer service bot, and you're probably using something like OpenAI or Anthropic to power the core model behind that. And so the cost—the credits that you pay to OpenAI or Anthropic or someone else—is your cost of goods sold. We didn't use to talk about this very much for B2B SaaS companies because the cost of goods was very, very minimal. For pure software, it might have been your AWS bill or your bandwidth bill or something like that. It's minimal. And so pure B2B SaaS companies in the past might have had gross margins of 95%. You know, you sell $100 worth of software and it's only $5 of cost. And so people just assume it's very, very high margin.

Speaker: But these days, as software sort of takes over more and more industries, gross margin has become more and more important. So for AI companies today, the gross margin—the amount they pay to OpenAI or Anthropic or others for the foundation model—is a really important cost. And by the way, just because you're getting free credits doesn't mean that that's a cost that doesn't exist. It just means you're hiding it for the moment. So companies that hide behind OpenAI credits and claim that they've got these huge gross margins have a nasty shock coming when those credits run out.

Speaker: It's also why heavily operational businesses are so tricky. And when a company joins YC with something like a grocery delivery business or really any kind of business where a lot of humans are involved, a lot of operational processes going along—you maybe paint houses or install heat pumps or something—you have to pay a lot more attention to the gross margin because it's very rare that it's as high as 95%. You might be down at 5%, 10%, 15% gross margins, which means you have to do a lot more work. You have to get a lot more customers, a lot more revenue to generate the same gross margin. And that gross margin is the thing that can then pay your head office rent, your engineering salaries, all of those remaining costs that don't vary per customer but still have to be deducted before you get to profitability.

Speaker: And so for operationally intensive businesses, we often try to work with founders to see if there's a software-only version of their business that they can run at a much higher margin. So for example, instead of running a delivery company where you have vans and bikes and delivery people, instead can you take the software that powers all of that and sell it to other delivery companies? You're going to have a probably a much easier life. Certainly, you're going to have much higher gross margins if you do that.

Speaker: So in the zero interest rate environment—sort of 2010 to 2021 period—companies were scaling negative margin businesses because capital was so cheap. Famously, Uber did this. They used capital as a weapon. So they took these businesses that were initially negative gross margin. That means they're effectively selling $10 worth of service but only charging $9, so losing money on every single order, but trying to get to a sort of a network effect or a tipping point. For Uber, famously, it was a certain number of drivers, certain density of drivers and riders in a certain city that gets the flywheel going. But when they launched in a new city, they didn't have that density, and so they had to subsidize drivers and subsidize riders, which made it a negative gross margin business.

Speaker: And so they raised enormous amounts of capital to expand across the globe before competitors could catch up, but burnt tens of billions of dollars of invested money in doing so. And that blitz scaling approach, that scaling of negative margin, got popular with founders. And so we saw it in ride sharing, then we saw it in ten-minute grocery delivery, we saw it with electric scooters. And honestly, there's like a whole wasteland of startups that tried to do that and then realized they couldn't continue to raise money as investors just didn't want to keep subsidizing these businesses. And certainly now, with much higher interest rates, capital has become much more expensive. Investors are really, really loath to invest in negative margin businesses, and it's much, much harder to scale those negative margins.

Speaker: We did this at Monzo. So Monzo was an online bank in the UK, and for our first half million customers or so, we were losing money on every customer—30 or 40 pounds per customer. We scaled to more than half a million of those customers. It costs a lot, but we had a plan to turn it around. So we brought technology in house. We didn't rely so much on external vendors. We introduced charges for certain things. We introduced new products that customers were happy to pay for. And over time, we flipped those negative unit economics. So rather than losing 30 or 40 pounds per customer, we ended up, when I was there, making 30 or 40 pounds per customer. And now three or four years later, Monzo is profitable.

Speaker: So if you start with negative unit economics, you really, really have to have a plan to fix them. And I would really advise you: don't scale your customer base, don't try and grow as quickly as possible whilst you have negative unit economics. You fix them first, and then you scale.

Speaker: Okay, we covered a lot of stuff today. So as a recap, we talked about revenue and why it's the best core metric for most B2B companies. Then we talked about retention and its fancy cousin, net dollar retention, and why having a net dollar retention above 100% is so important for B2B startups. And we finish with gross margin and why it's so important not to scale businesses with negative gross margins.

Speaker: I wrap up with some final thoughts. Make sure you're tracking your four or five key metrics before you launch. Don't launch without metrics in place. It's like flying blind. Be rigorous in what you track. Track the right metrics. Don't fall for vanity metrics like gross merchandise value, your impressions, or unique users. Have a clear definition of each of your metrics and a central way of measuring them in your company to avoid those pointless arguments that derail meetings.

Speaker: Don't hide behind your metrics. You can't split everything, especially as a small startup. So a lot of these decisions just have to be made by talking to your users and using your product intuition. You still have to get out of the building and talk to customers. That's so important. So I hope that helps: run your startup with the right blend of metrics, talking to customers, and product intuition. Those three are a vital blend. Thanks for watching today.
