---
title: "How To Improve Cohort Retention"
author: "David Lieb"
slug: "LV-how-to-improve-cohort-retention"
series: "Startup School"
youtube_id: "VNxBZ7ka5J0"
youtube_url: "https://www.youtube.com/watch?v=VNxBZ7ka5J0"
source_url: "https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention"
description: "YC Group Partner David Lieb explains how to define cohorts, track active users and determine the appropriate time frame for measuring successful retention rates."
duration_seconds: 1763
created_at: "2024-08-29T17:00:32.000Z"
chapters:
  - time: 0
    title: "Intro"
  - time: 43
    title: "Cohort Retention"
  - time: 151
    title: "Key Insight"
  - time: 321
    title: "Best action to pick."
  - time: 629
    title: "What is good?"
  - time: 889
    title: "Ways to fool yourself"
  - time: 1287
    title: "Ways to improve the curve"
  - time: 1603
    title: "Conclusion"
  - time: 1745
    title: "Outro"
has_transcript: true
---

# How To Improve Cohort Retention

**David Lieb**
[YouTube](https://www.youtube.com/watch?v=VNxBZ7ka5J0) | [YC Library](https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention)

## Transcript

David Lee: Hi, everyone. I'm David Lee. I am a group partner here at YC. YC has a famously simple motto: make something people want. I think it's the purest statement of the job of startup founders, and we talk about this a lot. But what gets talked about a lot less is how do you know if you've actually done it? Did we make something people want? Today I want to go deep on the single best way that I have found to answer this question and do it in a really quantitative way, and that is cohort retention.

David Lee: So high level, cohort retention is the idea of tracking what fraction of your new users keep using your product over time. Now, this isn't a new concept. There's actually a ton of content on the internet about cohort retention. It's even built into most analytics tools that you might be using. But I bet that you don't fully understand what it measures and how to interpret the numbers. And the reason I suspect that you don't understand it is that I didn't understand it in my startup until many, many years later, when it was nearly too late.

David Lee: I remember one specific moment. I was pitching a very prestigious VC firm for our Series A, and they asked me, "Hey Dave, how's your cohort retention?" And I gave them a very hand-wavy answer. And then after the meeting, I went on my computer and I Googled cohort retention, and I realized that what I said must have made absolutely no sense. So I hope that I can save you that mistake here with this video.

David Lee: So before we dive in, quick background on me. I did YC back in the summer of 2009 with my startup Bump. Bump let you share contact information and photos with other people by just literally bumping your phones together. Bump was one of the first mobile apps to reach more than 100 million users, but it ultimately didn't work as a business. Thankfully, we did a few pivots into the photo sharing and photo management space, and ultimately were acquired by Google. Our last app, a photo management app, formed the basis for Google Photos, which I then worked on for nearly a decade. And Google Photos today serves well more than a billion users. So I've made something that a lot of people want, but I've also learned the very hard way how to know when you have not yet made something that people want.

David Lee: Okay, so the key insight, and the reason it's called cohort retention, is that we're going to track individual groups of new users, or cohorts, over time instead of trying to look at the user base or all of your customers kind of mixed together and make some inferences from that. And this gives you a much better sense of how individual users continue to use your product over time or don't.

David Lee: So to do this, we have to define three things. First, how we are going to isolate the cohorts. Then we're going to have to talk about what action we will use that counts a user as an active user or not. And finally, we have to pick which time period we want to measure subsequent usage in. So let's dive into each of these.

David Lee: So for cohorts, we have to pick a way to group new users into individual groups. The most common way you do this is simply by when they first used your product. So you might look at new users you acquire each week—so week one, then week two—or maybe by month. Here are all the new users that we got in January. That's one cohort. Here are all the new users we got in February. That's another cohort. That is typically the best place to start. But as you get a little bit deeper and more advanced in this, you can additionally slice by other dimensions, like country or region, or how you acquired that user, maybe what device they are using, or other characteristics of that customer.

David Lee: Next, let's talk about actions. So the action is the way to define what qualifies a user to be counted as an active user in each subsequent time period. The simplest way to do this is just: did they open our app? Did they visit our site? But a better way would be to pick a specific feature that you want to track that is more correlated with them actually using your product. Maybe that's posting a photo if you're building a social network, or using a specific workflow in your B2B tool that you're building.

David Lee: So let's look at some examples of what popular companies might choose. Let's say your Instagram. You would probably want to pick an action that relates to users actually seeing content in Instagram. So maybe I would pick "viewed three or more posts on Instagram." And the reason I picked three is that sometimes people will open up Instagram, not touch the screen at all, not get any value, and immediately leave. You probably want to filter those people out as active users.

David Lee: If you're Uber, you might pick "completed a ride"—actually like took a ride, ended up in a destination—as an active user of Uber. For Google Photos, for my product, we chose whether a user actually tapped in and viewed a photo full screen on their phone as the best measure of whether they were an active user. Because we know that if you viewed a photo full screen—either yours or someone else's that was shared to you—you were actually getting value from the product.

David Lee: So the best action to pick is one that is really correlated with the user getting real value from your product. And you want to try to filter away things where a user might be touching your product in some way but not getting real value.

David Lee: Okay, so last, you have to also define the time period that you're going to measure this on. So what I mean by this is the granularity of time that you're going to look at when you're counting whether a user performed the action that we just talked about. Typically, this should be a time period that is most connected to the desired usage of your product.

David Lee: So let me give you some examples. If you're building a social app or an entertainment app—maybe your Instagram or TikTok or YouTube—you probably intend for your user to use your product every day. So the time period in which we're going to measure the cohort retention should be daily. If you're building a utility product, maybe something like Google Photos or Uber, where you don't think a user would necessarily use it every single day, maybe weekly is a better time period to use.

David Lee: If you're a travel app—let's say you're Airbnb—people don't travel more than three or four times a year, so Airbnb probably would want to track something on a larger time granularity—larger time period, maybe quarterly or maybe even like semi-annually or annually. And the key here is you want to pick a time period that matches what you intend for your product. And we can talk about ways that you might screw that up later on.

David Lee: Okay, so now let's walk through an actual example and talk through how we're actually going to measure this in detail. So what you see here in front of you is what we call a triangle chart. Down the rows, you can see every month. So we're going to choose our cohorts by month—so all the new users in January we're going to isolate, all the new users in February we will isolate, and so on. And then what we're going to do is track those users in every subsequent month that happens.

David Lee: So in this first row and first column, you see that we had 12 new users in the month of January. And what we'll do now is look in February—one month later—how many of those 12 users came back and performed our action in the month of February? And we see that it's six. And then we'll look in March—two months later—and see that we had four people come back in the month of March.

David Lee: The key here is that we're counting each person one time during that time period, regardless of whether they came back one time in the month or 10 times in the month. Each user gets counted one time. And you can also see if we go to the next month, we actually get five people to come back from that original group of 12. So the key is this number can go up or down. It can never be bigger than the initial group in the first month of the cohort, because that's the total number of people we're going to look at.

David Lee: And then we'll do the same thing for February. So February we had 27 new users, and in subsequent months, now you can see how many of them came back each month. I like to think about this as a party. Say you're having a party. You've got your room. When people come into the room, you kind of tag them. You give them like a little sticker that says what month they came to your party in. So all the people that joined in January, we're going to put a January sticker on their shirt. All the people that came in February, we're going to put a February sticker. And then every month, we're going to look at the people in our party, and we're going to count how many of you people came from the January cohort? How many of you came from the February cohort? And that's the way that we're actually dividing up the user base and tracking these cohorts individually over time.

David Lee: One last thing to call out here in this triangle chart: you can see I've highlighted in yellow this diagonal line. And the diagonal line in this type of chart actually represents one real calendar month. So the yellow line here is the month of December. And so you can see all of the users that used our product in the month of December—where did they come from? From which cohort were they a part of initially? And you can see if you added up all the numbers along this diagonal, you would get the total number of users that used our product in December. So that's just an orientation of how we measure this on the ground.

David Lee: Now, these numbers are great, but what we actually care about is what the trends look like relative to the initial cohort size. So in this graph, we've just taken the previous one and divided by the initial cohort size to kind of normalize and get percentages. So you can see the first column—the initial month—it's 100% by definition. And then every subsequent month, now we're measuring what fraction of the initial cohort returned during the month.

David Lee: So this is a great visualization. You can kind of see if you look across the rows how each of your cohorts performs over time, which we really care about. And you can also look down a column and look at all the rows in a column and see whether you are generally improving over time with each subsequent cohort, or if you're generally getting worse. But I think the best way to look at this is to actually take this chart and graph it as a line graph. And that's what you can see here.

David Lee: So this is typically what we look at when we're talking about looking at cohort retention curves. So every line on this graph is one of our cohorts—the December cohort, the November cohort, the July cohort. The longest cohort, the one that started in January, has a full 11 months of data. And the newest cohorts—the ones that started in November and December—only have a couple data points at the top. So you can see this is kind of like a typical way to look at a cohort retention curve.

David Lee: Okay, so I know you're thinking, what is good? How do I know if my cohort retention curves are good or if they're really bad? So before I tell you the answer, let's walk through an exaggerated example, and maybe you'll be able to see for yourself what is the right answer.

David Lee: So let's assume we have two products: Product A and Product B. A is the black line, B is the orange line here. And we're going to show the cohort retention curves for these two products over time as we gather more data each month. So at the beginning, you look at this, it sure looks like Product A is the clear winner. It retains way more of its users in the first month or two.

David Lee: Let's reveal a little bit more data. We can see now Product B—it continues to drop. Boy, it has lost more than half of its users in the first couple months, whereas Product A is looking pretty good. The numbers are still well above 50%—really great.

David Lee: Let's keep revealing a little bit more, and maybe now you've had a change of heart. If you're the owner of Product B, you're probably feeling pretty good, because you're not losing users anymore. While your absolute number is down to maybe 20% of the initial cohort, it sure seems like it's stable and flat. Whereas if you're the company behind Product A, you might be starting to think about what is wrong with your product, because it seems like it will go to zero and you will eventually churn all of your users.

David Lee: So this is the core insight behind cohort retention curves. The only thing that matters—and I can't stress this enough—the only, only thing that matters is whether your cohort curves get flat. The shape of the curve is what matters, not the absolute number. The absolute number, the height at which it might get flat—it certainly is better if it's higher, of course—but it doesn't matter nearly as much as whether it gets flat at all.

David Lee: So that's the key insight here. The reason getting flat on your cohort retention curves really matters is it gives you some chance to accumulate users over time. If your curves don't get flat, every month you're just going to be acquiring new users and losing your old users, and you're just going to be on this treadmill trying to keep up forever. Whereas if you can accumulate even a small fraction of your initial cohort of users, you know that if you can keep doing that over time, long enough, you will eventually grow to a very large customer base and hopefully be able to make a lot of money.

David Lee: So if your curves don't flatten out, I would say it's a pretty good sign that you haven't yet made something people want. Now, in the early days of Google Photos, we measured weekly cohort retention, and our curves looked a lot like that orange line. They would drop off pretty quickly, but then they would get flat somewhere between 20% or 40%, depending on which country and device we were looking at.

David Lee: What's interesting is, you know, if you talk to a friend of yours and told them, "Yeah, 80% of my users leave like pretty immediately," they would think it sounds pretty bad, right? It's not a thing you would go around bragging about. But the fact that on Google Photos, 20% of users pretty immediately demonstrated that they would stay with the product and use it every week for basically forever, it gave me a lot of confidence. In like six weeks after launch of Google Photos, I was pretty certain that we would eventually be able to get 20% of all humans on the planet to use Google Photos. And turns out that's exactly what happened. Four years later, we were well north of a billion users—is probably closing in on two billion users now. And so getting your cohort curves to be flat will also give you a lot of confidence as a founder that you can actually build this into a really big thing.

David Lee: So let's next talk about how you might fool yourself into thinking that your cohort retention is good when in fact it is not. And I am going to be speaking from experience. I have made every single one of these mistakes. So let's dive in to what they are.

David Lee: The biggest mistake that I see people make is picking too large of a time period in which to measure your subsequent retention. So in our example, you know, we picked months. If you pick quarters or half-years, you have a much better chance of every user coming back and being counted as an active user. So by definition, your cohort curves are going to be flatter and higher. The larger you pick your time period, and who doesn't want to look better for investors, for employees, just to feel better about themselves when they're falling asleep at night? We all do. And so this is something to be consciously aware of, and also realize that your unconscious brain is going to push

David Lee: You to widen your cohorts even though you probably shouldn't at Bump. This was a mistake I made. We would look at our weekly cohort retention curves because we thought that weekly was kind of the right period of time that users should be using Bump, and they were really bad. What we did practically was, well, we have some investor meetings coming up, so let's widen the cohort to a month and let's see how they look there. And they looked better. And then we convinced ourselves, well, quarterly actually is a reasonable time to use our product. Let's increase our time period to once a quarter. And then the cohorts looked really great. But we were fooling ourselves, right? Bump was not designed to be used once every quarter. It was designed to be used pretty frequently. And by expanding our cohort time period, we were just deluding ourselves about what actually was the state of our product.

Another way to fool yourself in your cohort retention is picking too easy of an action. So we talked a little bit earlier about picking an action that is just a user opening your app or coming to your site. I would caution you against picking something that easy or that shallow in the usage of your product because there's lots of ways to game that, and you will find yourself gaming your metrics once you start charting this stuff.

A common example there is using notifications or other alerts to drive users to your product kind of inorganically. And what you'll find is they'll get there and then they're going to leave immediately and not actually get value from your product. And you don't want to be counting that usage in your cohort retention curves because it will lead you astray.

A great example I saw at Google when I first joined Google was still working on its social network, Google+. There was a point in time I kid you not that the active usage of Google+ was determined by whether a user saw in the top right corner of every Google product a little notification bell that would have a red notification if you had a Google+ notification—somebody added you as a friend, you had a new photo that got uploaded, something like that. And by doing that, it made the active user numbers really big, and so everybody felt good. But if you looked at the cohort retention, it was a lie. These were not active users. These were people who were in their Gmail and they happened to click on this little red bell to see what it is, and they got counted as an active user of Google+. So don't make mistakes like that. It's going to just lead to disaster.

One counterintuitive thing here—I think a lot of people think, "Oh, I'll use the best measure of an action, which is whether the user is paying me dollars this month for my product. Of course that's the best way to measure whether they're active." And counterintuitively, this is actually often not the case. Users first stop using your product and then they stop paying you for your product. And I think we can all probably relate to this. I'm sure we each have, you know, streaming services like Netflix or something else that we're probably paying for. And if you think about when the last time you watched a show on Netflix, it might be more than a month ago, but you probably haven't canceled. So I would be careful with using just "is paying" as your action.

A better way to do it would be to pair it as "is paying and is an active user"—actually used some part of my product this month. That's a good combination to track.

So the best way to avoid picking too easy an action—this is the rubric that I would recommend to founders: Imagine you're sitting next to one of your customers. They're here at the table using your product. When you watch them use your product, what is the thing that's going through your head that helps you answer the question of whether that user is a good user of your product, that they're actually using it in the way that you intend? Whatever that answer is, I would recommend using that as the action in your cohort retention curves.

So another common way to delude yourself when you're looking at your cohort retention curves is to look at a single point in time as opposed to the shape of the entire curve. This probably should seem obvious, but this is a thing that I hear from founders literally every single day. A founder might come to me and say, "Dave, we're doing great. We have 80% week-over-week retention." And I scratch my head for a little bit, and then I ask, which week? What is the 80%? What's the numerator and what's the denominator in that number? And almost always the founder doesn't know the answer to that question.

In our example, we might look one or two months out, and product A has 75% week-three retention—sounds great. But what you might want to ask is, "Well, what does week-four retention look like? What about week two? What's the trend line?" And in our example, you would find that product A's retention is very much not flat. And so despite having a 75% week-three retention, it's a product that is not doing well.

Okay, finally, just a word of caution about using analytics tools or analytics suites. I think it's awesome that they all exist. I think it's awesome that they have retention and cohort retention graphs built in. But what I would caution you on is that often those graphs aren't measuring exactly what you think they are. I've seen cases where these tools aren't separating cohorts in the way that the founders think they are. Maybe they're measuring rolling retention over time as opposed to fully separating each cohort. Sometimes they do things like, "This is a graph of whether a user has returned at all by a certain date" as opposed to "whether a user returned during this specific time period."

So what I would recommend for most founders is to actually build these cohort retention curves on your own using your logs via a script or in Google Sheets. Do that a little bit upfront yourself to develop your own intuition about what's going on and how these are actually measured. And then compare it to what your analytics tool is doing. And if they exactly match up and you feel really confident, then by all means use the analytics tools. But too many times founders come to me and show me their dashboard, and I ask any questions about what those numbers actually represent, and they don't actually know. So don't be one of those people.

When you're looking at cohort retention curves, you don't need to be looking at these multiple times per day. You don't need to look at them even every day. But I would recommend at least refreshing these graphs every week or two weeks because when things go south, you're going to want to know it really quickly.

Far more likely what you will find is that your cohort retention is not good from the very beginning. And now we need to think about ways to improve it. So let's talk about that.

So the most obvious way is to improve your product. Come up with new use cases. Maybe it should do something completely different. Maybe you need to speed up your product or reduce latency somewhere. Make the flows a lot simpler. Doing all of these things actually will change your cohort retention curves, and you will see them get flatter and you will also see them get flatter at higher levels.

In our example that we showed earlier, if you look at these sets of cohorts, you might see that the oldest cohorts seem to be performing the worst—they seem to be attracted down to zero. But then the middle of the year, around June or July time frame, we see a little bit of improvement. The cohorts are a little bit higher and they're a little bit flatter. So maybe the team behind this product made some improvements that made things a lot better. And then the most recent cohorts, right October, November, they seem to be flattening out a lot more, a lot sooner. So this is what you might see if you actually do make improvements to your product that are meaningful.

So another way to improve your cohort curves is kind of the flip side of improving your product—is to acquire better users. I think this is a thing that a lot of founders don't think about often. You've built a great product, but you're targeting it to the wrong type of customer. So you can actually improve your performance here by just acquiring users in a different way.

This is something that I saw a lot at Google working on Google Photos. I remember at one point a marketing exec high up decided that Google needed to target young people more—like that was important for the company. And they did this big push on having marketing and advertising targeting Gen Z, the Gen Z audience. So the teams at Google are really good. They did a great job of bringing in a bunch of new young users to use Google Photos. But it turns out those cohorts had really bad retention. And it kind of makes sense, like Google Photos is a tool to accumulate your life's memories and reminisce. And if you're a young person, a, you don't have that many life memories yet. And if you do, you probably aren't thinking much about, like, reminiscing on that moment two years ago or one year ago. You're probably out living your life, being a young person. So this is an example of a mismatch between user acquisition—like, who you're trying to get to use your product—and what your product actually does.

And often, this is the easiest way to improve the performance of your cohorts.

We talked earlier about when you're picking your cohorts, ways that you can slice your cohorts. I talked about by country or by device. This is a great way to try to improve your product and figure out what's going on. So if you see that your cohort curves are not getting flat, one of the immediate next steps I might recommend is to try to slice those cohorts by different dimensions—by what country you're serving, what type of customer, whether it's a big company or a small company that you're targeting in your B2B tool. Divide it up by whatever attributes you think make sense. And what you might find is that some of those cohorts are very flat and perform really well, while others are really, really poor. And that would be a clue of where to start in terms of improving either your product or your user acquisition.

Related to the idea of acquiring better users, another way to improve your cohorts is to improve the first user experience—the onboarding, the activation of customers that you get. This is a thing again I think people overlook. They immediately jump to what the product does, but often you just need to help your users get into a good state and be able to use your product in the right way.

We see this a lot with companies that are building tools for businesses. They put a lot of time into building the tool itself, but then they don't think about how you actually teach people to use it. How do you get into their workflow? What are they doing yesterday before they used your product, and what do you want them to change about their life today when they are using your product? Investing in this often is like the cheapest and easiest way to improve your performance of your cohorts.

Okay, lastly, a great way to improve your cohort retention is to have some sort of network effect in your product. Now, this won't work for everyone, but products where every subsequent user of your product makes the product better for your existing users—social networks, sharing networks, texting apps—these are all examples of that. If you have a dynamic like that where the more people who use it, the better it gets, you should see cohort improvement over time as that network grows and becomes more dense. So if you're building a product that has something like that, you might want to think about how could we focus on building good, dense networks around the users that we have. And you may find improvements to your cohorts.

All right, finally, I want to talk a little bit about what is the Holy Grail—like, what is the best of the best look like here? And what I would say is that the best of the best is cohort curves that don't just get flat, but they actually go up over time. And you can do this from all of the techniques I just talked about—making your product better, targeting better customers. If you do this, you'll find that users of your product that are sticking with you actually will start using it more and more over time. And if you see that your cohort curves are getting flat and then increasing, and subsequent cohorts are getting better and better over time, you should be feeling really good.

Okay, so hopefully now you have a pretty good idea of actually how to measure cohort retention curves and how to decide if what you see in those curves is good or bad.

To conclude, I kind of want to tie this all together and see how it connects to building a really big company. So let's go back to how we measure the cohorts in the very first triangle chart that we looked at. This is just the count of users from each cohort, each month, who used your product in subsequent months. What we're going to do now is just instead of having it be relative months, we're going to slide all these rows to the other side and align them in absolute time. So now we're seeing all of the users in each calendar month, which cohort did they come from, right?

So let's look at December. In December, here we can see all of the users in December are represented in the last column in the chart here, and we can see which cohort they came from. Now let's take this chart but draw it as a line graph. And this is what we call a layer cake chart. For every month, this is the number of users you have of your product, active users of your product. But each of the layers of this cake represents which cohort they initially came from.

So what you can see here is that if you look at the last month in December, you know, we've now got almost 600 users of our product. It is not just users that we acquired recently in December or November. It's actually composed of all of the previous users who stuck with our product. And if you see a layer cake that looks like this, that the top line is growing really nicely and it's composed of thick layers coming from old cohorts, this is like the most beautiful chart that you'll ever see in your startup.

So if you see this, congratulations, you're off to the races.

Okay, so this layer cake graph is hopefully the start of what could be a multi-billion dollar company. And when we think about cohorts, the way I talk to founders about it is you obviously want to go talk to your users in person, hear what they're saying. This is the qualitative feedback that's going to actually give you insights about your product. A cohort retention curve isn't going to teach you what to change necessarily, but it might tell you whether you're on the right track and things are working or not.

And what I would say is, if you look at your cohort retention curves and they don't get flat, the one thing you can be sure of is that you need to get out there, talk to your customers, understand what's going on, and hopefully make something that they want.

So thank you so much for spending your time learning about cohorts with me. I wish for each of you a flat cohort retention curve in your future.
