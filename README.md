# Mesin Pencari Andal (Reliable Search Engine)

An internal search system designed to explore and index information available within an organization's website, focusing on inter-page link traversal using graph-based algorithmic approaches.

## Overview

This application is an internal search system that uses Breadth-First Search (BFS) or Depth-First Search (DFS) algorithms to explore the link structure of organizational websites. The system is specifically designed to help users find information scattered across multiple pages and subdomains of an organization's site.

## System Objectives

1. **Intuitive Web Interface** - Provide an easy-to-use interface for exploring organizational websites
2. **Link Structure Exploration** - Traverse the link structure of pages within a single organizational domain
3. **Automated Indexing** - Index content from every page discovered during the exploration process
4. **Keyword Search** - Enable keyword-based searching against indexed page content
5. **Route Visualization** - Provide link paths from the main page (seed URL) to search result pages
6. **Caching System** - Store crawling results to accelerate future searches

## Technical Specifications

### Technology Stack
- **Backend**: Python 3.x + Flask
- **Frontend**: HTML5, CSS3, Tailwind CSS
- **Web Scraping**: BeautifulSoup4, Requests
- **Data Processing**: Collections, Regular Expressions

### Dependencies
```bash
pip install flask requests beautifulsoup4
```

Or using requirements.txt:
```bash
pip install -r requirements.txt
```

## Installation and Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/mesin-pencari-andal.git
cd mesin-pencari-andal
```

### 2. Setup Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
flask run
```

Access the application at: `http://127.0.0.1:5000`

## Usage Guide

### Web Crawling
1. **Input Seed URL**
   - Enter the organizational URL to be used as the starting point for exploration
   - Example: `https://www.upi.edu` or `https://spada.upi.edu`

2. **Start Crawling**
   - Click the "Start Crawling" button
   - The system will explore all pages and subdomains within that domain
   - Crawling process uses BFS/DFS algorithms for systematic exploration

### Keyword Search
1. **Input Keywords**
   - Enter keywords relevant to the information you're looking for
   - Example: "scholarship", "registration", "academic calendar"

2. **Execute Search**
   - Click the "Search Now" button
   - The system will match keywords with indexed page content

3. **Search Results**
   - Results are displayed based on relevance
   - Each result includes a "View Link Route" option

## System Architecture

### Crawling Algorithm
```
1. Initialize with seed URL
2. Add URL to queue/stack (BFS/DFS)
3. For each URL:
   - Access page
   - Extract content using BeautifulSoup
   - Store data (URL, title, content, parent link)
   - Find new links within the same domain
   - Add new links to queue/stack
4. Repeat until all links are explored
```

### Data Structure
```python
{
    "url": "https://example.com/page",
    "title": "Page Title",
    "content": "Page content text",
    "parent_url": "https://example.com",
    "depth": 2
}
```

### Search and Matching
- **Method**: Case-insensitive string matching
- **Scope**: Page titles and content
- **Ranking**: Based on relevance and link depth

## Key Features

### 1. Link Route Visualization
The system displays navigation paths from seed URL to target pages:
```
https://www.upi.edu → https://www.upi.edu/faculty → https://fip.upi.edu/info/scholarships
```

### 2. Domain Filtering
Only explores links within the same domain to maintain focus and security.

### 3. Caching System
Crawling results are stored to accelerate repeated searches.

### 4. Responsive Interface
Modern and responsive interface with glassmorphism design.

## API Endpoints

### Crawling Endpoint
```http
POST /crawl
Content-Type: application/x-www-form-urlencoded

seed_url=https://spada.upi.edu/
```

### Search Endpoint
```http
POST /search
Content-Type: application/x-www-form-urlencoded

keyword=scholarship
```

## Configuration

### Crawling Settings
- **Max Depth**: Crawling depth limit
- **Request Delay**: Delay between requests to avoid overload
- **Domain Whitelist**: List of allowed domains

### Interface Settings
- **Results Per Page**: Number of results per page
- **Search Timeout**: Search timeout duration
- **Cache Duration**: Cache storage duration

## Troubleshooting

### Common Issues
1. **Connection Timeout**
   - Check internet connection
   - Verify seed URL is accessible

2. **No Results Found**
   - Ensure crawling has completed
   - Try more general keywords

3. **Memory Issues**
   - Limit crawling depth
   - Implement pagination

## Performance Optimization

- **Concurrent Requests**: Use threading for parallel crawling
- **Database Indexing**: Index frequently searched columns
- **Content Compression**: Compress stored data
- **Smart Caching**: Cache with appropriate TTL

## Security Considerations

- **Rate Limiting**: Limit requests per IP/session
- **Input Validation**: Validate all user inputs
- **Domain Restriction**: Only crawl allowed domains
- **Resource Limits**: Limit memory and CPU usage

## Behind the Scenes Process

### 1. Page Exploration (Crawling)
1. System starts from the initial URL and accesses all relevant links within that page
2. Each new link is added to a data structure (queue for BFS or stack for DFS)
3. Visited pages are extracted using BeautifulSoup to obtain:
   - Page text content
   - Next links
4. Only links within the same domain are explored (e.g., only *.upi.edu)

### 2. Data Storage
1. Each successfully visited page is stored with the following structure:
   - Page URL
   - Page title
   - Text content
   - Source link (for route tracking)

### 3. Keyword Search
1. After crawling is complete, search matches keywords with page content
2. Matching based on: Contains word
3. System outputs results based on relevance and configuration

### 4. Link Route Visualization
1. After search results appear, each result has a "View Link Route" button
2. Click this button to see the link path from the initial URL to that page
3. Displayed in format: `https://www.upi.edu → https://www.upi.edu/faculty → https://fip.upi.edu/info/scholarships`


## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Conclusion

This application is designed to support more efficient exploration of internal organizational site information. By leveraging graph algorithms and a simple search interface, users can find relevant information without having to manually navigate through many pages.

## Acknowledgments

- BeautifulSoup4 for HTML parsing
- Flask for web framework
- Tailwind CSS for styling
- BFS/DFS graph algorithms for crawling strategy
- Inter font family for modern typography
