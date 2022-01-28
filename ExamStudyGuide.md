# PRI Exam Study Guide

## References

- [BY](http://grupoweb.upf.edu/mir2ed/)
- [Manning](https://nlp.stanford.edu/IR-book/)
- [Croft](https://ciir.cs.umass.edu/irbook/)
- [Balog](https://eos-book.org/)

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
   - Ownership
   - Amount of data available
   - Complexity of the data
   - Speed at which it changes
   - Duplication of data
   - Inconsistency of data
   - Cost of data

5. Identify and describe challenges and techniques related to: data cleaning, data preparation and data presentation.


6. Describe the importance of data pipelines and how Makefiles can be used to implement them.


## Information Retrieval tasks and systems
  - [ ] What is the difference between information retrieval and data retrieval?
  - [ ] Give examples of IR and data retrieval systems.
  - [ ] Give some examples of retrieval tasks evaluated in TREC.
  - [ ] What are the modules of an IR system?

## Information Retrieval concepts
  - [ ] What is a document, collection, term, bag of words?
  - [ ] Define stemming.
  - [ ] What is an inverted index, vocabulary, postings list?
  - [ ] What is an information need, query, results list?
  - [ ] What is a relevant result in a results list.

## Vector Model
  - [ ] What is the bag of words model for a document?
  - [ ] What is term frequency, collection frequency, document frequency, inverse documuent frequency?
  - [ ] How do you calculate td-idf weights?
  - [ ] How do you rank documents in the vector model?

## Evaluation
  - [ ] What is precision, recall, interpolated precision?
  - [ ] What is precision at k, R-precision?
  - [ ] Name the components of a test collection.
  - [ ] Why is a set of relevance judgements considered a "ground truth" for IR?
  - [ ] Draw a precision-recall curve for capturing the evolution of precision in the ranked list of results for a query.
  - [ ] What is an average 11-point precision-recall graph for a set of queries?
  - [ ] What is MAP, and do you calculate it for a set of queries in a test collection?

## Web Search
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