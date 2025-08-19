    ---
    marp: true
    title: ChronoDB Product Documentation
    author: Technical Writer
    paginate: true
    math: katex
    theme: chrono-theme
    ---
    
    <!-- 
    This is our custom theme definition. 
    We're creating a new theme called 'chrono-theme' by extending the built-in 'uncover' theme.
    This allows us to set custom fonts, colors, and styles for the entire presentation.
    -->
    <!-- theme:
    @theme chrono-theme
    @import 'uncover';
    
    section {
      background-color: #1a202c;
      color: #e2e8f0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    h1, h2, h3 {
      font-family: 'Inter', 'Helvetica Neue', sans-serif;
      color: #63b3ed;
    }

    a {
      color: #63b3ed;
    }
    -->
    
    <!-- _class: lead -->
    # **ChronoDB**
    ### High-Performance Time-Series Database
    
    ---
    
    ## Agenda
    
    1.  **Introduction:** What is ChronoDB?
    2.  **Core Architecture:** How it Works
    3.  **Query Engine:** Performance & Complexity
    4.  **Getting Started:** Code Examples
    5.  **Q&A**
    
    **Contact:** [23f1001207@ds.study.iitm.ac.in](mailto:23f1001207@ds.study.iitm.ac.in)
    
    ---
    
    <!-- 
    Here we use a 'scoped' style tag to create a two-column layout for this slide only.
    This is a powerful feature for custom slide designs.
    -->
    <style scoped>
    .columns {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 2rem;
    }
    </style>
    
    ## What is ChronoDB?
    
    <div class="columns">
    <div>
    
    ChronoDB is a purpose-built database optimized for ingesting and querying large volumes of time-stamped data.
    
    - **Optimized for Speed:** Built from the ground up in Rust.
    - **Massively Scalable:** Distributed and fault-tolerant by design.
    - **Developer Friendly:** SQL-like query language and simple APIs.
    
    </div>
    <div>
    
    **Ideal Use Cases:**
    - IoT Sensor Data
    - Application Metrics
    - Financial Market Data
    - Log Aggregation
    
    </div>
    </div>
    
    ---
    
    <!-- 
    This slide demonstrates a background image.
    We use directives to set the image URL, dim it for readability, and set the text color to white.
    -->
    <!-- 
    _backgroundImage: "url('https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=3600')"
    _backgroundSize: cover
    _backgroundColor: #0009
    _color: white
    -->
    
    ## Core Architecture
    
    ChronoDB uses a distributed log-structured merge-tree (LSMT) architecture for efficient writes and compressed storage.
    
    - **Ingestion Nodes:** Handle incoming data streams.
    - **Storage Nodes:** Persist data in compressed blocks.
    - **Query Nodes:** Parallelize queries across storage nodes.
    
    ---
    
    ## Query Engine Performance
    
    Our proprietary query engine uses a time-based indexing algorithm to achieve rapid lookups. The average time complexity for a typical range query is:
    
    $$
    O(\log n)
    $$
    
    Where *n* is the number of data points in the queried time range. This ensures consistently fast performance even as data volume grows.
    
    ---
    
    ## Getting Started: Code Example
    
    Querying data is simple with our SQL-like interface.
    
    ```sql
    SELECT 
        AVG(cpu_usage)
    FROM 
        server_metrics
    WHERE 
        time > NOW() - 1h 
        AND location = 'us-east-1'
    GROUP BY 
        WINDOW(5m);
    ```
    
    ---
    
    <!-- _class: lead -->
    ## Thank You
    
    **Questions?**
    
    Find the full documentation at `docs.chronodb.dev`
    
    </div>
    
