import json
import logging
from datetime import datetime
import os
from typing import Optional
import requests
logger = logging.getLogger(__name__)

class CTPostsClient:
    """
    This class impelements methods, to retrieve annoucement data from Churchtools
    Part definition of ChurchToolsApi which focuses on calendars.

    Args:
        ChurchToolsApiAbstract: template with minimum references
    """

    def __init__(self, domain_base_path: str, session) -> None:
        self.session = session
        self.domain = domain_base_path

        
    def fetch_posts_list(self) -> list[dict]:
        """
        Function to retrieve all post objects
        This does not include pagination yet.

        Returns:
            Dict of posts
        """
        url = self.domain + "/api/posts"
        headers = {"accept": "application/json"}
        params = {}

        response = self.session.get(url=url, params=params, headers=headers)

        if response.status_code == 200:
            response_content = json.loads(response.content)
            return response_content["data"].copy()
        logger.warning(
            "%s Something went wrong fetching events: %s",
            response.status_code,
            response.content,
        )
        return None

    def fetch_image(self, image_url: str) -> bytes :

        headers = {"accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*"}
        params = {}

        response: requests.Response = self.session.get(url=image_url + "?fm=webp&q=80&w=auto&h=1080&crop=original", params=params, headers=headers)
        if response.status_code == 200:
            return response.content
        logger.warning(
            "%s Something went wrong fetching events: %s",
            response.status_code,
            response.content,
        )
        return None