---
title: "The common forms of structure people add to their notes"
enableToc: true # do not show a table of contents on this page
---
During our research, we encountered multiple methods people used to structure information.

### Naming

People would name concepts, and in the process, give themselves a "handle" to refer to a whole idea. See [[C- Hypertext enables communication with high information density]] for more details. Autocomplete supports this use case, augmenting "tip of my tongue" recall.

### Linking 

People would connect multiple concepts together, providing themselves navigational or semantic relationships. In the case [[Roam Research]], naming, categorization, chronology, pipeline, and description are all collapsed into links.

Not all links are created equal. For example, most networked notebook software simply enables users to say that two items are related without the ability to label the relationship, providing a reason **why** they are related. By displaying [[contextual backlinks]], the user can view the relationship in the context of a sentence or paragraph without requiring additional organizational overhead in requiring the user to explicitly label relationships.

Additionally, links between two nodes gain a higher degree of fidelity when the nodes have types. For example, [[P- Joel Chan]]'s [[Discourse Graph Plugin]] gives you claims, questions, evidence, and sources by default, while enabling the user to create their own types, such as decisions, ideas, and people. Simply being able to filter relationships by node type implies a lot of meaning. For example, claims related to a decision likely support arguments on either side, and evidence related to a claim likely supports or opposes the claim.

Links can also vary in whether they are directed or undirected. For example, A --leads to--> C, or A <-is friends with-> B. Most networked notebooks primarily support undirected links.

### Categorization

This is when the user places items into classes or groups. This can happen in a bottom up manner through [affinity mapping](https://www.usertesting.com/blog/affinity-mapping), where users would take previously uncategorized information, place it into groups of similar content, and then name the groups. It can also happen top down, where people would come up with types of note (like claims, questions, and resources).

### Description

This is typically a more bottoms up process than categorization, where things are defined in terms of how they are described, Then, when users want to pull up a note but can't remember the title of the note, they describe it and see what's similar. This is very similar to how people might recall an item when it's on the "tip of their tongue." In conjunction with labeled relationships, this can be a very effective strategy. For example, "I know there was a paper **about** psychological responses to sudden windfalls **by** a specific author." With labeled relationships, this sort of query would be trivial.

### Logical rules

This includes equivalence statements like "X is the same as Y," encompassing statements like "X contains Y," or conditional statements like "If X or Y, then Z."

Some apps, like [[Obsidian]], [[LogSeq]], and [[Codex OS]], enable aliases, which can be thought of similarly to an equivalence statement, but are not quite the same thing. These enable you to refer to a single concept in multiple ways, but do not enable you to refer to one concept or the other and have references show up in both, like [[I- Provide Push and Pull as inline syntax to affect the related items section for a page|push and pull do in Agora]].

Encompassing statements are available in some sense with applications like [[LogSeq]] and [[Bear]] that enable hierarchical namespacing. For example, in LogSeq, I might refer to specific applications as or Here I'm referring to something like "any time I refer to Perceptual Control Theory, I'm also referring to Behavioral Science Theories generally, but not the other way around.

[[Roam Research]] similarly enables encompassing statements through nested page titles - for example, `[[I- A [[structural editor]] for [[data structures]]]]` would reference both `[[structural editor]]` and `[[data structures]]` every time the encompassing page title was referenced. One might argue that this is more flexible than LogSeq's namespacing approach, as it does not scope either of the nested pages into one strict hierarchy.

### Pipeline

This is when users specify different stages in a pipeline where a note can live. In the traditional [[Zettelkasten]] practice, there are fleeting notes and permanent notes. In [[P- Maggie Appleton]]'s variation of [[P- Andy Matuschak]]'s system, [notes are "seedlings" before they develop into "evergreen."](https://www.youtube.com/watch?v=RXXXHN516qc) In my personal writing pipeline, I have [premise, develop, and publish](https://www.youtube.com/watch?v=F2To62BcMdI). See also: [[C- People process complex information in multiple levels and stages of processing]]

### Location

This can be seen in apps that use folders or outliners that use indentation to signify hierarchy. "Which folder does this idea go into?" "What should I indent this under?" We saw multiple users concerned with [[quick capture]] complain that "[[If I’m thinking too hard about structure before I write the note, I forget what I was going to write down]]."

### Chronology

[[Roam Research]] is opinionated insofar as it starts all users on the "Daily Notes Page" when they load the app. If all other forms of organization fail, users may still be able to find what they are looking for based on which day they wrote about it.