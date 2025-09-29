This is the source code of paper Collaborative Patterns Mining in Activity Graphs




# Collaborative Pattern Mining (CPM)

An index-based collaborative pattern mining system for discovering collaborative patterns in activity graphs.

## Project Overview

This project implements an efficient collaborative pattern mining algorithm that can discover frequently occurring collaborative patterns in dynamic networks. The system supports multiple datasets including intrusion alert network, social networks, movie rating networks, music recommendation networks, and provides comprehensive experimental evaluation and visualization capabilities.

## Core Features

### 1. Collaborative Pattern Mining
- **Index-based Efficient Mining**: Uses PBI index structures to accelerate pattern discovery
- **Multi-constraint Support**: Supports temporal constraints, structural constraints, and diameter constraints
- **Frequent Pattern Discovery**: Frequent pattern mining based on support thresholds
- **Significance Testing**: Uses G-test for statistical significance validation of discovered patterns

### 2. Data Processing
- **Multi-format Data Support**: Supports various network data formats
- **Dynamic Network Processing**: Handles dynamic network data with timestamps
- **Attribute Management**: Supports multiple attribute types for nodes and edges

### 3. Experimental Evaluation
- **Multi-dataset Experiments**: Supports Delicious, Last.fm, IMDB, intrusion detection networks, etc.
- **Performance Evaluation**: Runtime analysis, memory usage, scalability analysis
- **Comparative Experiments**: Performance comparison with baseline algorithms



## Core Algorithms

### 1. Collaborative Pattern Mining Algorithm
- **Input**: Dynamic network graph, support threshold, time window, diameter constraint, support thresold
- **Output**: Frequent collaborative patterns 
- **Features**: Index-based efficient search, supports multiple constraint conditions

### 2. Community Detection Algorithm (DiaLPA)
- **Function**: Diameter-constrained label propagation algorithm
- **Purpose**: Network community discovery and structural analysis

### 3. Significance Testing
- **Method**: G-test statistical testing
- **Purpose**: Validates statistical significance of discovered patterns

## Installation and Usage

### Requirements
- Python 3.7+
- Dependencies listed in requirements.txt

### Installation Steps

1. Clone the project
```bash
git clone <repository-url>
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the main program
```bash
python main.py
```

### Parameter Configuration

In `main.py`, you can configure the following parameters:
- `dia_threshold`: Diameter threshold (default: 3)
- `time_threshold`: Time threshold (default: 4320000 seconds, i.e., 72 minutes)
- `sup_threshold`: Support threshold (default: 50)
- `data_set`: Dataset path

## Datasets

The project supports multiple datasets:

### 1. Delicious Dataset
- **File**: `src/Delicious/datasets/delicious_activity_top3.txt`
- **Description**: Social bookmarking network containing user tag activities
- **Format**: Node ID, tag, timestamp

### 2. Last.fm Dataset
- **Description**: Music recommendation network
- **Features**: User music listening records

### 3. IMDB Dataset
- **Description**: Movie rating network
- **Features**: User movie rating data

### 4. Intrusion Detection Network
- **Description**: Network security event network
- **Features**: Attacker behavior pattern analysis

## Experimental Results

### Performance Metrics
- **Runtime**: Algorithm execution time
- **Memory Usage**: Memory consumption analysis
- **Scalability**: Performance on different scale data

### Visualization
The project provides various chart generation capabilities:
- Support change charts
- Diameter constraint impact analysis
- Time window effect evaluation
- Runtime comparison

## Experimental Scripts


# Generate synthetic dataset charts
python EDBT/Syn_Nodes.py
python EDBT/Syn_Edges.py
python EDBT/Syn_Labels.py
```



## Algorithm Details

### Collaborative Pattern Mining Process

1. **Data Preprocessing**: Parse network data and build index structures
2. **Pattern Generation**: Generate candidate collaborative patterns
3. **Support Calculation**: Calculate support values for each pattern
4. **Constraint Filtering**: Apply temporal, structural, and diameter constraints
5. **Significance Testing**: Validate pattern significance using G-test
6. **Result Output**: Output frequent collaborative patterns

### Index Structure

The system uses optimized index structures to accelerate pattern search:
- **Node Index**: Maps nodes to their attributes and timestamps
- **Edge Index**: Maps edges to their temporal information
- **Pattern Index**: Maps patterns to their support values

## Performance Optimization

- **Memory-efficient data structures**
- **Parallel processing support**
- **Incremental pattern mining**
- **Cache optimization for frequent queries**

## Contributing

We welcome contributions through Issues and Pull Requests to improve the project.

## License

Please see the LICENSE file for details.



