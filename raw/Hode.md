---
title: "Hode"
enableToc: false # do not show a table of contents on this page
---
Authored by:: [[P- Brendan Langen]]

Hode (Higher Order Data Editor) is a Haskell program for reading, writing and searching what might be loosely termed a hypergraph. It's like a knowledge graph, but more expressive -- atoms and relationships can both be members of other relationships, which are labeled and can have any number of members.

Created by [[P- Jeffrey Benjamin Brown]] https://github.com/JeffreyBenjaminBrown

> There are three branches to Hode: The RSLT data structure, the Hash language for describing subsets of an RSLT, and the UI, which lets you use the previous two things.
> A Rslt (Reflexive Set of Labeled Tuples) is a generalization of a knowledge graph. It lets a user easily represent any natural language expression. (A `Rslt` is isomorphic to what some programmers call a "hypergraph" -- but mathematicians claimed that term first, and in math it means something much less expressive.)
> A `Rslt`is a collection of expressions, each of which is either a phrase (like "cats"), or a relationship (like "cats have noses") or a template (like "_ have _") shared by many relationships.
> What distinguishes a `Rslt` from a `graph` is that relationships can involve any (positive) number of members, and a relationship can itself belong to other relationships.
> Hash is a language, close to ordinary natural language, for talking about expressions in a `Rslt`. It offers a concise representation, both for individual `Expr`s (expressions) in a `Rslt`, and for queries to retrieve sets of `Expr`s.
> The UI displays expressions from your graph using [the Hash language](https://github.com/JeffreyBenjaminBrown/hode/blob/master/docs/hash/the-hash-language.md).

Examples in action.
```
/a (mammals #need calcium) #because (mammals #build bones)
```

```query
mammals
	#need _
	7: "mammals #need calcium"
```
![[Pasted image 20210912173246.png]]

```
`/find /eval bob #likes pizza ##with pineapple ###because /it)` -- Returns only the reason, not the full "because" relationship.
```

```
`/find bob #likes /_ /|| bob #dislikes /_` -- Every #likes and every #dislikes statement with bob on the left.
```


![[Pasted image 20210915183241.png]]