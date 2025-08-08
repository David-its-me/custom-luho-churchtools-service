class CTPost():
    
    def __init__(self, post):
        self.post = post

    def get_url_first_image(self):
        if ('images' in self.post):
            post_images = self.post['images']
            if len(post_images) > 0:
                first_image = post_images[0]
                return first_image
        
        return None