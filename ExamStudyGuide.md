# PRI Exam Study Guide

## Information Processing

1. Distinguish between data, metadata and information.
   - Data: measurement of something on a scale; fact known by a direct observation.
   - Metadata: "data about data"; data providing information about aspects of the data
   - Information: data with a context, enabling decision making; data already processed, organized and structured.

2. Identify and describe the phases of a typical information lifecycle.
   - Occurence: discover, design, author, etc;
   - Transmission: networking, acessing, retrieving, transmitting, etc;
   - Processing and Management: collecting, validating, modifying, indexing, classifying, filtering, sorting, storing, etc;
   - Usage: monitoring, explaining, planning, forecasting, decision-making, educating, learning, etc;

3. Describe typical data processing patterns, pipelines and frameworks, e.g. ETL, EtlT, OSEMN.
   - Raw: data discovery; ingestion, understanding and metadata creation;
   - Refined: data preparation, establishing relationships between datasets, assessing data quality issues;
   - Production: integrating the data into production processes or products.
  
   - 3 typical patterns/frameworks:
     - ETL: Extract-Transform-Load; associated with classic centralized IT driven operations.
     - ELT: Extract-Load-Transform; capable of handling large volumes of data; column-oriented data; ELT, in contrast with ETL, pattern "better-suited" to the division of responsibilities in multidisciplinary teams.
       - EtLT: data cleaning tasks before loading.
     - OSEMN: Although there is 5 steps, real-world processes are typically non-linear (jumping through steps)
       - Obtain, gathering data
       - Scrub, clear, arrange, prepare data
       - Explore, observe, experiment, visualize
       - Model, create a statistical model of the data
       - Interpret, drawn conclusions, evaluating and communicating results.

4. Describe the challenges associated with data processing.
   - Amount of data available
   - Complexity of the data
   - Speed at which it changes
   - Data quality (missing data, inconsistent values, duplicate values)

5. Identify and describe challenges and techniques related to: data cleaning, data preparation and data presentation.
   - Data Cleaning: identify and fix data quality issues.
     - Parse and extract text and metadata from files (e.g. Beautiful Soup for HTML).
     - NLP toolkits provide natural text processing tools (e.g. NLTK).
     - Data processing (e.g. R, Pandas).
   - Data Preparation: suit the data to the follow-up phases:
     - Data transformation: improve or facilitate data handling in next stages.
       - Normalization of values to a comparable scale;
       - Scaling values to the same range;
       - Discretization or binning (numeric countinuous value into ordered categorical values).
     - Synthesis of Data: create new attributes derived from existing data.
       - Difference between 2 timestamps (e.g. duration);
       - Maximum value from a series of numerical attributes;
       - Integrated score that combines several attributes;
       - Splitting an existing numerical series in 2 independent series;
       - Most important keywords or topics extracted from a textual field.
     - Data integration: combine data from different sources.
       - Central step: link the corresponding records.
     - Data reduction or selection: eliminate data from the collection, for being not relevant, outdated, volume exceeds capacity and/or excessive precision.
       - Data filtering
       - Data sampling: non-deterministic process that takes a random subset of the data items of a requested size.
       - Data aggregation: reduce excessive detail in data; grouping method choice depends of domain-specific criteria; selection of the aggregation operator (mean, median, min, max, percentile).
   - Data Presentation: visually present the result of the execution of different methods.
     - Good understanding of the data properties.
     - Before applying methods to explore data properties.
     - During application of methods to inspect how data is being processed.
     - After applying methods to evaluate the quality of the results and compare them.
     - Depending on the audience, presentation can differ greatly.

6. Describe the importance of data pipelines and how Makefiles can be used to implement them.
   - Data pipelines are sets of processes that move and transform data from various sources to various destinations where new value can be derived; a data pipeline is a software system, thus general software best practices apply:
     - Reliable: work as expect even in face of adversity.
     - Scalable: work with increased load.
     - Maintainable: evolve throught time and teams (reduce complexity, make changes easier).
   - Makefiles are used to automate software build processes, by defining targets and rules to execute. The underlying abstraction is of a dependency graph, where tasks depend on the execution of other tasks. That's why Makefiles can be used to document and setup data pipelines.

