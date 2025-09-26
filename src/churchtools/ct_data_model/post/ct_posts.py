from churchtools.ct_data_model.post.ct_post import CTPost

class CTPosts():

    def __init__(self, posts_data):
        all_posts_from_api: list[CTPost] = list(map(lambda post: CTPost(post), posts_data))
        self.posts: list[CTPost] = []
        # Make sure every post is only included once, by checking if an id is already in self.posts
        # This seems to be bug somewhere. If churchtools has more posts than the limit/page size parameter, 
        # then we receive every post more than once. 
        # 
        # But at the moment limit=200 -> so it will take a while until we have 200 posts in our
        # churchtools installation and this part of the code will become necessary.
        for post in all_posts_from_api:
            if post.get_id() not in list(map(lambda post: post.get_id(), self.posts)):
                self.posts.append(post)

    
    def get_image_urls(self) -> list[str]:
        image_urls = []
        for post in self.posts:
            image_url = post.get_url_first_image()
            if image_url is not None:
                image_urls.append(image_url)
        
        return image_urls