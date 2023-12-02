---
title: "Nextjournal"
enableToc: false # do not show a table of contents on this page
---
Authored by:: [[P- Brendan Langen]]

Nextjournal is an example of a [[Literate programming interface]], as seen in [[R- clojureD 2021- Command and Conquer- Learnings from Decades of Code Editing by Philippa Markovics|this demo]]. Nextjournal uses a context-driven model that enables users around context-first thinking, via convenient UI abstraction, context-aware glossary of features, and a balance between easy to discover (mouse usage) and expert usage (keybindings, flows).


Context is critical for displaying UI elements at the correct time, so Nextjournal provides users with a command bar at the bottom of each page, like this. 

![[Pasted image 20211217121037.png]]

[[C- Tools for thought are popular when it feels like they get to know you better over time]], and Nextjournal aims to enable and foster an environment of power users. Below are the different contextual keybindings that are highlighted in a command bar, located at the bottom of each screen. 
![[Pasted image 20211217121152.png]]

![[Pasted image 20211217121225.png]]

![[Pasted image 20211217121241.png]]

Information is gathered across all of the states a user may be operating in.

![[Pasted image 20211217120935.png]]

Once a keyboard shortcut is used, a pallette is generated with specific context on where you are: 
In a rich text context, the focus:

![[Pasted image 20211217121348.png]]

In a code editing context, keybindings will tie to the specific language you're writing in (i.e. Clojure will operate differently than Typescript).

![[Pasted image 20211217121328.png]]

The overall feel is a tool that allows novices to gain a deeper understanding of their environment, while affording expert users with advanced functionality to improve their programming experience. 
