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
   - For a document, the bag of words model, the exact ordering of the terms in a document is ignored but the number of occurrences of each term is material (in contrast to Boolean retrieval). We only retain information on the number of occurrences of each term.

2. What is term frequency, collection frequency, document frequency, inverse document frequency?
   - Term Frequency (tf): number of times a term occurs in a document.
   - Collection frequency: total number of times each term appears in the document collection.
   - Document frequency (df): number of documents that contain a term. Always >= 1.
   - Inverse Document Frequency (idf): concept to incorporate the document frequency in the weight of a term: idf(term) = log(Total no. documents / df(term))

3. How do you calculate td-idf weights?
   - tf-idf(t, d) = tf(t, d) * idf(t)
   - This formula assigns a term t a weight in a document d that is:
     - highest when t occurs many times within a small number of documents.
     - lower when the term occurs fewer times in a document, or occurs in many documents.
     - lowest when the term occurs in virtually all documents.

4. How do you rank documents in the vector model?
   - Vector Space Model:
     - Each document is represented as a vector, with a component vector for each dictionary term.
     - td-idf weights are used as components.
     - Thus, the set of documents in a collection may be viewed as a set of vectors in a vector space, in which there is one axis for each term.
   - Cosine Similarity:
     - Similarity between 2 documents is given by the cosine of the angle between the 2 vector representations of the documents.
     - sim(d1, d2) = (vector(d1).vector(d2))/(|vector(d1)|*|vector(d2)|)
   - Queries as Vectors:
     - Queries can also be represented as vectors in a n-dimensional space, being n the number of terms in the query.
     - Basically, queries are viewed as very short documents.
     - The top ranked results for a given query are thus the documents whose vectors have the highest cosine similarity in comparison with the query vector. 

Examples: 6.2, 6.3, 6.4.

Exercises: 6.8, 6.9, 6.10, 6.11, 6.15, 6.16, 6.17.

References:
- [Manning, Chap. 2 (2.2) and Chap. 6 (6.2, 6.3)](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)

## Evaluation

1. What is precision, recall, interpolated precision?
   - Precision (P): Fraction of retrieved documents that are relevant:
     - P = #(relevant items retrieved)/#(retrieved items) = P(relevant|retrieved)
   - Recall (R): Fraction of relevant documents that are retrieved:
     - R = #(relevant items retrieved)/#(relevant items) = P(retrieved|relevant)
   - Interpolated Precision: At a certain recall level r, is defined as the highest precision found for any recall level r' >= r: 
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

Exercises: 8.1, 8.4, 8.8, 8.9.