References:
- [PRI Slides: Data Collection and Preparation](https://web.fe.up.pt/~ssn/wiki/_media/teach/pri/202122/lectures/pri2122-02-data.pdf)
- [PRI Slides: Data Processing](https://web.fe.up.pt/~ssn/wiki/_media/teach/pri/202122/lectures/pri2122-02b-data-processing.pdf)

## Information Retrieval tasks and systems

1. What is the difference between information retrieval (IR) and data retrieval (DR)?
   - In an IR system, DR consists of determining which documents of a collection contain the keywords in the user query, which is not enough to satisfy the user information need (normally), while IR consists of accepting documents that contains synonyms of the query terms in the result set, even when those documents do not contain any query terms.
   - A DR system deals with data that has a well defined structure and semantics, while an IR system deals with natural language text which is not well structured.
   - DR, while providing a solution to the user of a database system, doesn't solve the problem of retrieving information about a subject or topic, while IR does.
  
2. Give examples of IR and data retrieval systems.
   - IR Systems: Search Engines, such as Google, Bing, Yahoo, ...
   - DR Systems: Relational Databases.

3. Give some examples of retrieval tasks evaluated in TREC.
   - What the problem really is.
   - Test collections.
   - Evaluation methodology.

4. What are the modules of an IR system?
   - Indexing Process.
   - Retrieval Process.
   - Evaluation Process.

References:
- [BY, Chap. 1 (Intro)](http://grupoweb.upf.edu/mir2ed/pdf/chapter1.pdf)
- [TREC tracks](https://trec.nist.gov/tracks.html)
- [The Anatomy..., Brin & Page](http://infolab.stanford.edu/~backrub/google.html)

## Information Retrieval concepts

1. What is a document, collection, term, bag of words?
   - Document: unit we have decided to build a retrieval system over.
   - Collection: group of documents over which we perform retrieval.
   - Term: indexed units (usually words, but not always).
   - Bag of words: group of words used, where the exact ordering of terms in a document is ignored and only their presence is considered.

2. Define stemming.
   - Heuristic process that chops off the ends of words in the hope of reducing inflectional forms.

3. What is an inverted index, vocabulary, postings list?
   - Inverted Index: Index that maps back from terms to the parts of a document where they occur.
   - Vocabulary: Set of terms.
   - Postings List: List, for each term, that records which documents the term occurs in. Each item is a posting.

4. What is an information need, query, results list?
   - Information Need: the topic abouth which the user desires to know more.
   - Query: what the user conveys to the computer in an attempt to communicate the information need.

5. What is a relevant result in a results list.
   - A result is relevant if it is one that the user perceives as containing information of value with respect to their personal information need.

References:
- [Manning, Chap. 1](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)
- [PRI Slides: Information Retrieval Overview](https://web.fe.up.pt/~ssn/wiki/_media/teach/pri/202122/lectures/pri2122-ir-basics.pdf)

## Vector Model

1. What is the bag of words model for a document?
For a document, the bag of words model, the exact ordering of the terms in a document is ignored but the number of occurrences of each term is material (in contrast to Boolean retrieval). We only retain information on the number of occurrences of each term.

2. What is term frequency, collection frequency, document frequency, inverse document frequency?
   - Term Frequency (tf): number of times a term occurs in a document.
   - Collection frequency: total number of times each term appears in the document collection.
   - Document frequency (df): number of documents that contain a term.
   - Inverse Document Frequency (idf): concept to incorporate the document frequency in the weight of a term: idf(term) = log(Total no. documents / df(term))

3. How do you calculate td-idf weights?
   - tf-idf(t, d) = tf(t, d) * idf(t)
   - This formula assigns a term t a weight in a document d that is:
     - highest when t occurs many times within a small number of documents.
     - lower when the term occurs fewer times in a document, or occurs in many documents.
     - lowest when the term occurs in virtually all documents.

4. How do you rank documents in the vector model?
   - TODO:

References:
- [Manning, Chap. 2 (2.2) and Chap. 6 (6.2, 6.3)](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)

## Evaluation

1. What is precision, recall, interpolated precision?
   - Precision (P): Fraction of retrieved documents that are relevant:
     - P = #(relevant items retrieved)/#(retrieved items) = P(relevant|retrieved)
   - Recall (R): Fraction of relevant documents that are retrieved:
     - R = #(relevant items retrieved)/#(relevant items) = P(retrieved|relevant)
   - Interpolated Precision: At a certain recall level r, is defined as the highests precision found for any recall level r' >= r: 
     - pinterp(r) = max p(r'), so that r'>=r.

2. What is precision at k, R-precision?
   - Precision at k: Precision at fixed low levels of retrieved results (such as 10 or 30 documents).
   - R-Precision: If there are |Rel| relevant documents for a query, we examine the top |Rel| results of a system, and fint that r are relevant, then by definition, not only is the precision r/|Rel|, but also the recall.
     - Requires having a set of known relevant documents Rel, from which we calculate the precision of the top Rel documents returned.
     - It adjusts for the size of the set of relevant documents. A perfect system could score 1 for each query, whereas, even a perfect system could only achieve a precision at 20 of 0.4 if there were only 8 relevant documents. 

3. Name the components of a test collection.
   - Document collection;
   - Test suite of information needs, expressible as queries;
   - Set of relevance judgements.

4. Why is a set of relevance judgements considered a "ground truth" for IR?
   - Because it is a binary assessment of either relevant or nonrelevant for each query-document pair.

5. Draw a precision-recall curve for capturing the evolution of precision in the ranked list of results for a query.
   - For each set of results from a search system, precision and recall values can be plotted to give a precision-recall curve.
   - If the (k+1)th document retrieved is nonrelevant then recall is the same as for the top k documents, but precision has dropped. If it is relevant, then both precision and recall increase, and the curve jags up and to the right.

6. What is an average 11-point precision-recall graph for a set of queries?
   - For each information need, the interpolated precision is measured at the 11 recall levels of 0.0, 0.1, 0.2, ..., 1.0. For each recall level, we then calculate the arithmetic mean of the interpolated precision at that recall level for each information need in the test collection. A composite precision-recall curve showing 11 points can then be graphed.

7. What is MAP, and how do you calculate it for a set of queries in a test collection?
   - Mean Average Precision provides a single-figure measure of quality across recall levels. Given a set of queries, the MAP is the mean over the Average Precision values.

References:
- [Manning, Chap. 8](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)
- [TREC Pages](http://trec.nist.gov/)

## Web Search TODO: daqui para a frente
- [ ] What are informational, transactional and navigational information needs?
- [ ] Name some differences between web search and enterprise search.
- [ ] How do you index images?
- [ ] Give examples of ranking signals used by search engines.
- [ ] What are the SCC, IN and OUT components in the view of the web as a bowtie?

## Link Analysis
- [ ] What are in-links and out-links for a web page?
- [ ] How is anchor text used in web search?
- [ ] Calculate PageRank values for a set of linked documents.
- [ ] Calculate Hub and Authority values for a set of linked documents.

## Query Processing
- [ ] Describe and distinguish between the two query processing techniques: document-at-a-time and term-at-a-time.
- [ ] In what contexts is query transformation / expansion advantageous?
- [ ] What techniques can be used to apply transformations / expansions to user queries?
- [ ] Identify and describe query expansions techniques, such as relevance feedback or pseudo-relevance feedback.
- [ ] Query processing techniques and relevance feedback strategies.

## Entity-Oriented Search
  - [ ] What is entity-oriented search= What is necessary to implement it?
  - [ ] Describe the challenges and techniques associated with building entity descriptions, entity ranking, entity linking.
  - [ ] Describe the data sources typically required for entity oriented search and its characteristics.

## Search User Interfaces
  - [ ] Identify and describe user interface techniques and elements that can be used to improve user experience in using search systems.
  - [ ] Describe how user interaction innovations and experiments can be evaluated.
  - [ ] What are design principles and heuristics?