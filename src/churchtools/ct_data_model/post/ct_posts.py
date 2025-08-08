from churchtools.ct_data_model.post.ct_post import CTPost

class CTPosts():

    def __init__(self, posts):
        self.posts = list(map(lambda post: CTPost(post), posts))
    
    def get_image_urls(self) -> list[str]:
        image_urls = []
        for post in self.posts:
            image_url = post.get_url_first_image()
            if image_url is not None:
                image_urls.append(image_url)
        
        return image_urls