References:
- [Manning, Chap. 8](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)
- [TREC Pages](http://trec.nist.gov/)

## Web Search
1. What are informational, transactional and navigational information needs?
   -  Informational Queries: Seek general information on a broad topic; there is tipically not a single web page that contains all the information shought; indeed, users try to assimilate information from multiple web pages.
   -  Navigational Queries: Seek the website or home page of a single entity; for such a user, the best measure of user satisfaction is Precision at 1.
   -  Transactional Queries: preludes the user performing a transaction on the Web - purchasing a product, downloading a file or making a reservation.

2. Name some differences between web search and enterprise search.
   - In enterprise search, most documents are encapsulated in varied content management systems, email applications and databases.

3. How do you index images? TODO:

4. Give examples of ranking signals used by search engines.
   - Ranking Signal/Factor: characteristic of a website that search engine algorithms might consider to calculate its rankings.
   - HTML signals: titles, descriptions, headings, alt attributes, lists;
   - Architecture signals: accessibility, page speed, URL structure, internal/outgoing links, error status codes;
   - Social signals: social shares, reputation.


5. What are the SCC, IN and OUT components in the view of the web as a bowtie?
   -  Bowtie shape: 3 major categories of web pages:
      - SCC (Strongly Connected Core): Large cluster of websites that are connected to each other.
      - IN: Cluster of websites that link to SCC, but have no tlinks from the SCC back out to them.
      - OUT: Cluster of websites that SCC links to, but have no links back into SCC.
      - Disconnected components: Neither link to SCC nor are linked from it.
   - A web surfer can pass any page in IN to any page in SCC (by following links).
   - A web surfer can pass from page in SCC to any page in OUT.
   - A web surfer can pass from any page in SCC to any other page in SCC. 
   - A web surfer can't pass from a page in SCC to any page in IN, or from a page in OUT to a page in SCC neither IN.
References:
- [Manning, Chap. 19](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)

## Link Analysis
1. What are in-links and out-links for a web page?
   - In-links: Hyperlinks into a page.
   - Out-links: Hyperlinks out of a page.

2. How is anchor text used in web search?
   - Anchor text is used to encode an hyperlink in the HTML code of a page.

3. Calculate PageRank values for a set of linked documents.
   - PageRank of a node is a value between 0 and 1.
   - It is a query-independent value computed offline that only depends on the structure of the web graph.
   - The algorithms models a random surfer who begins at a web page and, at each step, randomly chooses between the out-links to move to the next page. If the random surfer executes this "forever", he will visit some pages more frequently than others. The PageRank value of a pge represents this probability:
   - PR(a) = q/T + (1-q)*(somatório de i=1 até n de)(PR(pi)/L(pi))

4. Calculate Hub and Authority values for a set of linked documents.
   - Query-independent algorithm.
   - Starts with the answer set (e.g. pages containing the keywords).
   - Computes two scores for each page: authority score and hub score.
     - Pages with many links pointing to them are called authorities.
     - Pages with many outgoing links are called hubs.
     - A(p) = (somatório v pertencente a S, v até p de)(H(v))
     - H(p) = (somatório u pertencente a S, p até u de)(A(u))

References:
- [Manning, Chap. 21](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)

## Query Processing

1. Describe and distinguish between the two query processing techniques: document-at-a-time and term-at-a-time.
   - Document-at-a-time: calculates complete scores for documents by processing all term lists, one document at a time. At the end all documents are sorted according to their score.
   - Term-at-a-time: accumulates scores for documents by processing term lists one at a time. When all terms are processed, the accumulators contain the final scores of all matching documents.

2. In what contexts is query transformation / expansion advantageous?
   - When when we have a IR system with a poor recall and we want to increase it (have a larger set of relevant results).

3. What techniques can be used to apply transformations / expansions to user queries?
   - Query expansion/reformulation with a thesaurus or WordNet;
   - Query expansion via automatic thesaurus generation;
   - Spelling correction;
   - Relevance feedback;
   - Pseudo/Blind relevance feedback;
   - Indirect relevance feedback.

4. Identify and describe query expansions techniques, such as relevance feedback or pseudo-relevance feedback.
   - Relevance feedback
     - Involve the user in the retrieval process so as to improve the final result set. In particular, the user gives feedback on the relevance of documents in an initial set of results (e.g. Rocchio algorithm).
   - Pseudo relevance feedback
     - Method for automatic local analysis. It automates the manual part of relevance feedback, so that the user gets improved retrieval performance without an extended interaction. The methos is to do normal retrieval to find an initial set of most relevant documents, to then assume that the top k ranked documents are relevant, and finally to do relevance feedback as before under this assumption.
   - Indirect relevance feedback
     - Less reliable than explicit feedback, but more useful than pseudo relevance feedback, which contains no evidence of user judgements. While users are often reluctant to provide explicit feedback, it is easy to collect implicit feedback in large quantities for a high volume system (such as web search engine).

References:
- [PRI Slides]()
- [Manning, Chap. 9](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)
- [Croft, Chap. 5]()

## Entity-Oriented Search

1. What is entity-oriented search? What is necessary to implement it?
   - Is the search paradigm of organizing and acessing information centered around entities, and their attributes and relationships.
     - From a user perspective, entities are natural units for organizing information. Allowing users to interact with specific entities offers a richer and more effective user experience than what is provided by conventional document-based retrieval systems.
     - From a machine perspective, entities allow for a better understanding of search queries, of a document content, and even of users. Entities enable search engines to be more effective.

2. Describe the challenges and techniques associated with building entity descriptions, entity ranking, entity linking.
   - Entity Retrieval - entities as the unit of retrieval. Challenges:
     - How to represent information needs;
     - How to represent entities;
     - How to match those representation.
   - Entity Linking - entities for knowledge representation.
   - Entities for an enhanced user experience.

3. Describe the data sources typically required for entity oriented search and its characteristics.
   - Unstructured data: Treated as textual documents (e.g. sequence of words)
   - Semi-structured data: Tags or other markup to separate textual content from semantic elements (e.g. HTML objects).
   - Structured data: Adheres to a predefined schema and organized in a tabular format (e.g. relational databases). The schema defines how the data is organized and imposes constrains to ensure consistency.

References:
- [PRI Slides]()
- [Balog]()

## Search User Interfaces

1. Identify and describe user interface techniques and elements that can be used to improve user experience in using search systems.
   - Elements can be grouped in:
     - Input: features tipically try to provide either suggestions for keyword searchers, or metadata that can be browsed.
       - Search box pervades search user interfaces and users expect to find a white text field to insert their search terms into. Advantages:
         - Flexible, and uses the searchers language.
         - Informs the user of the search being made, thus an informational feature.
         - Keeping it visible allows users to use it as a control feature too.
       - Adding Metadata: can provide input, control and informational support. Example: faceted metadata, e.g. grouping results in multiple different dimensions (facets).
     - Control: features can affect either the search that was being submitted, or can organize or rearrange the results.
       - Examples: Interative query changes (e.g. "related searches"), corrections, sorting, filters.
     - Informational: features relate to how results are organized and displayed. Individual results are presented in a Search Engine Results Page (SERP). Tipically includes:
       - Title of the result;
       - Snippet of text;
       - URL for the result.
     - Personalization: search experience is tailored to the searcher. Can be based on individual data (e.g. previous searches, user location, ...) or aggregated data (e.g. activity profiles, location data, ...).
       - Can impact results ranking, search suggestions, search engine features.

2. Describe how user interaction innovations and experiments can be evaluated.
   - IR Style
     - Evaluated within a TREC-style environment, based on datasets, specific tasks, and known 'best results' for each task (calculated by human experts).
     - Given this success, an interactive track was created to take search interaction into account, but success was limited (precision and recall measures were not sufficient).
   - Empirical User Studies
     - Observing and recording actual user performance.
     - Common measurements used: number of searches, number of terms per search, number of results visited, search times, task accuracy, ...
     - Designing and conducting user studies is hard. Results can be impacted by factors such as the motivation of participants, software bugs, small user experience differences (e.g. colors difference).
   - Analytical Approaches
     - Low-cost inspection methods are used to allow evaluators to assess a design and make well informed predictions about SUI.
     - There are many analytics methods for UI and UX (e.g. heuristic evaluation, cognitive walkthrough), but fewer specifically designed for SUI.
     - Can leverage the wealth of models and experience previously developed by experts.
     - Analytics methods can only make estimates about how suitable a design is, before a formal evaluation.

3. What are design principles and heuristics?
   - Existing guidelines and best practices that can help on the design of successful search user interfaces (SUI).

References:
- [PRI Slides]()