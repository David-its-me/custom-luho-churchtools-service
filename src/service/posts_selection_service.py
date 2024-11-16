from client.ct_posts_client import CTPostsClient


class PostSelectionService:

    def __init__(self, postsClient: CTPostsClient ) -> None:
        self.posts_client = postsClient
        self.posts_data = None

    def getAllVisiblePostIds(self) -> list[str]:

        #if self.posts_data is None:
        self.posts_data: list[dict] = self.posts_client.load_posts()
            #TODO implement some logic to only show the latest post
            # within a group
        
        
        imageIds: list[str] = []
        for post in self.posts_data:
            imageIds.append(str(post["id"]))

        return imageIds
    
    
    def getData(self, postId: str) -> str:
        if self.posts_data is None: #Caching
            self.posts_data: list[dict] = self.posts_client.load_posts()
            #TODO implement some logic to only show the latest post
            # within a group

        for post in self.posts_data:
            if str(post["id"]) == postId:
                return post
        
        return {
            "id": postId,
            "title": "Titel",
            "content": ""
        }
    
    def getImage(self, postId: str) -> bytes:

        if self.posts_data is None: #Caching
            self.posts_data: list[dict] = self.posts_client.load_posts()
            #TODO implement some logic to only show the latest post
            # within a group

        for post in self.posts_data:
            if str(post["id"]) == postId:
                if len(post["images"]) > 0:
                    return self.posts_client.load_image(post["images"][0])
        
        return None