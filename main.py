import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.rss_services import process_rss_feeds

if __name__ == '__main__':
    process_rss_feeds()
