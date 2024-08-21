This is second  homework of Cloud Computing course at AUT in fall 2023

# Introduction

### What is Hadoop?
**Hadoop** is an open-source framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from a single server to thousands of machines, with a high degree of fault tolerance. Hadoop uses HDFS(Hadoop Distributed File System). to store data, and the **MapReduce** programming model to process data.

### Benefits of Using MapReduce
**MapReduce** is a programming model that allows developers to process large datasets in a distributed environment efficiently. It breaks down the task into two main functions:

-   **Map:** It processes input data and converts it into a set of key-value pairs.
-   **Reduce:** It then takes these key-value pairs, aggregates them, and produces the final result.

This model is beneficial for processing massive datasets because it allows the job to be divided and executed in parallel, increasing efficiency and reducing computation time.

## Dataset

The dataset used in this project consists of approximately **200,000 tweets** related to the U.S. election. The dataset includes 21 columns, though not all records contain values for every column (i.e., some columns may have `NULL` values). The dataset file was placed in HDFS for processing.


The homework consists of three MapReduce programs as explained below:
## Programs

### Program 1: Likes, Retweets, and Sources Count

Counts the total **likes**, **retweets**, and the usage of different sources (e.g., iPhone, Android) for tweets about **Joe Biden** and **Donald Trump**.

**Result:**
![first program result](https://github.com/mahlashrifi/MapReduce_On_Hadoop/blob/main/screenshots/result2.png)

----------

### Program 2: State-Based Tweet Analysis

Analyzes tweets from **New York**, **Texas**, **California**, and **Florida** during **9 AM to 5 PM**, showing the percentage of tweets supporting each candidate.

**Result:**
![third program result](https://github.com/mahlashrifi/MapReduce_On_Hadoop/blob/main/screenshots/result2.png)

----------

### Program 3: Geographical Tweet Analysis

Uses **latitude and longitude** to determine tweet origin from **New York** and **California**, calculating the percentage of tweets for each candidate.

**Result:**
![third program result](https://github.com/mahlashrifi/MapReduce_On_Hadoop/blob/main/screenshots/result2.png)
