---
title: "Standoff Annotation"
enableToc: false # do not show a table of contents on this page
---
Authored By: [[P- Brendan Langen]]

[[P- Iian Neill]]'s goal with [[Codex OS]] is to build a system for *relation* - the principle of relatedness or [[sensemaking]]. To achieve this, he uses a modified data structure called standoff annotation, which allows information to respect multiple interpretations. 

This concept carries a ton of implications, but namely that an entity can be defined and connected in multiple locations.

Most databases require an entity to carry the same relationship across the entirety of the database. This causes inherent challenges in extending knowledge across domain boundaries, as entities often carry different definitions - and thus, relationships. 

Codex OS is designed to enable users to frame things in multiple ways (or layers) without breaking the structure of their graph. 

Standoff annotation allows users to annotate atop an entity, which is stored separately from the text, yet still retains the relationship to the initial text.
https://github.com/argimenes/standoff-properties-editor

> A standoff property is a property that 'stands off' from the text it refers to, that is stored apart from the text source.
> A property in this context is a data structure that represents a range of characters in the text along with information relevant to the annotation, such as the annotation type. Annotations can be of any type, e.g. stylistic (italics; bold; underline), semantic (line; paragraph; page), or linked entities (database record; URL).

> XML does not cope well with [overlapping annotations](https://en.wikipedia.org/wiki/Overlapping_markup). This is because the tree structure of XML mandates that an overlapping annotation (two or more annotations that overlap the same text sequence) cross one or more branches of that tree structure.
> These problems disappear, however, if the text and its annotation properties are kept entirely separate. The text, then, is stored in a raw or unformatted state, annotated by a collection of discrete standoff properties.

Technical challenges from standoff properties can be mitigated by creating linked-list data structures.

> The technical challenge posed by standoff properties is that they require indexes to link annotations to the words in the text, which suggests that the text cannot be changed without breaking the annotations. However, by using a linked list-style structure composed of SPANs it is possible to create properties that reference characters by pointers, allowing text to be freely inserted or deleted without breaking the annotations. Indexes are only calculated at the end of the session, when the annotated text is to be exported (and presumably saved).

[[P- Iian Neill]] suggests that since machine generated annotations could enable a wealth of annotations, a layering structure can act as a focusing frame. 

> As there is no defined limit on the number or types of annotations that can be added to a text, there is the chance that texts may become visually cluttered with annotations. To address this, there is an option to assign a user-defined 'layer' to an annotation for the purpose of grouping them. Layers can be shown and hidden at will, thus reducing clutter. This is particularly helpful when it comes to computer-generated annotations, such as syntactic or semantic annotations created by an NLP library or other text analysis tools.

Adding a graph database atop standoff properties affords compounding benefits.

> While standoff properties can be stored in any format storing them as LOD entities in a graph database vastly increases their potential. For example, if you were searching for all references to a person you would not only find the texts but the exact character positions in the text. If you expanded your query from a person like Leonardo da Vinci, say, to all artists you could see every instance an artist is mentioned in any text
> Queries could also be combined across annotation types. For example, if you had the syntax tree of a text you could find every occurence of a term within a given syntactical unit. The more annotation types you record, the greater the number of text mining options become available.

See also this thread from [[P- Iian Neill]] discussing advantages of using standoff annotation in conjunction with a graph database:

- [[Twitter thread]] [[Codex OS]]: An exploration of some of the things you can do with standoff markup in Codex that you can't do in certain ... other systems.
    - THREAD
    - 👇 [*](https://twitter.com/codexeditor/status/1302585628178051075)
  - no `[[brackets]]` ((of)) {{any}} kind needed!
    - no need to pick one name for your concept: just highlight the text to create/link to it
    - no need to rename embeds later
    - no need to define aliases
    - find a concept not just by name but by *any term ever used to refer to it* [*](https://twitter.com/codexeditor/status/1302585629922877443)
  - markup can intersect other markup without limit
    - can markup inside words, single letters, even between letters
    - markup doesn't interfere with the text, so can easily copy-paste the text without markup if desired [*](https://twitter.com/codexeditor/status/1302585631780958216)
  - all markup linked to the user who added/changed it
    - users can collaboratively markup without worrying about trashing the doc with clashing `[[brackets]]`
    - AI can add its own markup without clashing
    - easily filter markup in and out by the user, by type, by properties [*](https://twitter.com/codexeditor/status/1302585633546747905)
  - marking up text creates any kind of entity you like in the graph, not just pages or text blocks
    - graph entities can have properties, traits, user-defined relationships, be linked to activities
    - you define entities from the bottom up from your texts [*](https://twitter.com/codexeditor/status/1302585635421564928)
  - markup is basically handled like a web component: it's not just data, it can also have behaviours, life cycle
    - markup can call out to APIs
    - markup can be self-animating #NoCode: no JS or CSS needed, just click a button/hit a key [*](https://twitter.com/codexeditor/status/1302588233310588930)
  - markup not stored as HTML embedded in text so poses no XSS risk
    - new markup can be easily written in the API, from simple styling, to animation, to semantic links to the knowledge graph
    - markup links entities and texts in the graph together into one giant transclusive web [*](https://twitter.com/codexeditor/status/1302588235613310979)
  - pick a concept (like "markup") and see all *other* concepts mentioned in any lines in your graph where "markup" appears - in less than a second
    - pick a concept and find all lines where all things *related to that concept* appear
    - did I mention you can define relationships? [*](https://twitter.com/codexeditor/status/1302591073919795200)
  - did I mention you can define traits?
    - a trait is like a type or class but can also go sideways as well up/down
    - you can build up an entity from traits *you* define: man; woman; big; small; acidic; monadic; libertarian; American; any trait you can think up [*](https://twitter.com/codexeditor/status/1302595687503159297)
  - traits make it easy to perform fuzzy searches
    - can't remember the *name* of that French architect? Just query for the *traits* "French" and "architect"
    - or how about finding that company connected to that dev you worked with one time? Just do a relationship search [*](https://twitter.com/codexeditor/status/1302595689428299777)
  - did I mention you can define your own relationships?
    - create them directly from the text by point and click or from the graph view itself
    - clicking an arrow in the graph even *transcludes the line of text* where you made that relationship
    - total text/graph integration! [*](https://twitter.com/codexeditor/status/1302595691173224456)
  - did I mention you can also define properties?
    - you can add properties to any entity. Is your entity a place? Add lat/long. A video, image, PDF, etc.? Add a URL. Need a new type? Just define it
    - speaking of multimedia, now all your media can be in a graph [*](https://twitter.com/codexeditor/status/1302598731041177606)
  - did I mention you can also create timelines in Codex?
    - you can define events involving multiple entities occuring at a point in time
    - if any entity (person, place, idea, etc.) is linked to an event you can find all events it appears in
    - you can sync map + timeline views [*](https://twitter.com/codexeditor/status/1302600578116190210)
  - and you can mix texts, videos, images, PDFs, iframes, and dozens of other windows in a web-based desktop
    - you can make connections spatially
    - you can snapshot all windows on screen and reload them later, picking up a thought trail where you left off [*](https://twitter.com/codexeditor/status/1302610597184299010)
  - To cap off for now, you may be thinking, "OK, sounds good, but standoff texts are static and can't be changed. You can't write in them."
    - This problem was fixed in Codex in 2018. You can change the text freely without breaking standoff.
    - And do it in a WYSWIG editor! [*](https://twitter.com/codexeditor/status/1302616066774896640)
  - PS.
    - You can also link two blocks of text in different documents and write a note linking them. You can transclude from the source to the target or vice versa.
    - Not a block copy: live transclusion.
    - In fact, you can link many-to-many blocks of text, if so desired. [*](https://twitter.com/codexeditor/status/1302617530976989184)
  - Another practical advantage of standoff is that you can write code to segment your text into sentences and/or paragraphs using regex ... BUT even if the regex pattern was off a little the segmentation won't break the text because there's no embedded markup to break it. [*](https://twitter.com/codexeditor/status/1309593731310301184)
