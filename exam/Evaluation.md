## Evaluation

Exercises: 8.1, 8.4, 8.8, 8.9.

### 8.1. An IR system returns 8 relevant documents, and 10 nonrelevant documents. There are a total of 20 relevant documents in the collection. What is the precision of the system on this search, and what is its recall?

- Precision: 8/18 = 0.44
- Recall = 8/20 = 0.4

### 8.4. What are the possible values for interpolated precision at a recall level of 0?

At a certain recall level r, is defined as the highest precision found for any recall level r' >= r: 
     - pinterp(r) = max p(r'), so that r'>=r.

So, for interpolated precision at a recall level of 0:
- 0 <= pinterp(0) <= 1.

### 8.8. Consider an information need for which there are 4 relevant documents in the collection. Contrast two systems run on this collection. Their top 10 results are judged for relevance as follows (the leftmost item is the top ranked search result):
- System 1: R N R N N N N N R R
- System 2: N R N N R R R N N N

1. What is the MAP of each system? Which has a higher MAP?
2. Does this result intuitively make sense? What does it say about what is important
in getting a good MAP score?
3. What is the R-precision of each system? (Does it rank the systems the same as
MAP?)

1. 
   - MAP(System 1) = (1/1 + 2/3 + 3/9 + 4/10)/4 = 0.6
   - MAP(System 2) = (1/2 + 2/5 + 3/6 + 4/7)/4 = 0.493
   - System 1 has a higher MAP.

2. For a good map score, it is essential to have more relevant documents in the first few (3-5) retrieved documents. In the first 3-4, that's true; in the first 7 for example, it doesn't. 

3. 4 relevant documents -> R-Precision equals to Precision at 4
   - R-P(System 1) = 2/4 = 1/2
   - R-P(System 2) = 1/4
   - System 1 has a higher R-P.

### 8.9. The following list of Rs and Ns represents relevant (R) and nonrelevant (N) returned documents in a ranked list of 20 documents retrieved in response to a query from a collection of 10,000 documents. The top of the ranked list (the document the system thinks is most likely to be relevant) is on the left of the list. This list shows 6 relevant documents. Assume that there are 8 relevant documents in total in the collection.
- R R N N N
- N N N R N
- R N N N R
- N N N N R

  1. What is the precision of the system on the top 20?
  2. What is the F1 on the top 20?
  3. What is the uninterpolated precision of the system at 25% recall?
  4. What is the interpolated precision at 33% recall?
  5. Assume that these 20 documents are the complete result set of the system. What is the MAP for the query?

Assume, now, instead, that the system returned the entire 10,000 documents in a ranked list, and these are the first 20 results returned.
  6. What is the largest possible MAP that this system could have?
  7. What is the smallest possible MAP that this system could have?
  8. In a set of experiments, only the top 20 results are evaluated by hand. The result in (5.) is used to approximate the range (6.)–(7.). For this example, how large (in absolute terms) can the error for the MAP be by calculating (5.) instead of (6.) and (7.) for this query?

1. Precision at 20: 6/20 = 0.3.
2. ...
3. 

