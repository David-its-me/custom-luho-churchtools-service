import logging
import requests
from typing import Literal

logger = logging.getLogger(__name__)


class CTImageController:

    def __init__(self, domain_base_path: str, session) -> None:
        self.session = session
        self.domain = domain_base_path

    def __url_filter_options(
        type: Literal["png", "avif", "webp", "svg", "jpeg", "jpg"] = "png",
        width: int | Literal["auto"] = "auto",
        height: int | Literal["auto"] = 1080,
    ) -> str:
        return "?fm={}&q=80&w={}&h={}&crop=original".format(type, width, height)

    def get_image_png(self, image_url: str) -> bytes:

        headers = {
            "accept": "image/avif,image/webp,image/png,image/svg+xml,image/*,*/*"
        }
        params = {}

        response: requests.Response = self.session.get(
            url=image_url + self.__url_filter_options(),
            params=params,
            headers=headers,
        )
        if response.status_code == 200:
            return response.content
        logger.warning(
            "%s Something went wrong fetching events: %s",
            response.status_code,
            response.content,
        )
        return None
