Query 1: What range of text in the "Requirements" section have received the most attention from the reviewers.

SELECT ?resourceText  (COUNT(?replyID) AS ?commentCount)  WHERE {
?section <http://schema.org/hasPart> ?resourceId .
?section <http://schema.org/name> "Requirements" .
?resourceId <http://schema.org/description> ?resourceText .
?resourceId <http://purl.org/spar/cito/hasReplyFrom> ?replyID
}GROUP BY ?resourceText
ORDER  BY DESC(?commentCount)

Query 2 : What sections in the article received greatest number of comments by reviewers?

SELECT ?section  (COUNT(?commentID) AS ?commentCount)  WHERE {
?section <http://schema.org/hasPart> ?commentID . 
 ?section  <http://schema.org/description> ?sectionName .
?section  <http://schema.org/description> ?sectionName .
}
GROUP BY  ?section
ORDER  BY DESC(?commentCount)


Query 3 : Get a list of the article’s reviews that contain the word “communication”

PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?subject ?object WHERE {
  ?subject schema:name "Comment" ;
           rdf:value   ?object .
  FILTER regex(str(?object), "communication")
}


Query 4  Find out whether the name of a specific reviewer is in the list of reviewers of this article.