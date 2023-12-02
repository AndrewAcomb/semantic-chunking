---
title: Q- How do we enable many users with their own idiosyncratic structure to converge in one discourse graph
enableToc: false
tags:
- question
---
Authored by:: [[P- Rob Haisfield]]

This is an incredibly tricky problem.

One common solution is to expect that users update their writing into a new shared structure at the point where they choose to publish. If structure is missing, [[C- It will be important to capture the potential energy of information consumption]], enabling the broader user base to update it and add in new structure. To be able to rely on readers structuring publications post-hoc, we'd likely require incentives, which are largely out of scope for our research.

However, [[C- There is a wealth of creative exhaust generated by researchers that is going to waste]] and to leave that behind as is done in the above solution would be a shame. Currently, [[P- Joel Chan]] is running a journal club (everybody reads papers on a given topic) using the [[Discourse Graph Plugin]]. Everybody participating in it uses/used Roam Research at a high level, and therefore developed their own idiosyncratic style. Some people prefer to write information directly onto the claim, question, and evidence pages, while others prefer to do so in thoughtfully indented outlines. Through the plugin, we are able to write Datalog queries that describe each of our styles such that we end up with the same discourse relationships regardless of how they are written. This works well for a small group, but may not work well on a global scale. For that, it might prove necessary to segment the queries so certain rules apply to different authors.

The takeaway to the above solution is that there can be an underlying data structure separate from the visual presentation layer. As long as individual user behavior is consistent within documents, queries can identify that structure such they compile into the appropriate data structure.
