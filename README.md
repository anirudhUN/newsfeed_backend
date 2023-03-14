# Tech NewsFeed

This is a web application that provides users with the latest technology-related news. The application fetches news articles from various sources and presents them in an easy-to-read format, with brief summaries and clickable tiles that take users to the full articles.

Users can choose to filter news articles based on categories such as laptops, Android, gaming, and more. The application also features a search function that enables users to find articles related to specific topics or keywords.

The application is built using modern web development technologies and the popular database MongoDB. It also uses APIs to fetch and display news articles......

The goal of this project is to create a convenient and engaging platform for users to stay up-to-date with the latest developments in the world of technology.

This GitHub repository contains the backend of the application. 

# Features

### Home page

The home page shows the latest 10 article summaries as tiles with an option to load older articles through an infinite scroll or view more button. The header includes the website icon, navigation pane, categories list, search functionality, and notification for any new updates or breaking news. 

### Tiles

Each tile layout has a drop shadow and consists of a title, cover image, time, source name, and summary. On hovering over the article, other details like summary, author name, and other details are available. There is a "read more" option at the bottom of the tile that redirects to the article page. The tile displays the category or topic that the story falls under, allowing the user to easily filter by topics of interest. 

### Article page

The article page displays the entire article for the summary selected on the home page, with related articles, important tags specific to the article, a share button, an option to report any errors or issues with the article or to provide feedback to the publisher, an option to view the article in a printer-friendly format, and an option to adjust the font size and change the background theme for better readability. 

### Footer

The bottom of the page will contain the comments section which shows the user comments as well as an option for a user to add their comment. The footer includes global navigation, page info, copyright info, an about us section, related links for fresh content, and privacy policy and terms of use. 

The category page includes a category-specific header or image to indicate the label and newsfeed tile but specific to the category only. The application is optimized for mobile devices with a responsive design. 

Web scraping is performed to retrieve source URLs, and RSS feed URLs from a set of publications. Data is retrieved from the RSS feed of the source for attributes such as title, description, and timestamp of the source article. The algorithm performs summarization for the articles retrieved. Attributes such as article title, summary, image URL, timestamp, source, and tags are exported to the user application based on the request from the client. After the data has been extracted, the algorithm may also perform some natural language processing (NLP) techniques on the text for collecting important tags.
