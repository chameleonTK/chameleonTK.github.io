---
layout: post
title: Two-way referencing and denormalization
tags: [Archive, Code Code and Code]
author: Pakawat Nakwijit
excerpt_separator: <!--more-->
color: rgb(165,42,42)

---

กลับมาที่การออกแบบกันอีกครั้ง หลักจากที่ได้โครงสร้างคร่าวๆกันไปเป็นที่เรียบร้อยแล้ว

involving two-way referencing and denormalization.

Intermediate: Two-Way Referencing

The application will need to track all of the Tasks owned by a Person, so we will need to reference Person -> Task.

On the other hand, in some other contexts, this application will display a list of Tasks and it will need to quickly find which Person is responsible for each Task. You can optimize this by putting an additional reference to the Person in the Task document.

This design has all of the advantages and disadvantages of the “One-to-Many” schema, but with some additions. Putting in the extra ‘owner’ reference into the Task document means that its quick and easy to find the Task’s owner, but it also means that if you need to reassign the task to another person, you need to perform two updates instead of just one.

Intermediate: Denormalizing With “One-To-Many” Relationships

For the parts example, you could denormalize the name of the part into the ‘parts[]’ array. For reference,

Denormalizing would mean that you don’t have to perform the application-level join when displaying all of the part names for the product, but you would have to perform that join if you needed any other information about a part.

Denormalizing from Many -> One

While making it easier to get the part names, this would add just a bit of client-side work to the application-level join:

Denormalizing saves you a lookup of the denormalized data at the cost of a more expensive update: if you’ve denormalized the Part name into the Product document, then when you update the Part name you must also update every place it occurs in the ‘products’ collection.

Denormalizing only makes sense when there’s an high ratio of reads to updates.

If you’ll be reading the denormalized data frequently, but updating it only rarely, it often makes sense to pay the price of slower updates – and more complex updates – in order to get more efficient queries.

Also note that if you denormalize a field, you lose the ability to perform atomic and isolated updates on that field. Just like with the two-way referencing example above, if you update the part name in the Part document, and then in the Product document, there will be a sub-second interval where the denormalized ‘name’ in the Product document will not reflect the new, updated value in the Part document.

Denormalizing from One -> Many
it’s significantly more important to consider the read-to-write ratio when denormalizing in this way.

Intermediate: Denormalizing With “One-To-Squillions” Relationships

You can also denormalize the “one-to-squillions” example. This works in one of two ways: you can either put information about the “one” side (from the 'hosts’ document) into the “squillions” side (the log entries), or you can put summary information from the “squillions” side into the “one” side.

Here’s an example of denormalizing into the “squillions” side. I’m going to add the IP address of the host (from the ‘one’ side) into the individual log message:

In fact, if there’s only a limited amount of information you want to store at the “one” side, you can denormalize it ALL into the “squillions” side and get rid of the “one” collection altogether:

When deciding whether or not to denormalize, consider the following factors:

You cannot perform an atomic update on denormalized data
Denormalization only makes sense when you have a high read to write ratio

Rules of Thumb: Your Guide Through the Rainbow

One: favor embedding unless there is a compelling reason not to

Two: needing to access an object on its own is a compelling reason not to embed it

Three: Arrays should not grow without bound. If there are more than a couple of hundred documents on the “many” side, don’t embed them; if there are more than a few thousand documents on the “many” side, don’t use an array of ObjectID references. High-cardinality arrays are a compelling reason not to embed.

Four: Don’t be afraid of application-level joins: if you index correctly and use the projection specifier (as shown in part 2) then application-level joins are barely more expensive than server-side joins in a relational database.

Five: Consider the write/read ratio when denormalizing. A field that will mostly be read and only seldom updated is a good candidate for denormalization

Six: As always with MongoDB, how you model your data depends – entirely – on your particular application’s data access patterns. You want to structure your data to match the ways that your application queries and updates it.

Embed the N side if the cardinality is one-to-few and there is no need to access the embedded object outside the context of the parent object

Use an array of references to the N-side objects if the cardinality is one-to-many or if the N-side objects should stand alone for any reasons

Use a reference to the One-side in the N-side objects if the cardinality is one-to-squillions

Productivity and Flexibility

The upshot of all of this is that MongoDB gives you the ability to design your database schema to match the needs of your application. You can structure your data in MongoDB so that it adapts easily to change, and supports the queries and updates that you need to get the most out of your application.